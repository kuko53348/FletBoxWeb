import flet as ft
from .categories import widgets_by_categories

from .categories_divider import (
    Divider,
)

from .categories_tabs import (
    Tabs,
    Tab,
)

from .categories_layout import (
    Card,
    Column,
    Container,
    GridView,
    ListView,
    ResponsiveRow,
    Row,
    Stack,
)

from .categories_buttons import (
    Button,
    ElevatedButton,
    FilledButton,
    FilledTonalButton,
    FloatingActionButton,
    IconButton,
    Icon,
    MenuItemButton,
    OutlinedButton,
    SubmenuButton,
    SegmentedButton,
    TextButton,
    PopupMenuButton,
    CupertinoButton,
    CupertinoFilledButton,
    CupertinoSegmentedButton,
    CupertinoSlidingSegmentedButton,
    CupertinoContextMenu,
    CupertinoActionSheet,
)

from .categories_text import (
    CupertinoTextField,
    Markdown,
    Text,
    TextField,
)

from .categories_images import (
    Image,
    CircleAvatar,
)

from .categories_selection import (
    AnimatedSwitcher,
    Checkbox,
    Dropdown,
    RadioGroup,
    RangeSlider,
    Slider,
    Switch,
    CupertinoCheckbox,
    CupertinoSlider,
    CupertinoSwitch,
)
from .categories_progress import (
    ProgressBar,
    ProgressRing,
)

from .categories_charts import (
    BarChart,
    LineChart,
    LineChartData,
    LineChartDataPoint,
    PieChart,
    PieChartSection,
)

from .categories_tables import (
    DataTable,
    # DataRow,
    # DataCell,
    # DataColumn,
)

PRESENTATION_TEXT: str = """Ready to make your first app!!"""
numWidget: int = 1


