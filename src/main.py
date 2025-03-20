import logging

import flet as ft
from flet_box_app.flet_box_middle_app import middle_fletbox_container


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
        self.page.window.height = 780
        self.page.window.width = 1380

        self.page.on_route_change = lambda _: self.on_route_change(
            page=self.page,
            route="/",
        )

        self.page.go("/home")

    def on_route_change(self, page: object = None, route: str = str()) -> None:
        self.page = page
        self.route = route
        self.page.views.clear()

        if self.page.route == "/":
            self.page.views.append(
                page_app_view(
                    page=self.page,
                    route=self.route,
                    content=ft.ElevatedButton(
                        text="next",
                        on_click=lambda _: self.page.go("/home"),
                    ),
                )
            )
        if self.page.route == "/home":
            self.page.views.append(
                page_app_view(
                    page=self.page,
                    route=self.route,
                    content=middle_fletbox_container(page=self.page),
                )
            )

        self.page.update()


if __name__ == "__main__":
    # level: debug, info, warning, debug, panic, fatal.
    logging.basicConfig(level=logging.WARNING)
    # logging.getLogger("flet_core").setLevel(logging.INFO)
    ft.app(
        target=flet_box_app,
        assets_dir="assets",
    )
