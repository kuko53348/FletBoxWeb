import flet as ft

from markdown_code_editor.markdown_code_editor import code_editor
from .custom_widgets import custom_widgets, custom_image_dict, parse_widget_to_string
from .icons_widgets import icons_widgets
from .parse_data import parse_data
from .flet_widgets import (
    layouts_witgets,
    buttons_witgets,
    cupertino_witgets,
    charts_witgets,
    selection_witgets,
)
from .custom_cards_widgets import custom_cards_witgets, parse_cards_widget_to_string

icons_widgets_dict = icons_widgets()


class header_menu(ft.Container):

    def __init__(
        self,
        page: object = None,
        visible_selection: object = None,
    ):
        super().__init__()
        self.page = page
        self.visible_selection = visible_selection
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors("black"),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )
        self.bgcolor = ft.Colors.with_opacity(opacity=0.09, color=ft.Colors("white"))
        self.padding = ft.padding.only(left=4, top=0, right=2, bottom=0)
        self.margin = ft.margin.only(left=0, top=0, right=0, bottom=0)
        self.alignment = ft.alignment.center
        self.content = ft.Row(
            scroll=ft.ScrollMode.HIDDEN,
            spacing=4,
            run_spacing=4,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            controls=[
                ft.IconButton(
                    tooltip="Customs",
                    icon="fact_check_rounded",
                    on_click=lambda _: self.show_visible_selection(
                        index=1,
                        change_icon=_.control,
                    ),
                ),
                ft.IconButton(
                    tooltip="Customs Cards",
                    icon="co_present_outlined",
                    on_click=lambda _: self.show_visible_selection(
                        index=2,
                        change_icon=_.control,
                    ),
                ),
                ft.IconButton(
                    tooltip="Layouts",
                    icon="grid_view_outlined",
                    on_click=lambda _: self.show_visible_selection(
                        index=3,
                        change_icon=_.control,
                    ),
                ),
                ft.IconButton(
                    tooltip="Buttons",
                    icon="generating_tokens_outlined",
                    on_click=lambda _: self.show_visible_selection(
                        index=4,
                        change_icon=_.control,
                    ),
                ),
                ft.IconButton(
                    tooltip="Cupertino",
                    icon="perm_contact_cal_outlined",
                    on_click=lambda _: self.show_visible_selection(
                        index=5,
                        change_icon=_.control,
                    ),
                ),
                ft.IconButton(
                    tooltip="Selection",
                    icon="check_box_outlined",
                    on_click=lambda _: self.show_visible_selection(
                        index=6,
                        change_icon=_.control,
                    ),
                ),
                ft.IconButton(
                    tooltip="Charts",
                    icon="insert_chart_outlined_rounded",
                    on_click=lambda _: self.show_visible_selection(
                        index=7,
                        change_icon=_.control,
                    ),
                ),
            ],
        )

    def show_visible_selection(
        self, index: int = int(), change_icon: object = None
    ) -> None:
        check_visible_widget = self.visible_selection.content.controls[index].visible
        self.visible_selection.content.controls[index].visible = (
            False if check_visible_widget else True
        )

        if change_icon.icon == "fact_check_rounded":
            change_icon.icon = "fact_check_outlined"

        elif change_icon.icon == "fact_check_outlined":
            change_icon.icon = "fact_check_rounded"

        elif change_icon.icon == "co_present_outlined":
            change_icon.icon = "co_present_rounded"

        elif change_icon.icon == "co_present_rounded":
            change_icon.icon = "co_present_outlined"

        elif change_icon.icon == "grid_view_rounded":
            change_icon.icon = "grid_view_outlined"

        elif change_icon.icon == "grid_view_outlined":
            change_icon.icon = "grid_view_rounded"

        elif change_icon.icon == "generating_tokens_rounded":
            change_icon.icon = "generating_tokens_outlined"

        elif change_icon.icon == "generating_tokens_outlined":
            change_icon.icon = "generating_tokens_rounded"

        elif change_icon.icon == "perm_contact_cal_rounded":
            change_icon.icon = "perm_contact_cal_outlined"

        elif change_icon.icon == "perm_contact_cal_outlined":
            change_icon.icon = "perm_contact_cal_rounded"

        elif change_icon.icon == "check_box_rounded":
            change_icon.icon = "check_box_outlined"

        elif change_icon.icon == "check_box_outlined":
            change_icon.icon = "check_box_rounded"

        elif change_icon.icon == "insert_chart_rounded":
            change_icon.icon = "insert_chart_outlined_rounded"

        elif change_icon.icon == "insert_chart_outlined_rounded":
            change_icon.icon = "insert_chart_rounded"

        change_icon.update()
        self.visible_selection.content.update()


