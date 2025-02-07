import flet as ft


Image = ft.Image(
    src="logo.png",
    width=200,
    height=200,
    fit=ft.ImageFit.NONE,
    repeat=ft.ImageRepeat.NO_REPEAT,
    border_radius=ft.border_radius.all(10),
)


CircleAvatar = ft.Stack(
    width=40,
    height=40,
    controls=[
        ft.CircleAvatar(foreground_image_src=".my_avatar.png"),
        ft.Container(
            content=ft.CircleAvatar(bgcolor=ft.Colors.YELLOW, radius=5),
            alignment=ft.alignment.bottom_left,
        ),
    ],
)
