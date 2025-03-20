import flet as ft
from flet import Offset, Tab, Alignment


# widget class
class fletbox_ui_0(ft.Container):

    # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    def __init__(
        self,
        page: object = None,
        expand: bool = True,
    ) -> None:
        super().__init__()
        # self.shadow = ft.BoxShadow(spread_radius = 1, blur_radius  = 15, color = ft.colors('black'), offset = ft.Offset(0,0), blur_style = ft.ShadowBlurStyle.OUTER,)
        # self.image = ft.DecorationImage(src='logo.png',fit=ft.ImageFit.COVER,opacity=0.02)
        # self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        # self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)

        self.page = page
        self.bgcolor = ft.colors("transparent")
        self.expand = expand
        # self.alignment = ft.alignment.top_center

        # content of current widget
        self.content = ft.Container(
            bgcolor=ft.Colors("transparent"),
            ink=True,
            ink_color=ft.Colors("red"),
            opacity=1.0,
            padding=ft.Padding(left=8, top=8, right=8, bottom=8),
            shadow=[],
            visible=True,
            content=ft.Container(
                bgcolor=ft.Colors("grey900"),
                border_radius=ft.BorderRadius(
                    top_left=32, top_right=32, bottom_left=32, bottom_right=32
                ),
                height=160,
                image=ft.DecorationImage(
                    src="pizza_get.jpg",
                    src_base64=None,
                    color_filter=None,
                    fit="cover",
                    alignment=None,
                    repeat=None,
                    match_text_direction=None,
                    scale=None,
                    opacity=0.5,
                    filter_quality=None,
                    invert_colors=None,
                    anti_alias=None,
                ),
                opacity=1.0,
                padding=ft.Padding(left=0, top=0, right=0, bottom=0),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color="black",
                    offset=Offset(x=0, y=5),
                    blur_style="normal",
                ),
                visible=True,
                width=340,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.END,
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    opacity=1.0,
                    run_alignment=ft.CrossAxisAlignment.CENTER,
                    run_spacing=8,
                    spacing=8,
                    visible=True,
                    controls=[
                        ft.Container(
                            bgcolor="red,0.8",
                            border_radius=ft.BorderRadius(
                                top_left=0, top_right=32, bottom_left=0, bottom_right=0
                            ),
                            opacity=1.0,
                            padding=ft.Padding(left=24, top=8, right=24, bottom=8),
                            shadow=[],
                            visible=True,
                            content=ft.Text(
                                enable_interactive_selection=True,
                                font_family="Consolas",
                                opacity=1.0,
                                selection_cursor_width=2.0,
                                value="25-30 min",
                                visible=True,
                                weight=ft.FontWeight.BOLD,
                                width=80,
                            ),
                        ),
                    ],
                ),
            ),
        )


class fletbox_ui_1(ft.Container):

    # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    def __init__(
        self,
        page: object = None,
        expand: bool = True,
    ) -> None:
        super().__init__()
        # self.shadow = ft.BoxShadow(spread_radius = 1, blur_radius  = 15, color = ft.colors('black'), offset = ft.Offset(0,0), blur_style = ft.ShadowBlurStyle.OUTER,)
        # self.image = ft.DecorationImage(src='logo.png',fit=ft.ImageFit.COVER,opacity=0.02)
        # self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        # self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)

        self.page = page
        self.bgcolor = ft.colors("transparent")
        self.expand = expand
        # self.alignment = ft.alignment.top_center

        # content of current widget
        self.content = ft.Container(
            bgcolor=ft.Colors("transparent"),
            ink=True,
            ink_color=ft.Colors("red"),
            opacity=1.0,
            padding=ft.Padding(left=8, top=8, right=8, bottom=8),
            shadow=[],
            visible=True,
            content=ft.Container(
                bgcolor=ft.Colors("grey900"),
                border_radius=ft.BorderRadius(
                    top_left=32, top_right=32, bottom_left=32, bottom_right=32
                ),
                height=160,
                image=ft.DecorationImage(
                    src="pizza_get.jpg",
                    src_base64=None,
                    color_filter=None,
                    fit="cover",
                    alignment=None,
                    repeat=None,
                    match_text_direction=None,
                    scale=None,
                    opacity=0.5,
                    filter_quality=None,
                    invert_colors=None,
                    anti_alias=None,
                ),
                opacity=1.0,
                padding=ft.Padding(left=0, top=0, right=0, bottom=0),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color="black",
                    offset=Offset(x=0, y=5),
                    blur_style="normal",
                ),
                visible=True,
                width=340,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                    opacity=1.0,
                    run_alignment=ft.CrossAxisAlignment.CENTER,
                    run_spacing=8,
                    spacing=8,
                    visible=True,
                    controls=[
                        ft.Container(
                            bgcolor="grey900,0.8",
                            expand=True,
                            opacity=1.0,
                            padding=ft.Padding(left=24, top=8, right=24, bottom=8),
                            shadow=[],
                            visible=True,
                            content=ft.Text(
                                enable_interactive_selection=True,
                                font_family="Consolas",
                                opacity=1.0,
                                selection_cursor_width=2.0,
                                size=18,
                                text_align=ft.TextAlign.RIGHT,
                                value="Can you hear the bass boom? I'm ready",
                                visible=True,
                                weight=ft.FontWeight.BOLD,
                                width=100,
                            ),
                        ),
                    ],
                ),
            ),
        )


