import flet as ft

from dragg_dropp_edit_attr_widgets.bool_widget import bool_widget
from dragg_dropp_edit_attr_widgets.one_number_widget import get_one_string
from dragg_dropp_edit_attr_widgets.two_number_widget import get_two_numers
from dragg_dropp_edit_attr_widgets.four_number_widget import get_four_numers
from dragg_dropp_edit_attr_widgets.linear_gradient_widget import get_linear_gradient
from dragg_dropp_edit_attr_widgets.aligment_widgets import (
    get_aligment,
    get_aligment_container,
    get_aligment_horizontal,
)
from dragg_dropp_edit_attr_widgets.dragg_dropp_edit_attr_container import (
    banner_eddit_title_container,
    main_edit_container,
)
from dragg_dropp_edit_attr_widgets.one_number_widget_with_button import (
    get_one_string_with_button,
)
from dragg_dropp_edit_attr_widgets.one_number_with_slider import (
    get_one_string_with_slider,
)


class icon_button_container(ft.Container):

    def __init__(
        self,
        page: object = None,
        content: object = None,
        footer_bar: object = None,
        icon_name: str = "home",
        tooltip: str = "",
        icon_color: str = "white",
        bgcolor: str = "transparent",
    ) -> None:
        super().__init__()
        self.page = page

        self.tooltip = tooltip
        self.border_radius = ft.border_radius.only(
            top_left=32, top_right=32, bottom_left=32, bottom_right=32
        )
        self.alignment = ft.alignment.center
        self.expand = True
        self.width = 40
        self.height = 40
        self.ink = True
        self.ink_color = ft.Colors("yellow")
        self.footer_bar = footer_bar
        self.bgcolor = ft.Colors(bgcolor)
        self.content = ft.Icon(icon_name, color=icon_color)

        self.on_click = lambda widget_name: self.setting_widget()

    def setting_widget(self):
        cheking = self.tooltip
        phone = self.page.session.get("save_data")

        selected_widget = self.page.session.get("selected_in_phone_widget")
        validation = self.page.session.get("validate_click_selection_widget")

        match cheking:
            case "Edit":
                self.set_widget_content()
                # self.adding_tab_123(tab_index=0)
                self.adding_tab_123(tab_index=1)
                self.adding_tab_123(tab_index=2)

            case "Delete":
                if selected_widget and validation == True:
                    self.page.session.set("selected_in_phone_widget", None)
                    parent_widget = selected_widget.parent

                    list_controls = getattr(parent_widget, "controls")
                    for index, _ in enumerate(list_controls):
                        if _.uid == selected_widget.uid:
                            delete_index = index

                    del parent_widget.controls[delete_index]

                    self.page.session.set("selected_in_phone_widget", None)
                    self.page.session.set("validate_click_selection_widget", False)

            case "Clean":
                phone.content.controls.clear()
                self.page.session.set("selected_in_phone_widget", phone)

            case "Rotate":
                if phone.width >= 1000:
                    return

                phone.width, phone.height = phone.height, phone.width

            case "Phone":
                phone.height = 600
                phone.width = 320

            case "Tablet":
                phone.height = 720
                phone.width = 420

            case "Pc":
                phone.height = 720
                phone.width = 1240

        phone.update()

    def set_footer_selectd_widget(
        self,
        title: str = "",
        body_text: str = "",
        place: bool = False,
        icon_name: str = "select_all_rounded",
    ):
        # right footer selection widget
        # if True right side if false left side
        text_selection_widget = self.footer_bar
        # setting icon
        icon_widget = text_selection_widget.controls[place].content.controls[0].content
        icon_widget.name = icon_name
        # setting text
        header_text_widget = (
            text_selection_widget.controls[place].content.controls[1].content
        )
        header_text_widget.value = f"{title}\n"
        header_text_widget.spans[0].text = body_text

        # update widget
        text_selection_widget.update()

    def set_widget_content(self, payload: object = None):
        # check selected widget
        selected_in_phone_widget = self.page.session.get("selected_in_phone_widget")

        # if validation is True continue
        validation = self.page.session.get("validate_click_selection_widget")

        if validation:
            self.set_footer_selectd_widget(
                title="EDITING PHONE BOX",
                body_text=selected_in_phone_widget.tooltip,
                icon_name="rebase_edit",
                place=True,
            )

    def adding_tab_123(self, tab_index: int = 1):
        selected_in_phone_widget = self.page.session.get("selected_in_phone_widget")
        tabs_widgets = self.page.session.get("tabs_containers")
        validation = self.page.session.get("validate_click_selection_widget")

        # set name of current widget
        calss_widget_name = selected_in_phone_widget.__class__.__name__

        # all tabs index
        if tab_index == 0:
            widget_tab_container = tabs_widgets.content.tabs[0].content.content.controls

        if tab_index == 1:
            widget_tab_container = tabs_widgets.content.tabs[1].content.content.controls

        if tab_index == 2:
            selected_in_phone_widget = selected_in_phone_widget.content
            calss_widget_name = selected_in_phone_widget.__class__.__name__
            widget_tab_container = tabs_widgets.content.tabs[2].content.content.controls

        # widget_tab_0 = tabs_widgets.content.tabs[0].content.content.controls
        # widget_tab_container = tabs_widgets.content.tabs[1].content.content.controls
        # widget_tab_2 = tabs_widgets.content.tabs[2].content.content.controls
        print(calss_widget_name)
        # clear specifyc tab
        bool_list = [
            "visible",
            "disabled",
            "read_only",
            "expand",
            "adaptive",
            "autofocus",
            "ink",
            "blur_on_submit",
            "multiline",
            "filled",
            "obscure_text",
            "selected",
            "checked",
            "can_scroll",
            "enebled",
            "dense",
            "scroll",
            "auto_scroll",
        ]

        slider_list = [
            "opacity",
            "aspect_ratio",
            "font_size",
            "icon_size",
            "letter_spacing",
            "line_height",
            "elevation",
            "scale",
            "padding",
            "margin",
            "border_radius",
            "width",
            "height",
            "spacing",
            "run_spacing",
            "size",
            "index",
            "selected_index",
            "item_count",
            "min",
            "max",
            "cross_axis_count",
            "main_axis_count",
            "max_lines",
            "max_length",
            "divisions",
            "min_lines",
        ]
        text_with_slider_list = [
            # "image",
            "bgcolor",
            "color",
        ]

        only_text_list = [
            "value",
            "text",
            "label",
            "hint_text",
            "tooltip",
            "src",
            "icon",
            "font_family",
            "prefix_text",
            "suffix_text",
            "place_holder",
            "link",
            "alt",
        ]

        get_two_numers_list = [
            "offset",
        ]

        get_four_numers_list = [
            "padding",
            "margin",
            "border_radius",
        ]

        get_linear_gradient_list = [
            "gradient",
        ]

        get_aligment_list = [
            "alignment",
        ]
        get_aligment_container_list = [
            "alignment",
        ]
        get_aligment_horizontal_list = [
            "vertical_alignment",
            "horizontal_alignment",
            # "run_alignment",
        ]

        # CLEAR TAB 1
        widget_tab_container.clear()

        # ------------------  BOOL TAB 1
        tmp_list_widget: list = list()

        for index, attr_widget in enumerate(only_text_list, start=1):
            check_status = self.select_widget_attribute(
                widget_to_edit=selected_in_phone_widget,
                tag_edit_widget=attr_widget,
            )

            if check_status:
                tmp_list_widget.append(
                    self.wraper_divider_widget(
                        content=get_one_string(
                            page=self.page,
                            tag_edit_widget=attr_widget,
                            widget_to_edit=selected_in_phone_widget,
                        )
                    )
                )

        # REMOVE LAST DIVIDER
        if not len(tmp_list_widget) == 0:
            tmp_list_widget[-1].controls.pop()

        self.wraper_widget(
            title="Edit one numbers widget",
            main_tab=widget_tab_container,
            controls=tmp_list_widget,
        )

        # ------------------ SLIDER
        tmp_list_widget: list = []

        for index, attr_widget in enumerate(slider_list, start=1):
            check_status = self.select_widget_attribute(
                widget_to_edit=selected_in_phone_widget,
                tag_edit_widget=attr_widget,
            )

            if check_status:
                tmp_list_widget.append(
                    self.wraper_divider_widget(
                        content=get_one_string_with_slider(
                            page=self.page,
                            tag_edit_widget=attr_widget,
                            widget_to_edit=selected_in_phone_widget,
                        )
                    )
                )

        # REMOVE LAST DIVIDER
        if not len(tmp_list_widget) == 0:
            tmp_list_widget[-1].controls.pop()

        self.wraper_widget(
            title="Edit one numbers range",
            main_tab=widget_tab_container,
            controls=tmp_list_widget,
        )

        # ------------------ SLIDER
        tmp_list_widget: list = []

        for index, attr_widget in enumerate(get_two_numers_list, start=1):
            check_status = self.select_widget_attribute(
                widget_to_edit=selected_in_phone_widget,
                tag_edit_widget=attr_widget,
            )

            if check_status:
                tmp_list_widget.append(
                    self.wraper_divider_widget(
                        content=get_two_numers(
                            page=self.page,
                            tag_edit_widget=attr_widget,
                            widget_to_edit=selected_in_phone_widget,
                        )
                    )
                )

        # REMOVE LAST DIVIDER
        if not len(tmp_list_widget) == 0:
            tmp_list_widget[-1].controls.pop()

        self.wraper_widget(
            title="Edit bool container",
            main_tab=widget_tab_container,
            controls=tmp_list_widget,
        )

        # ------------------  SLIDER
        tmp_list_widget: list = []

        for index, attr_widget in enumerate(get_four_numers_list, start=1):
            check_status = self.select_widget_attribute(
                widget_to_edit=selected_in_phone_widget,
                tag_edit_widget=attr_widget,
            )

            if check_status:
                tmp_list_widget.append(
                    self.wraper_divider_widget(
                        content=get_four_numers(
                            page=self.page,
                            tag_edit_widget=attr_widget,
                            widget_to_edit=selected_in_phone_widget,
                        )
                    )
                )

        # REMOVE LAST DIVIDER
        if not len(tmp_list_widget) == 0:
            tmp_list_widget[-1].controls.pop()

        self.wraper_widget(
            title="Edit bool container",
            main_tab=widget_tab_container,
            controls=tmp_list_widget,
        )

        # ------------------  SLIDER
        tmp_list_widget: list = []

        for index, attr_widget in enumerate(text_with_slider_list, start=1):
            check_status = self.select_widget_attribute(
                widget_to_edit=selected_in_phone_widget,
                tag_edit_widget=attr_widget,
            )

            if check_status:
                tmp_list_widget.append(
                    self.wraper_divider_widget(
                        content=get_one_string_with_button(
                            page=self.page,
                            tag_edit_widget=attr_widget,
                            widget_to_edit=selected_in_phone_widget,
                        )
                    )
                )

        # REMOVE LAST DIVIDER
        if not len(tmp_list_widget) == 0:
            tmp_list_widget[-1].controls.pop()

        self.wraper_widget(
            title="Edit one numbers",
            main_tab=widget_tab_container,
            controls=tmp_list_widget,
        )

        # ------------------ SLIDER
        tmp_list_widget: list = []

        for index, attr_widget in enumerate(bool_list, start=1):
            check_status = self.select_widget_attribute(
                widget_to_edit=selected_in_phone_widget,
                tag_edit_widget=attr_widget,
            )

            if check_status:
                tmp_list_widget.append(
                    self.wraper_divider_widget(
                        content=bool_widget(
                            page=self.page,
                            tag_edit_widget=attr_widget,
                            widget_to_edit=selected_in_phone_widget,
                        )
                    )
                )

        # REMOVE LAST DIVIDER
        if not len(tmp_list_widget) == 0:
            tmp_list_widget[-1].controls.pop()

        self.wraper_widget(
            title="Edit bool container",
            main_tab=widget_tab_container,
            controls=tmp_list_widget,
        )

        # ------------------  SLIDER
        tmp_list_widget: list = []

        filter_aligment_only = ["Row", "Column"]

        if calss_widget_name in filter_aligment_only:
            for index, attr_widget in enumerate(get_aligment_list, start=1):
                check_status = self.select_widget_attribute(
                    widget_to_edit=selected_in_phone_widget,
                    tag_edit_widget=attr_widget,
                )

                if check_status:
                    tmp_list_widget.append(
                        self.wraper_divider_widget(
                            content=get_aligment(
                                page=self.page,
                                widget_parent_name=calss_widget_name,
                                tag_edit_widget=attr_widget,
                                widget_to_edit=selected_in_phone_widget,
                            )
                        )
                    )

            # REMOVE LAST DIVIDER
            if not len(tmp_list_widget) == 0:
                tmp_list_widget[-1].controls.pop()

            self.wraper_widget(
                title="Edit bool container",
                main_tab=widget_tab_container,
                controls=tmp_list_widget,
            )

        # ------------------  SLIDER
        # tmp_list_widget: list = []

        filter_aligment_container_only = ["Container"]

        if calss_widget_name in filter_aligment_container_only:

            for index, attr_widget in enumerate(get_aligment_container_list, start=1):
                check_status = self.select_widget_attribute(
                    widget_to_edit=selected_in_phone_widget,
                    tag_edit_widget=attr_widget,
                )

                if check_status:
                    tmp_list_widget.append(
                        self.wraper_divider_widget(
                            content=get_aligment_container(
                                page=self.page,
                                tag_edit_widget=attr_widget,
                                widget_to_edit=selected_in_phone_widget,
                            )
                        )
                    )

            # REMOVE LAST DIVIDER
            if not len(tmp_list_widget) == 0:
                tmp_list_widget[-1].controls.pop()

            self.wraper_widget(
                title="Edit bool container",
                main_tab=widget_tab_container,
                controls=tmp_list_widget,
            )

        # ------------------  SLIDER
        tmp_list_widget: list = []

        for index, attr_widget in enumerate(get_aligment_horizontal_list, start=1):
            check_status = self.select_widget_attribute(
                widget_to_edit=selected_in_phone_widget,
                tag_edit_widget=attr_widget,
            )

            if check_status:
                tmp_list_widget.append(
                    self.wraper_divider_widget(
                        content=get_aligment_horizontal(
                            page=self.page,
                            tag_edit_widget=attr_widget,
                            widget_to_edit=selected_in_phone_widget,
                        )
                    )
                )

        # REMOVE LAST DIVIDER
        if not len(tmp_list_widget) == 0:
            tmp_list_widget[-1].controls.pop()

        self.wraper_widget(
            title="Edit bool container",
            main_tab=widget_tab_container,
            controls=tmp_list_widget,
        )

        # ------------------  SLIDER
        tmp_list_widget: list = []

        for index, attr_widget in enumerate(get_linear_gradient_list, start=1):
            check_status = self.select_widget_attribute(
                widget_to_edit=selected_in_phone_widget,
                tag_edit_widget=attr_widget,
            )

            if check_status:
                tmp_list_widget.append(
                    self.wraper_divider_widget(
                        content=get_linear_gradient(
                            page=self.page,
                            tag_edit_widget=attr_widget,
                            widget_to_edit=selected_in_phone_widget,
                        )
                    )
                )

        # REMOVE LAST DIVIDER
        if not len(tmp_list_widget) == 0:
            tmp_list_widget[-1].controls.pop()

        self.wraper_widget(
            title="Edit bool container",
            main_tab=widget_tab_container,
            controls=tmp_list_widget,
        )

        # ------------------  SLIDER
        tmp_list_widget: list = []

        # UPDATE ALL WIDGETS
        tabs_widgets.content.update()

    def wraper_divider_widget(self, content: object = None) -> object:
        return ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                content,
                ft.Container(
                    width=300,
                    alignment=ft.alignment.center,
                    content=ft.Divider(
                        thickness=1,
                        height=1.1,
                        opacity=0.08,
                        color=ft.Colors("white"),
                    ),
                ),
            ],
        )

    def wraper_widget(
        self, title: str = "", main_tab: object = None, controls: list = []
    ):

        main_tab.append(
            banner_eddit_title_container(
                page=self.page,
                title_container=title,
                content=main_edit_container(
                    page=self.page,
                    controls=controls,
                ),
            ),
        )

    def select_widget_attribute(
        self,
        widget_to_edit: object = None,
        tag_edit_widget: str = "",
    ) -> bool:
        filter_deprecated = [
            "event_handlers",
            "icon_size",
            "icon_enabled_color",
            "icon_disabled_color",
            "icon_content",
            "select_icon",
            "self",
            "args",
            "kwargs",
            "rtl",
            "image_src",
            "image_repeat",
            "image_opacity",
            "image_src_base64",
            "image_fit",
            "track_color",
            "inactive_track_color",
            "active_color",
            # "tooltip",
            "content",
            "controls",
            "tabs",
            "parent",
            "n",
            "selected_index",
            "on_hover",
            # "on_click",
            "on_change",
            "on_long_press",
            "on_will_accept",
            "on_accept",
            "on_leave",
            "page",
            "uid",
            "spans",
        ]

        for attr in dir(widget_to_edit):
            # try:
            if attr in filter_deprecated:
                continue
            if not attr.startswith("_") and not callable(getattr(widget_to_edit, attr)):
                # print(f"[+] > print attributes: {attr}")
                if tag_edit_widget == attr:
                    print(f"attr >>> {attr} - tag: {tag_edit_widget}")

                    value = getattr(widget_to_edit, attr)
                    data_type = type(value)

                    return True


