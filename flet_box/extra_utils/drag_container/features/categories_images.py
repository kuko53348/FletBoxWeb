import flet as ft


class Image(ft.Image):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page

        self.src = "logo.png"
        self.width = 200
        self.height = 200
        self.fit = ft.ImageFit.NONE
        self.repeat = ft.ImageRepeat.NO_REPEAT
        self.border_radius = ft.border_radius.all(10)


class Image(ft.Image):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page

        self.src = "logo.png"
        self.width = 200
        self.height = 200
        self.fit = ft.ImageFit.NONE
        self.repeat = ft.ImageRepeat.NO_REPEAT
        self.border_radius = ft.border_radius.all(10)


class CircleAvatar(ft.Stack):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.width = 40
        self.height = 40

    def build(self):
        self.controls = [
            ft.CircleAvatar(foreground_image_src=".my_avatar.png"),
            ft.Container(
                content=ft.CircleAvatar(bgcolor=ft.Colors.YELLOW, radius=5),
                alignment=ft.alignment.bottom_left,
            ),
        ]
