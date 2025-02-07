import flet as ft
import inspect
from typing import Any, List, Dict, Set, Deque, Optional
from collections import deque

import json

# import re
import requests

from ..external_library.async_requests import async_requests
from .widget_templates import widget_templates
from ..external_library.sqlite_db import sqlite_db


header = """
class FletboxUI:

    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.page = page
        self.start_app(self.page)

    def start_app(self, page: object = None):"""

footer = """
if __name__ == "__main__":
    ft.app(
        target=FletboxUI,
        assets_dir="assets",
        # name='Flet-Box',
        # route_url_strategy='assets/project_assets/',
        # use_color_emoji=True,
        # web_renderer=ft.WebRenderer.CANVAS_KIT,
        # port=8081,
    )"""

dragg_event_manager = """# DRAGG EVENTS
            on_will_accept = lambda dragg_item : self.dragg_on_will_accept(DragTargetEvent=dragg_item),
            on_leave = lambda dragg_item : self.dragg_on_leave(DragTargetEvent=dragg_item),
            on_accept = lambda dragg_item : self.dragg_on_accept(DragTargetEvent=dragg_item)"""

full_event = """
    def show_text_dragg_selected(self, name_selected: str = "") -> None:
        self.name_selected = name_selected
        self.widget_selected = self.page.session.get("SHOW_TEXT_SELECTED_DRAGG_WIDGET")
        self.draggs_selected = self.page.session.get("SHOW_TEXT_SELECTED_PHONE_WIDGET")

        self.widget_selected.content.controls[1].content.spans[0].text = "None"
        self.draggs_selected.content.controls[1].content.spans[0].text = self.name_selected
        self.widget_selected.bgcolor = ft.colors('black12')
        self.draggs_selected.bgcolor = ft.Colors.with_opacity(0.1,ft.colors('cyan'))
        self.widget_selected.update()
        self.draggs_selected.update()

    def dragg_on_will_accept(self, DragTargetEvent: object = None):
        DragTargetEvent.control.content.border = None
        DragTargetEvent.control.content.border = ft.border.all(4, ft.colors('cyan900'))
        DragTargetEvent.control.update()
        self.page.update()

    def dragg_on_accept(self, DragTargetEvent: object = None):
        # print(DragTargetEvent.control.content.content)
        self.widgetFilter = self.page.session.get("ONLY_CONTROLS_ADDING_IN_APP")

        session_id = self.page._session_id
        selectWidgetBox = self.page.session.get(session_id)

        self.InfinityBox = self.page.session.get('infinity_box')
        self.InstanceNewWidget = self.InfinityBox(
                                        dataPassed=selectWidgetBox,
                                        page=self.page
                                    )

        self.right_widget = DragTargetEvent.control.content.content
        self.right_control = self.right_widget._get_control_name()

        if self.right_control in self.widgetFilter:
            DragTargetEvent.control.content.content.controls.append(self.InstanceNewWidget)

        else:
            if self.right_control in self.widgetFilter:
                DragTargetEvent.control.content.content.controls.append(self.InstanceNewWidget)

            else:
                # GET FROM INFINITY DRAGG BOX CONTENT OF MAIN CONTAINER
                DragTargetEvent.control.content.content = self.InstanceNewWidget.widgets.get(selectWidgetBox)[0].content

        #: UPDATE COLOR WIDGET
        DragTargetEvent.control.content.border = True
        DragTargetEvent.control.content.border = ft.border.all(0, ft.colors('transparent'))
        DragTargetEvent.control.update()

        self.page.update()

    def draggin_framework(self, content: object =None) -> object():
        dragg_widget = ft.DragTarget(
            group="GroupDragg",
            on_will_accept    = lambda dragg_item : self.dragg_on_will_accept(DragTargetEvent=dragg_item), # Traslate Drop
            on_leave          = lambda dragg_item : self.dragg_on_leave(DragTargetEvent=dragg_item), # Leafing Drop Line Border
            on_accept         = lambda dragg_item : self.dragg_on_accept(DragTargetEvent=dragg_item), # Leafing Drop Line Border
        )
        dragg_widget.content = content

        return dragg_widget

    def dragg_on_leave(self, DragTargetEvent: object = None):
        DragTargetEvent.control.content.border = True
        DragTargetEvent.control.content.border = ft.border.all(0, ft.colors('transparent'))

        DragTargetEvent.control.update()
        self.page.update()

    def switch_border_selected(self, selected: object =None):
        selected_widget = self.page.session.get("SELECTED_CONTAINER")

        # print(selected_widget)
        if not selected_widget == None:
            selected_widget.border = ft.border.all(2, ft.colors('transparent'))
            selected_widget.update()

        selected.border = ft.border.all(2, ft.colors('yellow900'))
        selected.update()

        self.show_text_dragg_selected(
            name_selected=selected.content._get_control_name())

    def set_selected_widget(self, selected):
        self.page.session.set("SELECTED_CONTAINER", selected)

    def set_selected_widget_id(self, selected):
        self.page.session.set("SELECTED_CONTAINER_ID", selected.uid)

    def dragg_event(self, selected_widget: object =None):
        # def dragg_event(self,listWidget,e: ft.ContainerTapEvent):
        '''
        NOTE:

        WE CAPTURE THE CLICK SELECTION_WIDGET SHOWING BORDER COLOR YELLOW

        IF PRESS IN OTHER WIDGET WE COMPARE tmp_list listWidgetUpdate
        IF IS DIFERENT SHOW BLACK COLOR THE PREVIEW SELECT_WIDGET

        NOTE:

        WE PASS TO Build_Editor => self.infinityDropWidget[0] THAT IS CLICKED SELECTION
        Build_Editor.update_widget_attributes(widget_cliked=ft.Container(content=ft.Text()))

        '''

        # SWITCH BORDER COLOR IN SELECTED CONTAINER PHONE
        self.selected = selected_widget.control
        self.page.session.set("cover_widget", self.selected.parent.parent)

        self.switch_border_selected(selected=selected_widget.control)
        self.set_selected_widget(selected=self.selected)
        self.set_selected_widget_id(selected=self.selected)

        # print(f"[-] {self.selected.tooltip} ID: <<< dragg_event: [infinity_box_layer_one.py]")"""


