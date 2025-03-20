parse_data = """
import flet as ft

# UI Custom widget edit tag name
class UIFletBox(ft.Container):

    def __init__(self, page: object = None) -> None:
        super().__init__()
        self.page = page

        self.expand = True
        self.bgcolor = ft.colors('transparent')
        self.alignment = ft.alignment.top_center
        self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)
        self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)

        # content of current widget
        self.content = remplace_data

"""

stream_widget = """
class fletbox_ui_stream(ft.Container):

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
        self.content = remplace_data
        """

main_stream = """

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
        self.all_instances: remplace_data

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
"""