class fletbox_ui_2(ft.Container):

    # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    def __init__(
        self,
        page: object = None,
        expand: bool = True,
    ) -> None:
        super().__init__()
        # self.shadow = ft.BoxShadow(spread_radius = 1, blur_radius  = 15, color = ft.colors('black'), offset = ft.Offset(0,0), blur_style = ft.ShadowBlurStyle.OUTER,)
        # self.image = ft.DecorationImage(src='logo.png',fit=ft.ImageFit.COVER,opacity=0.02)
        # self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        # self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)

        self.page = page
        self.bgcolor = ft.colors("transparent")
        self.expand = expand
        # self.alignment = ft.alignment.top_center

        # content of current widget
        self.content = ft.Container(
            bgcolor=ft.Colors("transparent"),
            ink=True,
            ink_color=ft.Colors("red"),
            opacity=1.0,
            padding=ft.Padding(left=8, top=8, right=8, bottom=8),
            shadow=[],
            visible=True,
            content=ft.Container(
                bgcolor=ft.Colors("grey900"),
                border_radius=ft.BorderRadius(
                    top_left=32, top_right=32, bottom_left=32, bottom_right=32
                ),
                image=ft.DecorationImage(
                    src="clothes.jpg",
                    src_base64=None,
                    color_filter=None,
                    fit="cover",
                    alignment=None,
                    repeat=None,
                    match_text_direction=None,
                    scale=None,
                    opacity=0.18,
                    filter_quality=None,
                    invert_colors=None,
                    anti_alias=None,
                ),
                opacity=1.0,
                padding=ft.Padding(left=4, top=4, right=4, bottom=4),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color="black",
                    offset=Offset(x=0, y=5),
                    blur_style="normal",
                ),
                visible=True,
                width=340,
                content=ft.Row(
                    opacity=1.0,
                    spacing=10,
                    visible=True,
                    controls=[
                        ft.Image(
                            border_radius=ft.BorderRadius(
                                top_left=32,
                                top_right=32,
                                bottom_left=32,
                                bottom_right=32,
                            ),
                            fit=ft.ImageFit.COVER,
                            height=150,
                            opacity=1.0,
                            src="shoes.jpg",
                            visible=True,
                            width=150,
                        ),
                        ft.Column(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            expand=True,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            opacity=1.0,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            run_spacing=12,
                            spacing=12,
                            visible=True,
                            controls=[
                                ft.Column(
                                    opacity=1.0,
                                    spacing=10,
                                    visible=True,
                                    controls=[
                                        ft.Text(
                                            color=ft.Colors("white"),
                                            enable_interactive_selection=True,
                                            opacity=1.0,
                                            selection_cursor_width=2.0,
                                            size=18,
                                            value="35% OFF",
                                            visible=True,
                                            weight="bold",
                                        ),
                                        ft.Text(
                                            color=ft.Colors("white70"),
                                            enable_interactive_selection=True,
                                            opacity=1.0,
                                            selection_cursor_width=2.0,
                                            size=12,
                                            value="Get Best offer now",
                                            visible=True,
                                        ),
                                    ],
                                ),
                                ft.Container(
                                    alignment=ft.Alignment(x=0, y=0),
                                    bgcolor=ft.Colors("red900"),
                                    border_radius=ft.BorderRadius(
                                        top_left=24,
                                        top_right=24,
                                        bottom_left=24,
                                        bottom_right=24,
                                    ),
                                    expand=True,
                                    ink_color=ft.Colors("yellow"),
                                    margin=ft.Margin(left=0, top=16, right=0, bottom=0),
                                    opacity=1.0,
                                    padding=ft.Padding(
                                        left=12, top=8, right=12, bottom=8
                                    ),
                                    shadow=[],
                                    visible=True,
                                    width=100,
                                    content=ft.Text(
                                        color=ft.Colors("white70"),
                                        enable_interactive_selection=True,
                                        opacity=1.0,
                                        selection_cursor_width=2.0,
                                        size=11,
                                        value="Buy Now ",
                                        visible=True,
                                        weight="bold",
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        )


class fletbox_ui_3(ft.Container):

    # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    def __init__(
        self,
        page: object = None,
        expand: bool = True,
    ) -> None:
        super().__init__()
        # self.shadow = ft.BoxShadow(spread_radius = 1, blur_radius  = 15, color = ft.colors('black'), offset = ft.Offset(0,0), blur_style = ft.ShadowBlurStyle.OUTER,)
        # self.image = ft.DecorationImage(src='logo.png',fit=ft.ImageFit.COVER,opacity=0.02)
        # self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        # self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)

        self.page = page
        self.bgcolor = ft.colors("transparent")
        self.expand = expand
        # self.alignment = ft.alignment.top_center

        # content of current widget
        self.content = ft.Container(
            bgcolor=ft.Colors("transparent"),
            ink=True,
            ink_color=ft.Colors("red"),
            opacity=1.0,
            padding=ft.Padding(left=8, top=8, right=8, bottom=8),
            shadow=[],
            visible=True,
            content=ft.Container(
                bgcolor=ft.Colors("grey900"),
                border_radius=ft.BorderRadius(
                    top_left=32, top_right=32, bottom_left=32, bottom_right=32
                ),
                image=ft.DecorationImage(
                    src="clothes.jpg",
                    src_base64=None,
                    color_filter=None,
                    fit="cover",
                    alignment=None,
                    repeat=None,
                    match_text_direction=None,
                    scale=None,
                    opacity=0.18,
                    filter_quality=None,
                    invert_colors=None,
                    anti_alias=None,
                ),
                opacity=1.0,
                padding=ft.Padding(left=4, top=4, right=4, bottom=4),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color="black",
                    offset=Offset(x=0, y=5),
                    blur_style="normal",
                ),
                visible=True,
                width=340,
                content=ft.Row(
                    opacity=1.0,
                    spacing=10,
                    visible=True,
                    controls=[
                        ft.Image(
                            border_radius=ft.BorderRadius(
                                top_left=32,
                                top_right=32,
                                bottom_left=32,
                                bottom_right=32,
                            ),
                            fit=ft.ImageFit.COVER,
                            height=150,
                            opacity=1.0,
                            src="shoes.jpg",
                            visible=True,
                            width=150,
                        ),
                        ft.Column(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            expand=True,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            opacity=1.0,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            run_spacing=12,
                            spacing=12,
                            visible=True,
                            controls=[
                                ft.Column(
                                    opacity=1.0,
                                    spacing=10,
                                    visible=True,
                                    controls=[
                                        ft.Text(
                                            color=ft.Colors("white"),
                                            enable_interactive_selection=True,
                                            opacity=1.0,
                                            selection_cursor_width=2.0,
                                            size=18,
                                            value="35% OFF",
                                            visible=True,
                                            weight="bold",
                                        ),
                                        ft.Text(
                                            color=ft.Colors("white70"),
                                            enable_interactive_selection=True,
                                            opacity=1.0,
                                            selection_cursor_width=2.0,
                                            size=12,
                                            value="Get Best offer now",
                                            visible=True,
                                        ),
                                    ],
                                ),
                                ft.Container(
                                    alignment=ft.Alignment(x=0, y=0),
                                    bgcolor=ft.Colors("red900"),
                                    border_radius=ft.BorderRadius(
                                        top_left=24,
                                        top_right=24,
                                        bottom_left=24,
                                        bottom_right=24,
                                    ),
                                    expand=True,
                                    ink_color=ft.Colors("yellow"),
                                    margin=ft.Margin(left=0, top=16, right=0, bottom=0),
                                    opacity=1.0,
                                    padding=ft.Padding(
                                        left=12, top=8, right=12, bottom=8
                                    ),
                                    shadow=[],
                                    visible=True,
                                    width=100,
                                    content=ft.Text(
                                        color=ft.Colors("white70"),
                                        enable_interactive_selection=True,
                                        opacity=1.0,
                                        selection_cursor_width=2.0,
                                        size=11,
                                        value="Buy Now ",
                                        visible=True,
                                        weight="bold",
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        )


class fletbox_ui_4(ft.Container):

    # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    def __init__(
        self,
        page: object = None,
        expand: bool = True,
    ) -> None:
        super().__init__()
        # self.shadow = ft.BoxShadow(spread_radius = 1, blur_radius  = 15, color = ft.colors('black'), offset = ft.Offset(0,0), blur_style = ft.ShadowBlurStyle.OUTER,)
        # self.image = ft.DecorationImage(src='logo.png',fit=ft.ImageFit.COVER,opacity=0.02)
        # self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        # self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)

        self.page = page
        self.bgcolor = ft.colors("transparent")
        self.expand = expand
        # self.alignment = ft.alignment.top_center

        # content of current widget
        self.content = ft.Container(
            bgcolor=ft.Colors("transparent"),
            ink=True,
            ink_color=ft.Colors("red"),
            opacity=1.0,
            padding=ft.Padding(left=8, top=8, right=8, bottom=8),
            shadow=[],
            visible=True,
            content=ft.Container(
                bgcolor=ft.Colors("grey900"),
                border_radius=ft.BorderRadius(
                    top_left=32, top_right=32, bottom_left=32, bottom_right=32
                ),
                image=ft.DecorationImage(
                    src="clothes.jpg",
                    src_base64=None,
                    color_filter=None,
                    fit="cover",
                    alignment=None,
                    repeat=None,
                    match_text_direction=None,
                    scale=None,
                    opacity=0.18,
                    filter_quality=None,
                    invert_colors=None,
                    anti_alias=None,
                ),
                opacity=1.0,
                padding=ft.Padding(left=4, top=4, right=4, bottom=4),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color="black",
                    offset=Offset(x=0, y=5),
                    blur_style="normal",
                ),
                visible=True,
                width=340,
                content=ft.Row(
                    opacity=1.0,
                    spacing=10,
                    visible=True,
                    controls=[
                        ft.Image(
                            border_radius=ft.BorderRadius(
                                top_left=32,
                                top_right=32,
                                bottom_left=32,
                                bottom_right=32,
                            ),
                            fit=ft.ImageFit.COVER,
                            height=150,
                            opacity=1.0,
                            src="shoes.jpg",
                            visible=True,
                            width=150,
                        ),
                        ft.Column(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            expand=True,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            opacity=1.0,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            run_spacing=12,
                            spacing=12,
                            visible=True,
                            controls=[
                                ft.Column(
                                    opacity=1.0,
                                    spacing=10,
                                    visible=True,
                                    controls=[
                                        ft.Text(
                                            color=ft.Colors("white"),
                                            enable_interactive_selection=True,
                                            opacity=1.0,
                                            selection_cursor_width=2.0,
                                            size=18,
                                            value="35% OFF",
                                            visible=True,
                                            weight="bold",
                                        ),
                                        ft.Text(
                                            color=ft.Colors("white70"),
                                            enable_interactive_selection=True,
                                            opacity=1.0,
                                            selection_cursor_width=2.0,
                                            size=12,
                                            value="Get Best offer now",
                                            visible=True,
                                        ),
                                    ],
                                ),
                                ft.Container(
                                    alignment=ft.Alignment(x=0, y=0),
                                    bgcolor=ft.Colors("red900"),
                                    border_radius=ft.BorderRadius(
                                        top_left=24,
                                        top_right=24,
                                        bottom_left=24,
                                        bottom_right=24,
                                    ),
                                    expand=True,
                                    ink_color=ft.Colors("yellow"),
                                    margin=ft.Margin(left=0, top=16, right=0, bottom=0),
                                    opacity=1.0,
                                    padding=ft.Padding(
                                        left=12, top=8, right=12, bottom=8
                                    ),
                                    shadow=[],
                                    visible=True,
                                    width=100,
                                    content=ft.Text(
                                        color=ft.Colors("white70"),
                                        enable_interactive_selection=True,
                                        opacity=1.0,
                                        selection_cursor_width=2.0,
                                        size=11,
                                        value="Buy Now ",
                                        visible=True,
                                        weight="bold",
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        )


class fletbox_ui_5(ft.Container):

    # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    def __init__(
        self,
        page: object = None,
        expand: bool = True,
    ) -> None:
        super().__init__()
        # self.shadow = ft.BoxShadow(spread_radius = 1, blur_radius  = 15, color = ft.colors('black'), offset = ft.Offset(0,0), blur_style = ft.ShadowBlurStyle.OUTER,)
        # self.image = ft.DecorationImage(src='logo.png',fit=ft.ImageFit.COVER,opacity=0.02)
        # self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        # self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)

        self.page = page
        self.bgcolor = ft.colors("transparent")
        self.expand = expand
        # self.alignment = ft.alignment.top_center

        # content of current widget
        self.content = ft.Container(
            bgcolor=ft.Colors("transparent"),
            ink=True,
            ink_color=ft.Colors("red"),
            opacity=1.0,
            padding=ft.Padding(left=8, top=8, right=8, bottom=8),
            shadow=[],
            visible=True,
            content=ft.Container(
                bgcolor=ft.Colors("grey900"),
                border_radius=ft.BorderRadius(
                    top_left=32, top_right=32, bottom_left=32, bottom_right=32
                ),
                image=ft.DecorationImage(
                    src="clothes.jpg",
                    src_base64=None,
                    color_filter=None,
                    fit="cover",
                    alignment=None,
                    repeat=None,
                    match_text_direction=None,
                    scale=None,
                    opacity=0.18,
                    filter_quality=None,
                    invert_colors=None,
                    anti_alias=None,
                ),
                opacity=1.0,
                padding=ft.Padding(left=4, top=4, right=4, bottom=4),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color="black",
                    offset=Offset(x=0, y=5),
                    blur_style="normal",
                ),
                visible=True,
                width=340,
                content=ft.Row(
                    opacity=1.0,
                    spacing=10,
                    visible=True,
                    controls=[
                        ft.Image(
                            border_radius=ft.BorderRadius(
                                top_left=32,
                                top_right=32,
                                bottom_left=32,
                                bottom_right=32,
                            ),
                            fit=ft.ImageFit.COVER,
                            height=150,
                            opacity=1.0,
                            src="shoes.jpg",
                            visible=True,
                            width=150,
                        ),
                        ft.Column(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            expand=True,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            opacity=1.0,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            run_spacing=12,
                            spacing=12,
                            visible=True,
                            controls=[
                                ft.Column(
                                    opacity=1.0,
                                    spacing=10,
                                    visible=True,
                                    controls=[
                                        ft.Text(
                                            color=ft.Colors("white"),
                                            enable_interactive_selection=True,
                                            opacity=1.0,
                                            selection_cursor_width=2.0,
                                            size=18,
                                            value="35% OFF",
                                            visible=True,
                                            weight="bold",
                                        ),
                                        ft.Text(
                                            color=ft.Colors("white70"),
                                            enable_interactive_selection=True,
                                            opacity=1.0,
                                            selection_cursor_width=2.0,
                                            size=12,
                                            value="Get Best offer now",
                                            visible=True,
                                        ),
                                    ],
                                ),
                                ft.Container(
                                    alignment=ft.Alignment(x=0, y=0),
                                    bgcolor=ft.Colors("red900"),
                                    border_radius=ft.BorderRadius(
                                        top_left=24,
                                        top_right=24,
                                        bottom_left=24,
                                        bottom_right=24,
                                    ),
                                    expand=True,
                                    ink_color=ft.Colors("yellow"),
                                    margin=ft.Margin(left=0, top=16, right=0, bottom=0),
                                    opacity=1.0,
                                    padding=ft.Padding(
                                        left=12, top=8, right=12, bottom=8
                                    ),
                                    shadow=[],
                                    visible=True,
                                    width=100,
                                    content=ft.Text(
                                        color=ft.Colors("white70"),
                                        enable_interactive_selection=True,
                                        opacity=1.0,
                                        selection_cursor_width=2.0,
                                        size=11,
                                        value="Buy Now ",
                                        visible=True,
                                        weight="bold",
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        )


class fletbox_ui_6(ft.Container):

    # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    def __init__(
        self,
        page: object = None,
        expand: bool = True,
    ) -> None:
        super().__init__()
        # self.shadow = ft.BoxShadow(spread_radius = 1, blur_radius  = 15, color = ft.colors('black'), offset = ft.Offset(0,0), blur_style = ft.ShadowBlurStyle.OUTER,)
        # self.image = ft.DecorationImage(src='logo.png',fit=ft.ImageFit.COVER,opacity=0.02)
        # self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        # self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)

        self.page = page
        self.bgcolor = ft.colors("transparent")
        self.expand = expand
        # self.alignment = ft.alignment.top_center

        # content of current widget
        self.content = (
            ft.Container(
                bgcolor=ft.Colors("grey900"),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors("black"),
                    offset=ft.Offset(0, 5),
                ),
                border_radius=ft.border_radius.all(32),
                padding=ft.padding.only(left=0, top=0, right=0, bottom=18),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    run_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                            # expand=True,
                            border_radius=ft.border_radius.all(32),
                            width=200,
                            height=200,
                            src="hotel.jpg",
                            fit="cover",
                            opacity=0.2,
                        ),
                        ft.Column(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            expand=True,
                            spacing=0,
                            run_spacing=0,
                            controls=[
                                ft.Text(
                                    expand=True,
                                    value="Hello World",
                                    text_align=ft.TextAlign.CENTER,
                                    weight=ft.FontWeight.BOLD,
                                    font_family="Consolas",
                                ),
                                ft.Container(
                                    width=100,
                                    padding=ft.padding.only(
                                        left=0, top=0, right=0, bottom=0
                                    ),
                                    border_radius=ft.border_radius.all(24),
                                    expand=True,
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        run_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=6,
                                        run_spacing=8,
                                        controls=[
                                            ft.Icon(name="star_rounded", size=12),
                                            ft.Icon(name="star_rounded", size=12),
                                            ft.Icon(name="star_rounded", size=12),
                                            ft.Icon(name="star_rounded", size=12),
                                            ft.Icon(name="star_rounded", size=12),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        )  # <


class fletbox_ui(ft.Container):

    # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
    def __init__(self, page: object = None) -> None:
        super().__init__()
        # self.shadow = ft.BoxShadow(spread_radius=1, blur_radius=15, color=ft.colors('black'), offset=ft.Offset(0,0), blur_style=ft.ShadowBlurStyle.OUTER,)
        # self.image = ft.DecorationImage(src='logo.png',fit=ft.ImageFit.COVER,opacity=0.02)
        # self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        # self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)

        self.page = page
        self.bgcolor = ft.colors("transparent")
        self.expand = True
        self.alignment = ft.alignment.top_center

        # all widgets
        self.all_instances: list = [
            fletbox_ui_0(
                page=self.page,
                expand=False,
            ),
            fletbox_ui_1(
                page=self.page,
                expand=False,
            ),
            fletbox_ui_2(
                page=self.page,
                expand=False,
            ),
            fletbox_ui_3(
                page=self.page,
                expand=False,
            ),
            fletbox_ui_4(
                page=self.page,
                expand=False,
            ),
            fletbox_ui_5(
                page=self.page,
                expand=False,
            ),
            fletbox_ui_6(
                page=self.page,
                expand=False,
            ),
        ]

        # content of current widget
        self.content = ft.Column(
            # tooltip = 'Column',
            # tight = True,
            # wrap = True,
            auto_scroll=True,
            # height = 150,
            # width = 150,
            # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
            # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
            scroll=ft.ScrollMode.HIDDEN,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            spacing=0,
            run_spacing=0,
            controls=self.all_instances,
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
