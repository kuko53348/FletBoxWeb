import flet as ft
from flet import Offset, Tab, Alignment, BorderSide

# widget class
class fletbox_ui_0(ft.Container):

    # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    def __init__(self, page: object = None, expand: bool = True,) -> None:
        super().__init__()
        # self.shadow = ft.BoxShadow(spread_radius = 1, blur_radius  = 15, color = ft.colors('black'), offset = ft.Offset(0,0), blur_style = ft.ShadowBlurStyle.OUTER,)
        # self.image = ft.DecorationImage(src='logo.png',fit=ft.ImageFit.COVER,opacity=0.02)
        # self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        # self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)

        self.page = page
        self.bgcolor = ft.colors('transparent')
        self.expand = expand
        # self.alignment = ft.alignment.top_center

        # content of current widget
        self.content = ft.Container(
            bgcolor=ft.Colors('transparent'),
            border_radius=ft.BorderRadius(
                top_left=0, top_right=0, bottom_left=0, bottom_right=0),
            ink=True,
            ink_color=ft.Colors('red'),
            margin=ft.Margin(left=0, top=0, right=0, bottom=0),
            offset=ft.Offset(x=0, y=0),
            opacity=1.0,
            padding=ft.Padding(left=0, top=0, right=12, bottom=0),
            shadow=[],
            visible=True,
            content=ft.Container(
                border_radius=ft.BorderRadius(
                    top_left=0, top_right=0, bottom_left=0, bottom_right=0),
                margin=ft.Margin(left=0, top=0, right=0, bottom=0),
                offset=ft.Offset(x=0, y=0),
                opacity=1.0,
                padding=ft.Padding(left=0, top=0, right=0, bottom=0),
                shadow=[],
                visible=True,
                width=320,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.START,
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    opacity=1.0,
                    run_alignment=ft.CrossAxisAlignment.CENTER,
                    visible=True,
                    controls=[
                        ft.Container(
                            opacity=1.0,
                            padding=ft.Padding(
                                left=24, top=0, right=0, bottom=0),
                            shadow=[],
                            visible=True,
                            content=ft.Text(
                                enable_interactive_selection=True,
                                font_family='Consolas',
                                opacity=1.0,
                                selection_cursor_width=2.0,
                                text_align=ft.TextAlign.START,
                                value='Volumen',
                                visible=True,
                            ),
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            opacity=1.0,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            visible=True,
                            controls=[
                                ft.Slider(
                                    expand=True,
                                    max=100,
                                    opacity=1.0,
                                    value=37.618334540005385,
                                    visible=True,
                                ),
                                ft.Icon(
                                    name='volume_up',
                                    opacity=1.0,
                                    visible=True,
                                ),
                            ],
                        ),
                    ],
                ),
            ),)


class fletbox_ui_1(ft.Container):

    # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    def __init__(self, page: object = None, expand: bool = True,) -> None:
        super().__init__()
        # self.shadow = ft.BoxShadow(spread_radius = 1, blur_radius  = 15, color = ft.colors('black'), offset = ft.Offset(0,0), blur_style = ft.ShadowBlurStyle.OUTER,)
        # self.image = ft.DecorationImage(src='logo.png',fit=ft.ImageFit.COVER,opacity=0.02)
        # self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        # self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)

        self.page = page
        self.bgcolor = ft.colors('transparent')
        self.expand = expand
        # self.alignment = ft.alignment.top_center

        # content of current widget
        self.content = ft.Container(
            bgcolor=ft.Colors('transparent'),
            border_radius=ft.BorderRadius(
                top_left=0, top_right=0, bottom_left=0, bottom_right=0),
            ink=True,
            ink_color=ft.Colors('red'),
            margin=ft.Margin(left=0, top=0, right=0, bottom=0),
            offset=ft.Offset(x=0, y=0),
            opacity=1.0,
            padding=ft.Padding(left=0, top=0, right=12, bottom=0),
            shadow=[],
            visible=True,
            content=ft.Container(
                border_radius=ft.BorderRadius(
                    top_left=0, top_right=0, bottom_left=0, bottom_right=0),
                margin=ft.Margin(left=0, top=0, right=0, bottom=0),
                offset=ft.Offset(x=0, y=0),
                opacity=1.0,
                padding=ft.Padding(left=0, top=0, right=0, bottom=0),
                shadow=[],
                visible=True,
                width=320,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.START,
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    opacity=1.0,
                    run_alignment=ft.CrossAxisAlignment.CENTER,
                    visible=True,
                    controls=[
                        ft.Container(
                            opacity=1.0,
                            padding=ft.Padding(
                                left=24, top=0, right=0, bottom=0),
                            shadow=[],
                            visible=True,
                            content=ft.Text(
                                enable_interactive_selection=True,
                                font_family='Consolas',
                                opacity=1.0,
                                selection_cursor_width=2.0,
                                text_align=ft.TextAlign.START,
                                value='Volumen',
                                visible=True,
                            ),
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            opacity=1.0,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            visible=True,
                            controls=[
                                ft.Slider(
                                    expand=True,
                                    max=100,
                                    opacity=1.0,
                                    value=37.618334540005385,
                                    visible=True,
                                ),
                                ft.Icon(
                                    name='volume_up',
                                    opacity=1.0,
                                    visible=True,
                                ),
                            ],
                        ),
                    ],
                ),
            ),)