class RobustWidgetSerializer:
    """
    ## Widget Serialization
    - Crate a instance to serializate

    ```python
    >>> generator = RobustWidgetSerializer()
    >>> generator.serialize(
        self.page,
    )```

    ## Hot Serialization
    - Implementation inside class

    ```python
    >>> class FletboxUI:

        def __init__(self, page: ft.Page) -> None:
            super().__init__()
            self.page = page
            self.start_app(self.page)

        def start_app(self, page: object = None):
            self.widget_data = ft.Column(
                controls=[
                    ft.Container(
                        border_radius=ft.border_radius.only(
                            top_left=8, top_right=8, bottom_left=8, bottom_right=8
                        ),
                    )
                ],
            )

            self.page.add(self.widget_data)
            generator = RobustWidgetSerializer()
            generator.serialize(
                self.page,
            )

            self.page.update()


    >>> if __name__ == "__main__":
        ft.app(
            target=FletboxUI,
            assets_dir="assets",
            # name='Flet-Box',
            # route_url_strategy='assets/project_assets/',
            # use_color_emoji=True,
            # web_renderer=ft.WebRenderer.CANVAS_KIT,
            # port=8081,
        )
    ```
    """

    def __init__(self):
        self.imports: Set[str] = set()
        self.widget_queue: Deque[ft.Control] = deque()
        self.declared: Dict[str, str] = {}  # uid -> var_name
        self.declared_widgets: Dict[str, str] = {}
        self.widget_registry: Dict[str, ft.Control] = {}
        self.widget_counter: Dict[str, int] = {}
        self.hierarchy: Dict[str, List[str]] = {}
        self.indent_size = 4

    def serialize(self, page: ft.Page, filename: str = "ui_robust.py") -> None:
        """Main serialization method with error handling"""
        try:
            self._process_widgets(page)
            declarations = self._generate_declarations()
            assignments = self._generate_assignments()
            main_code = self._generate_main_code(page)

            # WRITE ORIGINAL DRAGG SAVED DATA
            with open(filename, "w") as f:
                f.write(self._build_full_code(main_code, declarations, assignments))

            # =======================  MAKE CLEAN CODE
            revision_0 = self.process_list_widget(data_to_procces=declarations)
            revision_1 = self.process_list_widget(data_to_procces=revision_0)
            declarations_refactorized = self.process_list_widget(
                data_to_procces=revision_1
            )

            assignments_refactorized = [
                _.replace("dragtarget_", "container_")
                for _ in self._generate_assignments()
                if not _.startswith("        dragtarget_")
            ]
            main_code_refactorized = self._generate_main_code(page, local_code=True)

            # WRITE ORIGINAL DRAGG SAVED DATA
            with open("flet_box/refactorized_code.py", "w") as f:
                f.write(
                    self._build_full_code(
                        main_code_refactorized,
                        declarations_refactorized,
                        assignments_refactorized,
                        local_code=True,
                    )
                )

        except Exception as e:
            print(f"Serialization error: {str(e)}")
            raise

    def process_list_widget(self, data_to_procces: list = list()) -> list:
        clean_code = data_to_procces

        for index, _ in enumerate(clean_code):
            if _.startswith("        dragtarget_"):
                validate = clean_code.pop(index)

                for clean_index, tmp in enumerate(clean_code[index::]):
                    if tmp.startswith("        )"):
                        validate = clean_code.pop(index)
                        break
                    else:
                        validate = clean_code.pop(index)

        return clean_code

    def _process_widgets(self, page: ft.Page) -> None:
        """Process widgets with BFS and proper null checks"""
        self.widget_queue.extend(page.controls)
        self.widget_registry.clear()

        while self.widget_queue:
            widget = self.widget_queue.popleft()
            if not widget:
                continue

            uid = self._get_widget_uid(widget)
            if uid in self.declared_widgets:
                continue

            self._register_widget(widget, uid)
            self._process_children(widget, uid)

    def _register_widget(self, widget: ft.Control, uid: str) -> None:
        """Store widget metadata safely"""
        self.declared_widgets[uid] = self._generate_var_name(widget)
        self.widget_registry[uid] = widget
        self.imports.add(widget.__class__.__name__)

        import_list = [
            "Blur",
            "LinearGradient",
            "BoxShadow",
            "Alignment",
            "colors",
            "Border",
            "BorderSide",
            "Offset",
            "ButtonStyle",
        ]
        for _ in import_list:
            self.imports.add(_)

    def _process_children(self, widget: ft.Control, parent_uid: str) -> None:
        """Handle child widgets with null safety"""
        children = []
        child_uids = []

        # Process controls property
        if hasattr(widget, "controls"):
            for child in widget.controls or []:
                if child:
                    children.append(child)
                    child_uids.append(self._get_widget_uid(child))

        elif hasattr(widget, "tabs"):
            for child in widget.tabs or []:
                if child:
                    children.append(child)
                    # print(children, child, self._get_widget_uid(child))
                    child_uids.append(self._get_widget_uid(child))

        elif hasattr(widget, "actions"):
            for child in widget.actions or []:
                if child:
                    children.append(child)
                    # print(children, child, self._get_widget_uid(child))
                    child_uids.append(self._get_widget_uid(child))

        elif hasattr(widget, "segments"):
            for child in widget.actions or []:
                if child:
                    children.append(child)
                    # print(children, child, self._get_widget_uid(child))
                    child_uids.append(self._get_widget_uid(child))

        # Process content property
        elif hasattr(widget, "content") and widget.content:
            widget.on_click = "container_event"
            children.append(widget.content)
            child_uids.append(self._get_widget_uid(widget.content))

        # Update hierarchy and queue
        if child_uids:
            self.hierarchy[parent_uid] = child_uids
            self.widget_queue.extend(children)

        # print(children, self.widget_queue, self.hierarchy)

    def _generate_declarations(self) -> List[str]:
        """Generate widget declarations with error handling"""
        declarations = []
        for uid, var_name in self.declared_widgets.items():
            widget = self.widget_registry.get(uid)
            if not widget:
                continue

            try:
                args, kwargs = self._get_constructor_args(widget)
                declarations.extend(
                    [
                        f"        {var_name} = ft.{widget.__class__.__name__}(",
                        *[f"            {k}={v}," for k, v in kwargs.items()],
                        "        )\n",
                    ]
                )
            except Exception as e:
                print(f"Skipping widget {uid}: {str(e)}")
                continue

        return declarations

    def _generate_assignments(self) -> List[str]:
        """Generate hierarchy assignments safely"""
        assignments = []
        for parent_uid, child_uids in self.hierarchy.items():
            parent_var = self.declared_widgets.get(parent_uid)
            parent_widget = self.widget_registry.get(parent_uid)

            if not parent_var or not parent_widget:
                continue

            children = [
                self.declared_widgets[cid]
                for cid in child_uids
                if cid in self.declared_widgets
            ]

            if hasattr(parent_widget, "controls"):
                assignments.append(
                    f"        {parent_var}.controls = [{', '.join(children)}]"
                )

            elif hasattr(parent_widget, "tabs"):
                assignments.append(
                    f"        {parent_var}.tabs = [{', '.join(children)}]"
                )

            elif hasattr(parent_widget, "actions"):
                assignments.append(
                    f"        {parent_var}.actions = [{', '.join(children)}]"
                )

            elif hasattr(parent_widget, "segments"):
                assignments.append(
                    f"        {parent_var}.segments = [{', '.join(children)}]"
                )

            elif hasattr(parent_widget, "title"):
                assignments.append(
                    f"        {parent_var}.title = [{', '.join(children)}]"
                )

            elif hasattr(parent_widget, "content") and children:
                # print(parent_var)
                assignments.append(f"        {parent_var}.content = {children[0]}")

        # print(assignments)
        return assignments

    def _get_constructor_args(self, widget: ft.Control) -> tuple:
        """Safe constructor argument extraction"""
        try:
            params = inspect.signature(widget.__init__).parameters
        except ValueError:
            return [], {}

        kwargs = {}
        for name, param in params.items():
            if name in [
                "self",
                "args",
                "kwargs",
                "rtl",
                "image_src",
                "image_repeat",
                "image_opacity",
                "image_src_base64",
                "image_fit",
                "tooltip",
                "content",
                "controls",
                "colors",
                "ink_color",
                "tabs",
                "selected_index",
                "disabled_color",
                "on_hover",
                # "on_click",
                "on_change",
                "on_long_press",
                "on_will_accept",
                "on_accept",
                "on_leave",
            ]:
                continue

            try:
                value = getattr(widget, name)
            except AttributeError:
                continue

            if value == param.default or value is None:
                continue

            kwargs[name] = self._format_value(value)

        return [], kwargs

    def _format_value(self, value: Any, indent_level: int = 4) -> str:
        # """Comprehensive value formatting"""
        if isinstance(value, ft.Container):
            value.bgcolor = "red"
            return value

        if isinstance(value, ft.Control):
            return self.declared.get(self._get_widget_uid(value), "None")

        if isinstance(value, ft.colors):
            return f"ft.colors('{value.name.lower()}')"

        if isinstance(value, ft.Colors):
            return f"ft.Colors('{value.name.lower()}')"

        if isinstance(value, ft.CupertinoColors):
            return f"ft.Colors('{value.name.lower()}')"

        if isinstance(value, ft.Blur):
            value.tile_mode = f"{value.tile_mode}".split(" ")[0].split(".")[1].lower()
            return value

        if isinstance(value, ft.ImageFit):
            return f"ft.ImageFit('{value.name.lower()}')"

        if isinstance(value, ft.Icon):
            return f"ft.icons('{value.icons.lower()}')"

        if isinstance(value, ft.Alignment):
            return f"ft.alignment.Alignment({value.x}, {value.y})"

        # if isinstance(value, ft.GradientTileMode):
        #     return f"ft.GradientTileMode('{value.lower()}')"

        if isinstance(value, ft.LinearGradient):
            value.tile_mode = f"{value.tile_mode}".split(" ")[0].split(".")[1].lower()
            value.colors = [_.split(" ")[0] for _ in value.colors]
            return value

        if isinstance(value, ft.Border):
            # return f"ft.border.all({value.width}, {self._format_value(value.color, 0)})"
            value.top.color = f"ft.{value.top.color}".split(".")[2].lower()
            # value.bottom.color = f"ft.{value.bottom.color}"
            # value.right.color = f"ft.{value.right.color}"
            # value.left.color = f"ft.{value.left.color}"
            return value

        if isinstance(value, ft.Padding):
            return (
                f"ft.Padding({value.left}, {value.top}, {value.right}, {value.bottom})"
            )

        if isinstance(value, ft.TextStyle):
            value.weight = (
                f"ft.{value.weight}".split(".")[1].lower() if value.weight else None
            )
            value.shadow.color = (
                f"ft.{value.shadow.color}".split(".")[2].lower()
                if value.shadow.color
                else None
            )
            value.shadow.blur_style = (
                f"ft.{value.shadow.blur_style}".split(".")[2].lower()
                if value.shadow.blur_style
                else None
            )
            return f"ft.{value}"

        # Handle ButtonStyle
        if isinstance(value, ft.ButtonStyle):
            # print(value.bgcolor.split(" "), "<<<<<<<<<<<<<<<,..............")
            # value.bgcolor = {_ for _ in value.bgcolor}
            value.bgcolor = {"hovered": "blue"}
            value.padding = {"default": None}
            value.side = {"default": None}
            value.shape = {"default": None}
            value.text_style = {"default": None}
            return value
            # return self._format_button_style(value, indent_level)

        # if isinstance(value, ft.SubmenuButton):
        #     return self._format_submenu_button(value, indent_level)

        # if isinstance(value, ft.MenuItemButton):
        #     return self._format_menu_item_button(value)

        # if isinstance(value, ft.PopupMenuButton):
        #     return self._format_popup_menu_button(value)

        # if isinstance(value, ft.MenuBar):
        #     return self._format_menu_bar(value, indent_level)

        if isinstance(value, list):
            return f"[{', '.join(self._format_value(v, 0) for v in value)}]"

        if isinstance(value, dict):
            return f"{{{', '.join(f'{self._format_value(k, 0)}: {self._format_value(v, 0)}' for k, v in value.items())}}}"

        if isinstance(value, str):
            return f'"{value}"'

        if isinstance(value, ft.ThemeMode):
            return f"ft.{value}"

        if isinstance(value, ft.FontWeight):
            return f"ft.{value}"

        if isinstance(value, ft.TextThemeStyle):
            return f"ft.{value}"

        if isinstance(value, ft.TextOverflow):
            return f"ft.{value}"

        if isinstance(value, ft.CrossAxisAlignment):
            return f"ft.{value}"

        if isinstance(value, ft.MainAxisAlignment):
            return f"ft.{value}"

        if isinstance(value, ft.TabAlignment):
            return f"ft.{value}"

        if isinstance(value, ft.BoxShadow):
            value.color = f"{value.color.lower()}"
            value.blur_style = "outer"
            return f"{value}"

        class_filter = ["True", "False", "int", "float", "bool", "tuple"]
        class_name = value.__class__.__name__

        if not class_name in class_filter:
            # ADDING imports
            self.imports.add(class_name)
        # print(value, value.__class__)
        return repr(value)

    def _generate_main_code(self, page: ft.Page, local_code: bool = False) -> List[str]:
        """Generate page setup code with safety checks"""
        main_controls = [
            self.declared_widgets[self._get_widget_uid(c)]
            for c in page.controls
            if c and self._get_widget_uid(c) in self.declared_widgets
        ]

        if not local_code:
            return [
                f'        page.title = "{page.title}"',
                f"        page.theme_mode = {self._format_value(page.theme_mode)}",
                "        page.add(",
                f"            {', '.join(main_controls)}" if main_controls else "",
                "        )\n",
            ]
        else:
            return [
                f'        page.title = "{page.title}"',
                f"        page.theme_mode = {self._format_value(page.theme_mode)}",
                "        page.add(container_0)",
            ]

    def _build_full_code(
        self,
        main_code: List[str],
        declarations: List[str],
        assignments: List[str],
        local_code: bool = False,
    ) -> str:
        """Assemble final code with proper formatting"""
        return (
            "\n".join(
                [
                    "import flet as ft",
                    *[f"from flet import {imp}" for imp in sorted(self.imports)],
                    # "\n\nclass GeneratedUI:\n    @staticmethod\n    def create(page: ft.Page):",
                    header,
                    *declarations,
                    *assignments,
                    "\n\t\t# Main App\n\t\t# MAKE RANGE WIDGETS\n\t\t# column_1.controls = [container_4 for _ in range(20)]",
                    *main_code,
                    full_event if not local_code else "\n",
                    footer,
                    # "\n\nif __name__ == '__main__':\n    ft.app(GeneratedUI.create)",
                ]
            )
            .replace(
                '"container_event"', "lambda tmp_widget: print(tmp_widget.control)"
            )
            .replace("page=None,", "")
            .replace(
                "ft.CupertinoSegmentedButton(",
                "ft.CupertinoSegmentedButton(\n\t\t\tcontrols=[],",
            )
            .replace(
                "ft.CupertinoSlidingSegmentedButton(",
                "ft.CupertinoSlidingSegmentedButton(\n\t\t\tcontrols=[],",
            )
            .replace("ft.MenuBar(", "ft.MenuBar(\n\t\t\tcontrols=[],")
            .replace("ft.DragTarget(", "ft.DragTarget(\n\t\t\tcontent=None,")
            .replace('dataPassed="CLICK_EVENT"', dragg_event_manager)
        )

    def _get_widget_uid(self, widget: ft.Control) -> str:
        """Safe UID extraction"""
        return str(getattr(widget, "uid", id(widget)))

    def _generate_var_name(self, widget: ft.Control) -> str:
        """Generate unique variable names"""
        widget_type = widget.__class__.__name__
        count = self.widget_counter.get(widget_type, 0)
        var_name = f"{widget_type.lower()}_{count}"
        self.widget_counter[widget_type] = count + 1
        return var_name


if __name__ == "__main__":

    class FletboxUI:

        def __init__(self, page: ft.Page) -> None:
            super().__init__()
            self.page = page
            self.start_app(self.page)

        def start_app(self, page: object = None):
            self.widget_data = ft.Column(
                controls=[
                    ft.Container(
                        border_radius=ft.border_radius.only(
                            top_left=8, top_right=8, bottom_left=8, bottom_right=8
                        ),
                    )
                ],
            )

            self.page.add(self.widget_data)
            generator = RobustWidgetSerializer()
            generator.serialize(
                self.page,
            )

            self.page.update()

    ft.app(
        target=FletboxUI,
        assets_dir="assets",
        # name='Flet-Box',
        # route_url_strategy='assets/project_assets/',
        # use_color_emoji=True,
        # web_renderer=ft.WebRenderer.CANVAS_KIT,
        # port=8081,
    )
