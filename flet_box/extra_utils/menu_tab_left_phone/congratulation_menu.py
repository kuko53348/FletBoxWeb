import flet as ft


class congratulation_menu(ft.Container):

    def __init__(self, page: object = None, visible: bool=False, hide_widget: object=None):
        super().__init__()
        self.page = page
        self.visible = visible
        self.hide_widget = hide_widget

    def build(self,):
        content_container=ft.Column(
            controls=[
                ft.Container(
                    padding=ft.padding.all(16),
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        size=30,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.W_900,
                        font_family="Consolas",
                        value="Congratulation !!.",
                    )
                ),
                ft.Container(
                    padding=ft.padding.all(16),
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        size=18,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        # font_family="Consolas",
                        color=ft.colors('yellow'),
                        value="A Heartfelt Thank You to the Flet Development Team!"

                    )
                ),
                ft.Container(
                    padding=ft.padding.all(16),
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        size=18,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        # font_family="Consolas",
                        color=ft.colors('cyan'),
                        value="Dear @feodorf, @the_ethical_boy, and the entire Flet development team, Thank you for your hard work, passion, and vision. We are excited to see how Flet will evolve and inspire even more innovation in the future. Keep shining bright!",
                    )
                ),
                ft.Container(
                    padding=ft.padding.all(16),
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        size=30,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.W_900,
                        font_family="Consolas",
                        value="Project succesfully saved !!.",
                    )
                ),
            ft.Container(
                padding=ft.padding.all(8),
                margin=ft.margin.all(16),
                border_radius=ft.border_radius.all(18),
                alignment=ft.alignment.center,
                # expand=True,
                ink=True,
                height=60,
                bgcolor=ft.Colors.with_opacity(0.2, ft.colors('black')),
                content=ft.Text(
                    size=18,
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.W_900,
                    font_family="Consolas",
                    color=ft.colors('yellow'),
                    value="Go to Market Place",
                ),
                on_click=lambda _:self.go_home_page(),
            ),
            ]
        )
        self.content = content_container

    def go_home_page(self):
        # RESET ALL VIEW BY DEFAULD
        self.hide_widget.visible = True
        self.visible = False

        self.page.views[1].controls[0].visible=True
        self.page.views[1].controls[1].visible=False
        self.page.views[1].controls[2].visible=False
        self.page.views[1].update()