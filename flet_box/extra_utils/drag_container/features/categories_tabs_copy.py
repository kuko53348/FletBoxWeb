import flet as ft


Tabs = ft.Tabs(height=450, tabs=[])


Tab = ft.Tab(
    text="Tab 1",
    content=ft.Container(
        bgcolor="white12",
        content=ft.Column(),
    ),
)