class Container(ft.Container):
    def __init__(
        self,
        page: object = ft.Page,
        content: object = None,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page

        self.bgcolor = ft.Colors.with_opacity(opacity=0.02, color=ft.colors("white"))
        self.alignment = ft.alignment.center
        self.padding = ft.padding.all(6)
        self.border = ft.border.all(2, ft.colors("cyan900"))
        self.tooltip = "Row"
        self.ink = True
        self.ink_color = "cyan"

        self.content = content
        self.on_click = event_manager


class DragTarget(ft.DragTarget):
    """
    NOTE:

    1. THIS IS VERY IMPORTANT WIDGET TO DRAGG AND DROP
    IS A LOOP DRAGGTARGET THAT WILL CONTAIN ALL WIDGET INSIDE.

    AND IT SELF WILL ADD WIDGETS DEPENDIND
    ROW , COLUMN , GRIDVIEW ... USE CONTROLS=[ WIDGETS, WIDGETS... ]
    REST WIDGETS USE CONTENT = WIDGET()

    2. Make widget need
    """

    md1 = """# Markdown Example Markdown allows you to easily include formatted text, images, and even formatted Dart code in your app.\n## Titles"""

    def __init__(self, dataPassed: str = str(), page: object = ft.Page):
        super().__init__(content=ft.Container())
        self.group = "GroupDragg"
        self.page = page
        self.dataPassed = "CLICK_EVENT"
        # self.dataPassed = dataPassed
        self.clip_behavior = ft.ClipBehavior.NONE

        # self.widgets = {
        #     #: SPACE LAYOUTS
        #     "Divider": [
        #         ft.Container(
        #             bgcolor=ft.colors("transparent"),
        #             alignment=ft.alignment.center,
        #             padding=ft.padding.all(6),
        #             margin=ft.margin.all(0),
        #             border=ft.border.all(0, ft.colors("transparent")),
        #             tooltip="Divider",
        #             ink=True,
        #             ink_color="red",
        #             on_click=lambda _: self.touch_widget_in_phone(
        #                 selected_widget=self.infinityDropWidget
        #             ),
        #             content=ft.Divider(),
        #         ),
        #     ],
        # }
        categorie_layout = widgets_by_categories

        self.widgets = dict()

        self.modify_widge = {
            # DIVIDERS
            "Divider": Divider(page=self.page),
            # TABS
            "Tabs": Tabs(page=self.page),
            "Tab": Tab(page=self.page),
            # LAYOUTS
            "Card": Card(page=self.page),
            "Column": Column(page=self.page),
            "Container": Container(page=self.page),
            "GridView": GridView(page=self.page),
            "ListView": ListView(page=self.page),
            "ResponsiveRow": ResponsiveRow(page=self.page),
            "Row": Row(page=self.page),
            "Stack": Stack(page=self.page),
            # BUTTONS
            "Button": Button(page=self.page),
            "ElevatedButton": ElevatedButton(page=self.page),
            "FilledButton": FilledButton(page=self.page),
            "FilledTonalButton": FilledTonalButton(page=self.page),
            "FloatingActionButton": FloatingActionButton(page=self.page),
            "IconButton": IconButton(page=self.page),
            "Icon": Icon(page=self.page),
            "OutlinedButton": OutlinedButton(page=self.page),
            # CONTROLS
            "MenuItemButton": MenuItemButton(page=self.page),
            "SubmenuButton": SubmenuButton(page=self.page),
            "SegmentedButton": SegmentedButton(page=self.page),
            "TextButton": TextButton(page=self.page),
            # CONTENT
            "PopupMenuButton": PopupMenuButton(page=self.page),
            # CUPERTINO CONTENT
            "CupertinoFilledButton": CupertinoFilledButton(page=self.page),
            # CUPERTINO CONTROLS
            "CupertinoButton": CupertinoButton(page=self.page),
            "CupertinoSegmentedButton": CupertinoSegmentedButton(page=self.page),
            "CupertinoSlidingSegmentedButton": CupertinoSlidingSegmentedButton(
                page=self.page
            ),
            "CupertinoContextMenu": CupertinoContextMenu(page=self.page),
            "CupertinoActionSheet": CupertinoActionSheet(page=self.page),
            # TEXT
            "CupertinoTextField": CupertinoTextField(page=self.page),
            "Markdown": Markdown(page=self.page),
            "Text": Text(page=self.page),
            "TextField": TextField(page=self.page),
            # IMAGE
            "Image": Image(page=self.page),
            "CircleAvatar": CircleAvatar(page=self.page),
            # SELECTION
            "AnimatedSwitcher": AnimatedSwitcher(page=self.page),
            "Checkbox": Checkbox(page=self.page),
            "Dropdown": Dropdown(page=self.page),
            "RadioGroup": RadioGroup(page=self.page),
            "RangeSlider": RangeSlider(page=self.page),
            "Slider": Slider(page=self.page),
            "Switch": Switch(page=self.page),
            # CUPERTINO SELECTION
            "CupertinoCheckbox": CupertinoCheckbox(page=self.page),
            "CupertinoSlider": CupertinoSlider(page=self.page),
            # PROGRESS
            "ProgressBar": ProgressBar(page=self.page),
            "ProgressRing": ProgressRing(page=self.page),
            # CHARTS
            "BarChart": BarChart(page=self.page),
            "LineChart": LineChart(page=self.page),
            "LineChartData": LineChartData(page=self.page),
            "LineChartDataPoint": LineChartDataPoint(page=self.page),
            "PieChart": PieChart(page=self.page),
            "PieChartSection": PieChartSection(page=self.page),
            # TABLES
            "DataTable": DataTable(page=self.page),
        }

        for full_categoryes in categorie_layout:
            for _ in categorie_layout.get(full_categoryes):
                check = self.modify_widge.get(_, None)
                self.widgets[f"{_}"] = [
                    Container(
                        event_manager=lambda _: self.touch_widget_in_phone(
                            selected_widget=self.infinityDropWidget
                        ),
                        content=check,
                    )
                ]

    def build(self):
        global numWidget

        """
        check CircleAvatar, VerticalDivider
        """

        #: ALERTS STATUS

        #: WIDGETS STATUS

        #: ESPECIAL WIDGET

        #: CHARTS LAYOUTS

        # selectWidgetBox                    = GLOBAL_VAR(get_global_var='SELECT_DRAGG')
        session_id = self.page._session_id
        selectWidgetBox = self.page.session.get(session_id)

        print(selectWidgetBox, "<<<<<<<")
        self.infinityDropWidget = self.widgets.get(selectWidgetBox)
        # self.infinityDropWidget[0].id      = f"{self.dataPassed}: {numWidget}"              # OUR ID
        # self.infinityDropWidget[0].tooltip = f"{self.dataPassed}: {numWidget}"              # TOOLTIP ID

        #: SET WIDGET DROPPED TO DICT DATABASE TO EXPORT PROYECT
        #: GLOBAL_VAR(set_global_var={'EXPORT_DATA_PHONE':{self.infinityDropWidget[0].id:self.infinityDropWidget[0]}})

        # print('============')
        # print(f"""
        #       [+]             selected_widget: {self.dataPassed},
        #       [+]             ID_widget: {numWidget},
        #       [+]             UID: {self.infinityDropWidget[0].uid}
        #       [+]             ID tooltip: {self.infinityDropWidget[0].tooltip}
        #       [+]  Content: {self.infinityDropWidget}""")
        # print('============')

        print(
            # f"{self.dataPassed} ID: <<< drag_dropped: [infinity_box_layer_one.py]  number: {numWidget} "
            f" ID: <<< drag_dropped: [infinity_box_layer_one.py]  number: {numWidget} "
        )

        # MAIN WIDGET THAT WILL BE DROPPED EACH TIME THAT DRAG ACCEPT
        self.content = self.infinityDropWidget[0]

        self.on_will_accept = self.drag_will_accept  # Traslate Drop
        self.on_leave = self.drag_leave  # Leafing Drop Line Border
        self.on_accept = lambda widget_passed: self.drag_accept(
            DragTargetEvent=widget_passed
        )

        # INDEX OF WIDGET ADDED
        numWidget += 1

        self.page.session.set("dict_widget", self.widgets)

    def show_text_dragg_selected(self, name_selected: str = "") -> None:
        # session_id = self.page._session_id
        # self.name_selected = self.page.session.get(session_id)
        self.name_selected = name_selected
        self.widget_selected = self.page.session.get("SHOW_TEXT_SELECTED_DRAGG_WIDGET")
        self.draggs_selected = self.page.session.get("SHOW_TEXT_SELECTED_PHONE_WIDGET")

        self.widget_selected.content.controls[1].content.spans[0].text = "None"
        self.draggs_selected.content.controls[1].content.spans[
            0
        ].text = self.name_selected

        self.widget_selected.bgcolor = ft.colors("black12")
        self.draggs_selected.bgcolor = "cyan,0.1"

        self.widget_selected.update()
        self.draggs_selected.update()

    def switch_border_selected(self, selected: object = None):
        selected_widget = self.page.session.get("SELECTED_CONTAINER")

        if not selected_widget == None:
            selected_widget.border = ft.border.all(2, ft.colors("transparent"))
            selected_widget.update()

        selected.border = ft.border.all(2, ft.colors("yellow900"))
        selected.update()

        self.show_text_dragg_selected(
            name_selected=selected.content._get_control_name()
        )

    def set_selected_widget(self, selected):
        self.page.session.set("SELECTED_CONTAINER", selected)

    def set_selected_widget_id(self, selected):
        self.page.session.set("SELECTED_CONTAINER_ID", selected.uid)

    def touch_widget_in_phone(self, selected_widget: object = None):
        # def touch_widget_in_phone(self,listWidget,e: ft.ContainerTapEvent):
        """
        NOTE:

        WE CAPTURE THE CLICK SELECTION_WIDGET SHOWING BORDER COLOR YELLOW

        IF PRESS IN OTHER WIDGET WE COMPARE tmp_list listWidgetUpdate
        IF IS DIFERENT SHOW BLACK COLOR THE PREVIEW SELECT_WIDGET

        NOTE:

        WE PASS TO Build_Editor => self.infinityDropWidget[0] THAT IS CLICKED SELECTION
        Build_Editor.update_widget_attributes(widget_cliked=ft.Container(content=ft.Text()))

        """

        # SWITCH BORDER COLOR IN SELECTED CONTAINER PHONE
        self.selected = selected_widget[0]
        self.page.session.set("cover_widget", self.selected.parent.parent)

        self.switch_border_selected(selected=selected_widget[0])
        self.set_selected_widget(selected=self.selected)
        self.set_selected_widget_id(selected=self.selected)

        print(
            f"[-] {self.selected.tooltip} ID: <<< touch_widget_in_phone: [infinity_box_layer_one.py]"
        )

    def return_new_widget(self, selected_widget: str = str()) -> object:
        """
        return selected widget

        :param      selected_widget:  The selected widget
        :type       selected_widget:  str
        """
        widget_selected = self.widgets.get(selected_widget)
        self.page.update()

        return widget_selected

    def drag_accept(self, DragTargetEvent: object = None) -> object:
        """
        NOTE:

        THIS PART IS VERY IMPORTANT BECAUSE IS THE LOOP OF THE DROP WIDGET THAT WE NEED APPEND OR PASS
        IN DEPENDENCY IF IS A CONTROLS USE APPEND AND IF IS A CONTENT WE PASS

        DragTargetEvent.control.parent          << before belong [row , column , gridview]
        DragTargetEvent.control                 << dragg_target
        DragTargetEvent.control.content         << dragg_target content= Container
        DragTargetEvent.control.content.content << content of Container = SelectedWidget

        DragTargetEvent.control.content.content._get_control_name()

        self.testing_wdiget = ft.DragTarget(
                    group="GroupDragg",
                    on_will_accept    = lambda dragg_item :self.dragg_on_will_accept(DragTargetEvent=dragg_item), # Traslate Drop
                    on_leave          = lambda dragg_item :self.dragg_on_leave(DragTargetEvent=dragg_item), # Leafing Drop Line Border
                    on_accept         = lambda dragg_item :self.dragg_on_accept(DragTargetEvent=dragg_item), # Leafing Drop Line Border
                    content=ft.Container(width=120,height=120,bgcolor="red")
                )

        def drag_will_accept(self,DragTargetEvent: object=None):
            DragTargetEvent.control.content.border = None
            DragTargetEvent.control.content.border = ft.border.all(4, ft.colors('cyan900'))

            DragTargetEvent.control.update()
            self.page.update()

        def dragg_on_leave(self,dragg_item: object=None):
            DragTargetEvent.control.content.border = True
            DragTargetEvent.control.content.border = ft.border.all(0, ft.colors('transparent'))

            DragTargetEvent.control.update()
            self.page.update()

        def dragg_on_accept(self,dragg_item: object=None):
            self.widgetFilter =  self.page.session.get("ONLY_CONTROLS_ADDING_IN_APP")

            session_id = self.page._session_id
            selectWidgetBox = self.page.session.get(session_id)

            self.InstanceNewWidget = Container(dataPassed=selectWidgetBox,page=self.page)
            self.right_control     = DragTargetEvent.control.content.content._get_control_name()

            if self.right_control in self.widgetFilter:
                # DragTargetEvent.control.content.content.controls.append(self.testing_wdiget)
                DragTargetEvent.control.content.content.controls.append(self.InstanceNewWidget)

            else:
                if self.right_control in self.widgetFilter:
                    DragTargetEvent.control.content.content.controls.append(self.InstanceNewWidget)

                else:
                    # SWITCH IF IS CONTENT
                    self.over_write_selected = self.return_new_widget(selected_widget=selectWidgetBox)
                    DragTargetEvent.control.content.content = self.over_write_selected[0].content


            # #: UPDATE COLOR WIDGET
            DragTargetEvent.control.content.border = True
            DragTargetEvent.control.content.border = ft.border.all(0, ft.colors('transparent'))
            DragTargetEvent.control.update()

            self.page.update()


        """

        # ROW COLUMN GRIDVIEW
        self.widgetFilter = self.page.session.get("ONLY_CONTROLS_ADDING_IN_APP")

        session_id = self.page._session_id
        selectWidgetBox = self.page.session.get(session_id)

        self.InstanceNewWidget = DragTarget(dataPassed=selectWidgetBox, page=self.page)
        self.right_control = DragTargetEvent.control.content.content._get_control_name()

        if self.right_control in self.widgetFilter:
            self.is_control = (
                DragTargetEvent.control.content.content._get_control_name()
            )

            print(self.is_control, "<++++++++")
            if self.is_control == "tabs":

                self.payload = ft.Container(
                    content=self.modify_widge.get("column"),
                )

                DragTargetEvent.control.content.content.tabs.append(
                    ft.Tab(text="Tabs", content=self.InstanceNewWidget)
                )

            elif (
                self.is_control == "column"
                or self.is_control == "row"
                or self.is_control == "stack"
                or self.is_control == "responsiverow"
                or self.is_control == "listview"
                or self.is_control == "gridview"
            ):

                DragTargetEvent.control.content.content.controls.append(
                    self.InstanceNewWidget
                )

        else:
            if self.right_control in self.widgetFilter:
                DragTargetEvent.control.content.content.controls.append(
                    self.InstanceNewWidget
                )

            else:
                # SWITCH IF IS CONTENT
                self.over_write_selected = self.return_new_widget(
                    selected_widget=selectWidgetBox
                )
                DragTargetEvent.control.content.content = self.over_write_selected[
                    0
                ].content

        # #: UPDATE COLOR WIDGET
        DragTargetEvent.control.content.border = True
        DragTargetEvent.control.content.border = ft.border.all(
            0, ft.colors("transparent")
        )
        DragTargetEvent.control.update()

        self.page.update()

        # RUN ONLY IN PRODUCTION
        # print(selectWidgetBox,"==",self.right_control)

    def drag_will_accept(self, DragTargetEvent: object = None):
        """
        : UPDATE COLOR WIDGET
        NOTE:

        THIS PART IS VERY IMPORTANT BECAUSE IS THE LOOP OF THE DROP WIDGET THAT WE NEED APPEND OR PASS
        IN DEPENDENCY IF IS A CONTROLS USE APPEND AND IF IS A CONTENT WE PASS

        DragTargetEvent.control.parent          << before belong [row , column , gridview]
        DragTargetEvent.control                 << dragg_target
        DragTargetEvent.control.content         << dragg_target content= Container
        DragTargetEvent.control.content.content << content of Container = SelectedWidget

        DragTargetEvent.control.content.content._get_control_name()

        self.testing_wdiget = ft.DragTarget(
            group="GroupDragg",
            on_will_accept    = lambda dragg_item :print(f"Traslate:  {dragg_item}"), # Traslate Drop
            on_leave          = lambda dragg_item :print(f"Leaving:   {dragg_item}"), # Leafing Drop Line Border
            on_accept         = lambda dragg_item :print(f"on_accept: {dragg_item}"), # Leafing Drop Line Border
            content=ft.Container(width=120,height=120,bgcolor="red")
            )
        """
        DragTargetEvent.control.content.border = None
        DragTargetEvent.control.content.border = ft.border.all(4, ft.colors("cyan900"))

        DragTargetEvent.control.update()
        self.page.update()

    def drag_leave(self, DragTargetEvent):
        """
        : UPDATE COLOR WIDGET
        NOTE:

        THIS PART IS VERY IMPORTANT BECAUSE IS THE LOOP OF THE DROP WIDGET THAT WE NEED APPEND OR PASS
        IN DEPENDENCY IF IS A CONTROLS USE APPEND AND IF IS A CONTENT WE PASS

        DragTargetEvent.control.parent          << before belong [row , column , gridview]
        DragTargetEvent.control                 << dragg_target
        DragTargetEvent.control.content         << dragg_target content= Container
        DragTargetEvent.control.content.content << content of Container = SelectedWidget

        DragTargetEvent.control.content.content._get_control_name()

        self.testing_wdiget = ft.DragTarget(
                group="GroupDragg",
                on_will_accept    = lambda dragg_item :print(f"Traslate:  {dragg_item}"), # Traslate Drop
                on_leave          = lambda dragg_item :print(f"Leaving:   {dragg_item}"), # Leafing Drop Line Border
                on_accept         = lambda dragg_item :print(f"on_accept: {dragg_item}"), # Leafing Drop Line Border
                content=ft.Container(width=120,height=120,bgcolor="red")
                )
        """

        DragTargetEvent.control.content.border = True
        DragTargetEvent.control.content.border = ft.border.all(
            0, ft.colors("transparent")
        )

        DragTargetEvent.control.update()
        self.page.update()