class dragg_box_container(ft.Container):

    def __init__(
        self,
        page: object = None,
        left_menu: object = None,
        text_box: str = "",
        tag_id: str = "",
        hide_text: bool = False,
        bg_image: str = "image136.jpeg",
        text_selection_widget: object = None,
    ) -> None:
        super().__init__()

        self.page = page
        self.tooltip = text_box
        self.tag_id = tag_id
        self.text_selection_widget = text_selection_widget

        self.border_radius = ft.border_radius.only(
            top_left=8, top_right=8, bottom_left=8, bottom_right=8
        )
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors("black"),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )

        self.padding = ft.padding.only(left=4, right=4, bottom=4, top=4)

        self.border = ft.border.all(width=2, color=ft.colors("grey900"))
        self.ink = True
        self.alignment = ft.alignment.center
        self.ink_color = ft.colors("red")

        tag_name = icons_widgets_dict.get(text_box, "home")

        # print(all_images)
        if hide_text:
            self.image = ft.DecorationImage(
                src=custom_image_dict(get_widget=text_box, keys=True),
                fit=ft.ImageFit.COVER,
            )
            self.height = 100
            self.width = 110
            self.content = ft.Container(
                alignment=ft.alignment.top_right,
                ink_color=ft.colors("yellow"),
                expand=True,
                bgcolor=ft.colors("black12"),
                content=ft.IconButton(
                    icon="data_array_rounded",
                    bgcolor=ft.Colors.with_opacity(
                        opacity=0.05,
                        color=ft.Colors("white"),
                    ),
                    on_click=lambda _: self.show_current_code(get_id_code=text_box),
                ),
            )
        else:
            self.bgcolor = ft.colors("grey900")
            self.height = 48
            self.width = 80
            self.content = ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=4,
                run_spacing=0,
                controls=[
                    ft.Icon(name=tag_name),
                    ft.Text(
                        value=text_box,
                        size=9,
                    ),
                ],
            )
        self.on_click = lambda widget_name: self.on_press_dragg_container(
            payload=widget_name
        )
        self.on_hover = lambda color_container: self.colored_container(
            payload=color_container
        )

    def show_current_code(self, get_id_code: str = "") -> None:
        # parse data
        dataparsed_widget = parse_widget_to_string()
        # md_code = f"```python\n>>> widget = {dataparsed_widget.get(get_id_code)}\n```"
        if dataparsed_widget.get(get_id_code) == None:
            dataparsed_widget = parse_cards_widget_to_string()

        md_code = parse_data.replace(
            "remplace_data", dataparsed_widget.get(get_id_code)
        )

        md_code = f"```python\n{md_code}\n```"

        wraper_widget_container = ft.Container(
            right=0,
            bottom=0,
            left=0,
            top=0,
        )

        self.page.overlay.append(wraper_widget_container)
        Markdown = code_editor(
            page=self.page,
            md_code=md_code,
            visible=True,
            widget=wraper_widget_container,
        )

        wraper_widget_container.content = ft.Container(
            margin=ft.margin.all(28),
            blur=ft.Blur(sigma_x=20, sigma_y=20),
            border_radius=ft.border_radius.only(
                top_left=32, top_right=32, bottom_left=32, bottom_right=32
            ),
            content=Markdown,
        )

        self.page.update()

    def on_press_dragg_container(self, payload: object = None):
        selected_in_phone_widget = self.page.session.get("selected_in_phone_widget")
        selected_in_dragg_widget = self.page.session.get("selected_in_dragg_widget")

        self.modify_left_footer_bar()

        if self.tag_id == "custom":
            tmp_widgets_id = custom_widgets
        if self.tag_id == "custom cards":
            tmp_widgets_id = custom_cards_witgets
        if self.tag_id == "layout":
            tmp_widgets_id = layouts_witgets
        if self.tag_id == "buttons":
            tmp_widgets_id = buttons_witgets
        if self.tag_id == "cupertino":
            tmp_widgets_id = cupertino_witgets
        if self.tag_id == "charts":
            tmp_widgets_id = charts_witgets
        if self.tag_id == "selection":
            tmp_widgets_id = selection_witgets

        if selected_in_phone_widget:
            if isinstance(
                selected_in_phone_widget.content,
                (
                    ft.Column,
                    ft.Row,
                    ft.Stack,
                    ft.GridView,
                    ft.ListView,
                    ft.ExpansionPanelList,
                    ft.ExpansionTile,
                    ft.ResponsiveRow,
                ),
            ):
                selected_in_phone_widget.content.controls.append(
                    ft.Container(
                        tooltip=self.tooltip,
                        padding=ft.padding.all(8),
                        ink=True,
                        ink_color=ft.colors("red"),
                        bgcolor=ft.colors("white12"),
                        on_click=lambda widget_name: self.set_widget_content(
                            payload=widget_name
                        ),
                        content=tmp_widgets_id(get_widget=self.tooltip),
                    )
                )
                selected_in_phone_widget.update()
            elif isinstance(selected_in_phone_widget.content, ft.Tabs):
                selected_in_phone_widget.content.tabs.append(
                    ft.Tab(
                        tab_content=ft.Icon(ft.Icons.SEARCH),
                        content=ft.Container(
                            tooltip=self.tooltip,
                            padding=ft.padding.all(8),
                            ink=True,
                            ink_color=ft.colors("red"),
                            bgcolor=ft.colors("white12"),
                            on_click=lambda widget_name: self.set_widget_content(
                                payload=widget_name
                            ),
                            content=tmp_widgets_id(get_widget=self.tooltip),
                        ),
                    )
                )
                selected_in_phone_widget.update()
            else:
                widget_selected = tmp_widgets_id(get_widget=self.tooltip)
                selected_in_phone_widget.content = widget_selected
                selected_in_phone_widget.update()

    def set_footer_selectd_widget(
        self,
        title: str = "",
        place: bool = False,
        icon_name: str = "select_all_rounded",
    ):
        # right footer selection widget
        # if True right side if false left side
        text_selection_widget = self.text_selection_widget
        # setting icon
        icon_widget = text_selection_widget.controls[place].content.controls[0].content
        icon_widget.name = icon_name
        # setting text
        header_text_widget = (
            text_selection_widget.controls[place].content.controls[1].content
        )
        header_text_widget.value = f"{title}\n"
        header_text_widget.spans[0].text = f"{self.tooltip}"

        # update widget
        text_selection_widget.update()

        return header_text_widget

    def modify_left_footer_bar(self):
        print(f"[+] <<< selected on dragg_box {self.tooltip}")
        header_text_widget = self.set_footer_selectd_widget(
            title="DRAGG BOX",
            icon_name="drag_indicator_rounded",
        )

    def set_widget_content(self, payload: object = None):
        print(f"[+] >>> selected on droop_phone {self.tooltip}")
        header_text_widget = self.set_footer_selectd_widget(
            title="PHONE BOX",
            icon_name="phone_iphone_rounded",
            place=True,
        )

        self.page.session.set("selected_in_phone_widget", payload.control)
        self.page.session.set("validate_click_selection_widget", True)

    def colored_container(self, payload: object = None):
        self.shadow.color = "red" if self.shadow.color == "black" else "black"
        self.update()