class fletbox_ui_2(ft.Container):

    # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    def __init__(self, page: object = None, expand: bool = True,) -> None:
        super().__init__()
        # self.shadow = ft.BoxShadow(spread_radius = 1, blur_radius  = 15, color = ft.colors('black'), offset = ft.Offset(0,0), blur_style = ft.ShadowBlurStyle.OUTER,)
        # self.image = ft.DecorationImage(src='logo.png',fit=ft.ImageFit.COVER,opacity=0.02)
        # self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        # self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)

        self.page = page
        self.bgcolor = ft.colors('transparent')
        self.expand = expand
        # self.alignment = ft.alignment.top_center

        # content of current widget
        self.content = ft.Container(
            bgcolor=ft.Colors('transparent'),
            border_radius=ft.BorderRadius(
                top_left=0, top_right=0, bottom_left=0, bottom_right=0),
            ink=True,
            ink_color=ft.Colors('red'),
            margin=ft.Margin(left=0, top=0, right=0, bottom=0),
            offset=ft.Offset(x=0, y=0),
            opacity=1.0,
            padding=ft.Padding(left=0, top=0, right=12, bottom=0),
            shadow=[],
            visible=True,
            content=ft.Container(
                border_radius=ft.BorderRadius(
                    top_left=0, top_right=0, bottom_left=0, bottom_right=0),
                margin=ft.Margin(left=0, top=0, right=0, bottom=0),
                offset=ft.Offset(x=0, y=0),
                opacity=1.0,
                padding=ft.Padding(left=0, top=0, right=0, bottom=0),
                shadow=[],
                visible=True,
                width=320,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.START,
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    opacity=1.0,
                    run_alignment=ft.CrossAxisAlignment.CENTER,
                    visible=True,
                    controls=[
                        ft.Container(
                            opacity=1.0,
                            padding=ft.Padding(
                                left=24, top=0, right=0, bottom=0),
                            shadow=[],
                            visible=True,
                            content=ft.Text(
                                enable_interactive_selection=True,
                                font_family='Consolas',
                                opacity=1.0,
                                selection_cursor_width=2.0,
                                text_align=ft.TextAlign.START,
                                value='Volumen',
                                visible=True,
                            ),
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            opacity=1.0,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            visible=True,
                            controls=[
                                ft.Slider(
                                    expand=True,
                                    max=100,
                                    opacity=1.0,
                                    value=37.618334540005385,
                                    visible=True,
                                ),
                                ft.Icon(
                                    name='volume_up',
                                    opacity=1.0,
                                    visible=True,
                                ),
                            ],
                        ),
                    ],
                ),
            ),)

class fletbox_ui(ft.Container):

    # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    def __init__(self, page: object = None) -> None:
        super().__init__()
        # self.shadow = ft.BoxShadow(spread_radius=1, blur_radius=15, color=ft.colors('black'), offset=ft.Offset(0,0), blur_style=ft.ShadowBlurStyle.OUTER,)
        # self.image = ft.DecorationImage(src='logo.png',fit=ft.ImageFit.COVER,opacity=0.02)
        # self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        # self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)

        self.page = page
        self.bgcolor = ft.colors('transparent')
        self.expand = True
        self.alignment = ft.alignment.top_center

        # all widgets
        self.all_instances: list = [fletbox_ui_0(page=self.page,expand=False,),fletbox_ui_1(page=self.page,expand=False,),fletbox_ui_2(page=self.page,expand=False,),]

        # content of current widget
        self.content = ft.Column(
            # tooltip = 'Column',
            # tight = True,
            # wrap = True,
            # auto_scroll = True,
            # height = 150,
            # width = 150,
            # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
            # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE

            # scroll = ft.ScrollMode.HIDDEN,
            alignment = ft.MainAxisAlignment.SPACE_AROUND,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            run_alignment = ft.CrossAxisAlignment.CENTER,
            expand = True,
            spacing = 0,
            run_spacing = 0,

            controls = self.all_instances
        )




if __name__ == "__main__":
    # Just testing MainApp

    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.DARK
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.window.left = 3
        page.window.top = 3
        page.padding = 0
        page.spacing = 0
        page.window.height = 720
        page.window.width = 320

        page.add(fletbox_ui(page=page))
        page.update()

    ft.app(
        target=main,
        assets_dir="assets",
    )
