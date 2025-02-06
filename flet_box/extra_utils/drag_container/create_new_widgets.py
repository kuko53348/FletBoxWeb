import flet as ft
import os

import flet as ft


class list_widgets(ft.Container):
    def __init__(
        self, page: object = None, title: str = None, body: str = None
    ) -> None:
        super().__init__()
        self.page = page
        self.bgcolor = "white12"
        self.title = title
        self.body = body
        self.height = 40

    def build(self):
        self.content = ft.Column(
            scroll="hidden",
            controls=[
                ft.Text(value=self.title, size=12),
                ft.Text(self.body),
                ft.ElevatedButton(
                    bgcolor=ft.Colors.with_opacity(
                        0.4,
                        ft.colors("red"),
                    ),
                    text="Delete",
                    on_click=lambda _: print(_.control.parent.parent),
                ),
            ],
        )


class Remove_widget(ft.Container):
    def __init__(
        self, page: object = None, route: str = str(), content: object = None
    ) -> None:
        super().__init__()
        self.page = page
        self.route = route
        self.padding = 0
        self.bgcolor = ft.colors("white10")
        self.padding = ft.padding.all(8)
        # self.width = 320

    def build(self):
        self.content = ft.Column()

        for _ in dir(ft):
            self.content.controls.append(
                list_widgets(
                    page=self.page,
                    title=_,
                    body="hello",
                )
            )


class page_app_view(ft.View):
    """'
    ## Create frame view
    ```python
    >>> current_view = page_app_view(
    >>>				page=self.page,
    >>>				route=self.route,
    >>>				content=ft.ElevatedButton(
    >>>					text='Home',
    >>>					on_click=lambda _: self.page.go('/'),
    >>> ))
    ```
    """

    def __init__(
        self, page: object = None, route: str = str(), content: object = None
    ) -> None:
        super().__init__()
        self.page = page
        self.route = route
        self.padding = 0
        self.content = content
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

    def build(self):
        self.controls: list = [self.content]


class flet_box_app:

    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.page = page
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window.left = 3
        self.page.window.top = 3
        self.page.padding = 0
        self.page.spacing = 0
        self.page.window.height = 720
        self.page.window.width = 720
        self.page.scroll = "Hidden"

        self.page.on_route_change = lambda _: self.on_route_change(
            page=self.page,
            route="/",
        )

        self.page.go("/")

    def on_route_change(self, page: object = None, route: str = str()) -> None:
        self.page = page
        self.route = route
        self.page.views.clear()

        if self.page.route == "/":
            self.page.views.append(
                page_app_view(
                    page=self.page,
                    route=self.route,
                    content=Remove_widget(page=self.page),
                )
            )
        if self.page.route == "/home":
            self.page.views.append(
                page_app_view(
                    page=self.page,
                    route=self.route,
                    content=ft.ElevatedButton(
                        text="Home",
                        on_click=lambda _: self.page.go("/"),
                    ),
                )
            )

        self.page.update()


if __name__ == "__main__":
    ft.app(
        target=flet_box_app,
        assets_dir="assets",
        # name='Flet-Box',
        # route_url_strategy='assets/project_assets/',
        # use_color_emoji=True,
        # web_renderer=ft.WebRenderer.CANVAS_KIT,
        # port=8081,
    )