class footer_menu(ft.Container):

    def __init__(
        self,
        page: object = None,
        dragg_width: object = None,
        left_menu: object = None,
    ) -> None:
        super().__init__()
        self.page = page
        self.dragg_width = dragg_width
        self.left_menu = left_menu

        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors("black"),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )
        self.bgcolor = ft.Colors.with_opacity(opacity=0.09, color=ft.Colors("white"))
        self.padding = ft.padding.only(left=4, top=0, right=2, bottom=0)
        self.margin = ft.margin.only(left=0, top=0, right=0, bottom=0)
        self.alignment = ft.alignment.center
        self.content = ft.Row(
            spacing=0,
            run_spacing=0,
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            controls=[
                ft.IconButton(
                    icon="remove_red_eye_rounded",
                    on_click=lambda slider_value: self.hide_menu(
                        hide_menu=self.left_menu
                    ),
                ),
                ft.Slider(
                    width=100,
                    min=1,
                    max=4,
                    divisions=0.1,
                    on_change=lambda slider_value: self.change_dragg_width(
                        payload=slider_value
                    ),
                ),
                ft.Text(value="width", weight="bold"),
            ],
        )

    def change_dragg_width(self, payload: str = ""):
        slider_width = payload.control
        self.dragg_width.width = slider_width.value * 90
        self.dragg_width.update()

    def hide_menu(self, hide_menu: object = None):
        self.left_menu.visible = False if self.left_menu.visible else True
        self.left_menu.update()