class header_selected_widget(ft.Row):
    """ONLY FUNCTION IS SHOW SELECTED WIDGET IN PHONE"""

    def __init__(
        self,
        page: object = None,
        footer_bar: object = None,
    ):
        super().__init__()
        # main page
        self.page = page
        self.spacing = 8
        self.run_spacing = 8
        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.run_alignment = ft.CrossAxisAlignment.CENTER
        self.expand = True
        self.footer_bar = footer_bar

        self.controls = [
            ft.Container(
                border=ft.border.all(
                    width=2,
                    color=ft.Colors.with_opacity(opacity=0.1, color=ft.Colors("white")),
                ),
                border_radius=ft.border_radius.only(
                    top_left=32, top_right=32, bottom_left=32, bottom_right=32
                ),
                padding=ft.padding.only(left=4, right=4),
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.with_opacity(opacity=0.1, color=ft.Colors("white")),
                # expand=True,
                content=ft.Row(
                    spacing=4,
                    run_spacing=4,
                    controls=[
                        icon_button_container(
                            page=self.page,
                            tooltip="Edit",
                            icon_color="yellow",
                            icon_name="edit_square",
                            footer_bar=footer_bar,
                        ),
                        icon_button_container(
                            page=self.page,
                            tooltip="Delete",
                            icon_color="red",
                            icon_name="delete_forever_rounded",
                        ),
                        icon_button_container(
                            page=self.page,
                            tooltip="Clean",
                            icon_name="cleaning_services_rounded",
                            bgcolor="red500",
                        ),
                    ],
                ),
            ),
            ft.Container(
                border=ft.border.all(
                    width=2,
                    color=ft.Colors.with_opacity(opacity=0.1, color=ft.Colors("white")),
                ),
                border_radius=ft.border_radius.only(
                    top_left=32, top_right=32, bottom_left=32, bottom_right=32
                ),
                padding=ft.padding.only(left=4, right=4),
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.with_opacity(opacity=0.2, color=ft.Colors("white")),
                # expand=True,
                content=ft.Row(
                    spacing=4,
                    run_spacing=4,
                    controls=[
                        icon_button_container(
                            page=self.page,
                            tooltip="Rotate",
                            icon_color="teal200",
                            icon_name="pivot_table_chart_rounded",
                        ),
                        icon_button_container(
                            page=self.page,
                            tooltip="Phone",
                            icon_color="green200",
                            icon_name="phone_android_rounded",
                        ),
                        icon_button_container(
                            page=self.page,
                            tooltip="Tablet",
                            icon_color="orange200",
                            icon_name="tablet_android_rounded",
                        ),
                        icon_button_container(
                            page=self.page,
                            tooltip="Pc",
                            icon_color="purple200",
                            icon_name="screenshot_monitor_rounded",
                        ),
                    ],
                ),
            ),
        ]
