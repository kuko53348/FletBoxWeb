import flet as ft


class Tabs(ft.Tabs):

    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__(tabs=[])
        self.page = page
        self.height = 450
        self.event_manager = event_manager


class Tab(ft.Tab):

    def __init__(
        self,
        page: object = ft.Page,
    ):
        super().__init__()
        self.page = page
        self.text = "Tab 1"

    def build(self):
        self.content = ft.Container(
            bgcolor="white12",
            content=ft.Column(),
        )
