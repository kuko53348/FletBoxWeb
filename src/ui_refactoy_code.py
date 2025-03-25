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
                top_left=12, top_right=12, bottom_left=12, bottom_right=12),
            ink=True,
            ink_color=ft.Colors('red'),
            margin=ft.Margin(left=0, top=0, right=0, bottom=0),
            offset=ft.Offset(x=0, y=0),
            opacity=1.0,
            padding=ft.Padding(left=16, top=16, right=16, bottom=16),
            shadow=[],
            visible=True,
            width=320.0,
            content=ft.Column(
                offset=ft.Offset(x=0, y=0),
                opacity=1.0,
                scroll=ft.ScrollMode.HIDDEN,
                spacing=2.0,
                visible=True,
                controls=[
                    ft.Container(
                        bgcolor=ft.Colors('transparent'),
                        border_radius=ft.BorderRadius(
                            top_left=0, top_right=0, bottom_left=0, bottom_right=0),
                        ink=True,
                        ink_color=ft.Colors('red'),
                        margin=ft.Margin(left=0, top=0, right=0, bottom=0),
                        offset=ft.Offset(x=0, y=0),
                        opacity=1.0,
                        padding=ft.Padding(left=8, top=8, right=8, bottom=8),
                        shadow=[],
                        visible=True,
                        content=ft.Text(
                            color=ft.Colors('white'),
                            enable_interactive_selection=True,
                            offset=ft.Offset(x=0, y=0),
                            opacity=1.0,
                            selection_cursor_width=2.0,
                            size=15,
                            value='New year sale',
                            visible=True,
                            weight=ft.FontWeight.NORMAL,
                        ),
                    ),
                    ft.Container(
                        bgcolor=ft.Colors('transparent'),
                        border_radius=ft.BorderRadius(
                            top_left=0, top_right=0, bottom_left=0, bottom_right=0),
                        ink=True,
                        ink_color=ft.Colors('red'),
                        margin=ft.Margin(left=0, top=0, right=0, bottom=0),
                        offset=ft.Offset(x=0, y=0),
                        opacity=1.0,
                        padding=ft.Padding(left=8, top=8, right=8, bottom=8),
                        shadow=[],
                        visible=True,
                        content=ft.Text(
                            color=ft.Colors('white'),
                            enable_interactive_selection=True,
                            offset=ft.Offset(x=0, y=0),
                            opacity=1.0,
                            selection_cursor_width=2.0,
                            size=24.0,
                            value='Change text OFF',
                            visible=True,
                            weight=ft.FontWeight.NORMAL,
                        ),
                    ),
                    ft.Container(
                        bgcolor=ft.Colors('transparent'),
                        ink=True,
                        ink_color=ft.Colors('red'),
                        opacity=1.0,
                        padding=ft.Padding(left=8, top=8, right=8, bottom=8),
                        shadow=[],
                        visible=True,
                        content=ft.Row(
                            opacity=1.0,
                            scroll=ft.ScrollMode.HIDDEN,
                            spacing=10,
                            visible=True,
                            controls=[
                                ft.Container(
                                    bgcolor=ft.Colors('transparent'),
                                    border_radius=ft.BorderRadius(
                                        top_left=12, top_right=12, bottom_left=12, bottom_right=12),
                                    ink=True,
                                    ink_color=ft.Colors('red'),
                                    margin=ft.Margin(
                                        left=0, top=0, right=0, bottom=0),
                                    offset=ft.Offset(x=0, y=0),
                                    opacity=1.0,
                                    padding=ft.Padding(
                                        left=12, top=12, right=12, bottom=12),
                                    shadow=[],
                                    visible=True,
                                    content=ft.Text(
                                        color=ft.Colors('white'),
                                        enable_interactive_selection=True,
                                        offset=ft.Offset(x=0, y=0),
                                        opacity=1.0,
                                        selection_cursor_width=2.0,
                                        size=15,
                                        value='a',
                                        visible=True,
                                        weight=ft.FontWeight.NORMAL,
                                    ),
                                ),
                                ft.Container(
                                    bgcolor=ft.Colors('transparent'),
                                    border_radius=ft.BorderRadius(
                                        top_left=12, top_right=12, bottom_left=12, bottom_right=12),
                                    ink=True,
                                    ink_color=ft.Colors('red'),
                                    margin=ft.Margin(
                                        left=0, top=0, right=0, bottom=0),
                                    offset=ft.Offset(x=0, y=0),
                                    opacity=1.0,
                                    padding=ft.Padding(
                                        left=12, top=12, right=12, bottom=12),
                                    shadow=[],
                                    visible=True,
                                    content=ft.Text(
                                        color=ft.Colors('white'),
                                        enable_interactive_selection=True,
                                        offset=ft.Offset(x=0, y=0),
                                        opacity=1.0,
                                        selection_cursor_width=2.0,
                                        size=15,
                                        value='b',
                                        visible=True,
                                        weight=ft.FontWeight.NORMAL,
                                    ),
                                ),
                                ft.Container(
                                    alignment=ft.Alignment(x=0, y=0),
                                    bgcolor='red',
                                    border_radius=ft.BorderRadius(
                                        top_left=12, top_right=12, bottom_left=12, bottom_right=12),
                                    height=0.01,
                                    ink=True,
                                    ink_color=ft.Colors('red'),
                                    margin=ft.Margin(
                                        left=0, top=0, right=0, bottom=0),
                                    offset=ft.Offset(x=0, y=0),
                                    opacity=1.0,
                                    padding=ft.Padding(
                                        left=0, top=0, right=0, bottom=0),
                                    shadow=[],
                                    visible=True,
                                    width=0.01,
                                    content=ft.Text(
                                        color=ft.Colors('white'),
                                        enable_interactive_selection=True,
                                        offset=ft.Offset(x=0, y=0),
                                        opacity=1.0,
                                        selection_cursor_width=2.0,
                                        size=15,
                                        value='c',
                                        visible=True,
                                        weight=ft.FontWeight.NORMAL,
                                    ),
                                ),
                                ft.Container(
                                    bgcolor=ft.Colors('transparent'),
                                    border_radius=ft.BorderRadius(
                                        top_left=12, top_right=12, bottom_left=12, bottom_right=12),
                                    ink=True,
                                    ink_color=ft.Colors('red'),
                                    margin=ft.Margin(
                                        left=0, top=0, right=0, bottom=0),
                                    offset=ft.Offset(x=0, y=0),
                                    opacity=1.0,
                                    padding=ft.Padding(
                                        left=12, top=12, right=12, bottom=12),
                                    shadow=[],
                                    visible=True,
                                    content=ft.Text(
                                        color=ft.Colors('white'),
                                        enable_interactive_selection=True,
                                        offset=ft.Offset(x=0, y=0),
                                        opacity=1.0,
                                        selection_cursor_width=2.0,
                                        size=15,
                                        value='c',
                                        visible=True,
                                        weight=ft.FontWeight.NORMAL,
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
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
        self.all_instances: list = [fletbox_ui_0(page=self.page,expand=False,),]

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
