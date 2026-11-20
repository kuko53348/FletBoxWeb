import flet as ft
from .header_selected_widget import header_selected_widget


class lite_menu_up_down_app(ft.Container):

    def __init__(
        self,
        page: object = None,
        content: object = None,
        height: int = 50,
    ) -> None:
        super().__init__()
        self.page = page
        self.tooltip = "Menu up"
        self.height = height
        self.alignment = ft.alignment.center
        self.padding = ft.padding.only(left=2, right=2, bottom=2, top=2)
        self.content = content


class drop_phone_container(ft.Container):

    def __init__(
        self,
        page: object = None,
        text_selection_widget: object = None,
    ) -> None:
        super().__init__()
        self.page = page
        self.expand = True

        self.phone_container = ft.Container(
            tooltip="Phone Container",
            border_radius=ft.border_radius.only(
                top_left=32,
                top_right=32,
                bottom_left=32,
                bottom_right=32,
            ),
            border=ft.border.all(
                width=2,
                color=ft.Colors("black12"),
            ),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            height=600,
            width=320,
            ink=True,
            ink_color=ft.Colors("red"),
            bgcolor=ft.Colors("black12"),
            alignment=ft.alignment.top_center,
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=8,
                run_spacing=8,
                controls=[],
            ),
            on_click=lambda widget_name: self.set_widget_content(payload=widget_name),
        )

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            spacing=8,
            run_spacing=8,
            controls=[
                lite_menu_up_down_app(
                    page=self.page,
                    content=header_selected_widget(
                        page=self.page,
                        footer_bar=text_selection_widget,
                    ),
                    height=55,
                ),
                self.phone_container,
                lite_menu_up_down_app(
                    page=self.page,
                    content=text_selection_widget,
                ),
            ],
        )

        self.page.session.set("save_data", self.phone_container)
        self.page.session.set("selected_in_phone_widget", self.phone_container)

    def set_widget_content(self, payload: object = None):
        # print("set widget to add more widgets")
        self.page.session.set("selected_in_phone_widget", self.phone_container)
