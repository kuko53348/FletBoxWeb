import flet as ft


class Divider(ft.Divider):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.height = 1
        self.color = ft.Colors.with_opacity(opacity=0.2, color=ft.Colors("white"))
        self.thickness = 3