class row_container_widgets(ft.Container):

    def __init__(
        self,
        page: object = None,
        run_all_widgets: str = "",
        visible: bool = True,
        tag_id: str = "",
        hide_text: bool = False,
        text_selection_widget: object = None,
    ) -> None:
        super().__init__()
        self.visible = visible
        self.page = page
        self.tag_id = tag_id
        self.expand = True
        self.expand_loose = True
        self.padding = ft.padding.only(left=0, right=0, bottom=0, top=8)
        self.text_selection_widget = text_selection_widget
        self.border = ft.border.all(
            width=1,
            color=ft.Colors.with_opacity(opacity=0.08, color=ft.colors("white")),
        )

        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors("black"),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )
        # heig
        self.alignment = ft.alignment.top_center

        self.content = ft.Row(
            wrap=True,
            scroll=ft.ScrollMode.HIDDEN,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            spacing=8,
            run_spacing=8,
            controls=[
                dragg_box_container(
                    hide_text=hide_text,
                    bg_image="logo.png",
                    page=self.page,
                    text_box=_,
                    tag_id=self.tag_id,
                    text_selection_widget=self.text_selection_widget,
                )
                for _ in run_all_widgets
            ],
        )


class dragg_container_app(ft.Container):

    custom_dict = custom_widgets(keys=False)
    custom_cards_dict = custom_cards_witgets(keys=False)

    layouts_dict = layouts_witgets(keys=False)
    buttons_dict = buttons_witgets(keys=False)
    cupertino_buttons_dict = cupertino_witgets(keys=False)
    charts_witgets_dict = charts_witgets(keys=False)
    selection_witgets_dict = selection_witgets(keys=False)

    def __init__(
        self,
        page: object = None,
        left_menu: object = None,
        text_selection_widget: object = None,
    ) -> None:
        super().__init__()
        self.page = page
        self.ink = True
        self.text_selection_widget = text_selection_widget
        self.left_menu = left_menu
        self.bgcolor = ft.colors("white12")
        self.alignment = ft.alignment.center
        self.ink_color = ft.colors("yellow")
        self.width = 360
        self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)
        self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        self.border_radius = ft.border_radius.only(
            top_left=32, top_right=32, bottom_left=32, bottom_right=32
        )
        self.border = ft.border.all(width=2, color=ft.colors("grey900"))
        self.gradient = ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.colors("transparent"), ft.colors("black12")],
        )
        self.image = ft.DecorationImage(
            src="image136.jpeg",
            fit=ft.ImageFit.COVER,
            opacity=0.05,
        )
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors("black"),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            spacing=0,
            run_spacing=0,
            controls=[
                header_menu(page=self.page, visible_selection=self),
                row_container_widgets(
                    hide_text=True,
                    tag_id="custom",
                    page=self.page,
                    run_all_widgets=self.custom_dict,
                    visible=True,
                    text_selection_widget=self.text_selection_widget,
                ),
                row_container_widgets(
                    hide_text=True,
                    tag_id="custom cards",
                    page=self.page,
                    run_all_widgets=self.custom_cards_dict,
                    visible=False,
                    text_selection_widget=self.text_selection_widget,
                ),
                row_container_widgets(
                    tag_id="layout",
                    page=self.page,
                    run_all_widgets=self.layouts_dict,
                    visible=False,
                    text_selection_widget=self.text_selection_widget,
                ),
                row_container_widgets(
                    tag_id="buttons",
                    page=self.page,
                    run_all_widgets=self.buttons_dict,
                    visible=False,
                    text_selection_widget=self.text_selection_widget,
                ),
                row_container_widgets(
                    tag_id="cupertino",
                    page=self.page,
                    run_all_widgets=self.cupertino_buttons_dict,
                    visible=False,
                    text_selection_widget=self.text_selection_widget,
                ),
                row_container_widgets(
                    tag_id="selection",
                    page=self.page,
                    run_all_widgets=self.selection_witgets_dict,
                    visible=False,
                    text_selection_widget=self.text_selection_widget,
                ),
                row_container_widgets(
                    tag_id="charts",
                    page=self.page,
                    run_all_widgets=self.charts_witgets_dict,
                    visible=False,
                    text_selection_widget=self.text_selection_widget,
                ),
                footer_menu(
                    page=self.page,
                    dragg_width=self,
                    left_menu=self.left_menu,
                ),
            ],
        )
