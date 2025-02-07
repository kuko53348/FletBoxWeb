import flet as ft


class ProgressBar(ft.ProgressBar):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.width = 400
        self.color = ft.Colors("yellow")
        self.bgcolor = ft.Colors("black12")


class ProgressRing(ft.ProgressRing):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.width = 16
        self.height = 16
        self.stroke_width = 2
        self.color = ft.Colors("yellow")
        self.bgcolor = ft.Colors("black12")
