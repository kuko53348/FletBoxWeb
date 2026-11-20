import flet as ft
import ast
import os

from utils_safe_print import safe_print

image = "image97.jpeg"
long_text = "Flet is a framework that allows building web, desktop and mobile applications in Python without prior experience in frontend development.\n\nYou can build a UI for your program with Flet controls which are based on Flutter by Google. Flet goes beyond merely wrapping Flutter widgets. It adds its own touch by combining smaller widgets, simplifying complexities, implementing UI best practices, and applying sensible defaults. This ensures that your applications look stylish and polished without requiring additional design efforts on your part."
medium_text = "Flet is a framework that allows building web, desktop and mobile applications in Python without prior experience in frontend development."


column_swap = ft.Column(
    width=420,
    height=180,
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    # spacing=16,
    run_spacing=0,
    spacing=12,
    controls=[
        ft.Container(
            # height=80,
            padding=ft.Padding(left=8, top=8, right=8, bottom=8),
            border_radius=ft.border_radius.all(24),
            expand=True,
            bgcolor=ft.Colors("grey900"),
            content=ft.Row(
                controls=[
                    ft.TextField(
                        expand=True,
                        bgcolor="grey900",
                        label="You will Get",
                        # icon=ft.Icons.ACCOUNT_CIRCLE_ROUNDED,
                        hint_text="0",
                        border_width=0,
                        border_radius=ft.border_radius.all(18),
                    ),
                    ft.Container(
                        border_radius=ft.border_radius.all(18),
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.8,
                            color=ft.Colors("blue"),
                        ),
                        padding=ft.padding.all(8),
                        content=ft.Icon(ft.Icons.SEARCH),
                    ),
                ],
            ),
        ),
        ft.Container(
            # height=80,
            padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
            border_radius=ft.border_radius.all(24),
            expand=True,
            bgcolor=ft.Colors("grey900"),
            content=ft.Row(
                controls=[
                    ft.TextField(
                        expand=True,
                        bgcolor="grey900",
                        label="You will Pay",
                        # icon=ft.Icons.ACCOUNT_CIRCLE_ROUNDED,
                        hint_text="0",
                        border_width=0,
                        border_radius=ft.border_radius.all(18),
                    ),
                    ft.Container(
                        border_radius=ft.border_radius.all(18),
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.8,
                            color=ft.Colors("blue"),
                        ),
                        padding=ft.padding.all(8),
                        content=ft.Icon(ft.Icons.SEARCH),
                    ),
                ],
            ),
        ),
    ],
)
widget_dict = {
    "Long text": ft.Container(
        content=ft.Column(
            controls=[
                # Banner Title
                ft.Text(
                    value="What is Flet?",
                    size=16,
                    weight="bold",
                    color=ft.Colors("white"),
                ),
                # Banner Description
                ft.Text(
                    value=long_text,
                    size=11,
                    color=ft.Colors("white70"),
                ),
            ],
            spacing=16,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
    ),  # <
    "H Dual text": ft.Container(
        content=ft.Row(
            controls=[
                # Banner Title
                ft.Container(
                    expand=True,
                    content=ft.Text(
                        "Cannes Film FestiHal",
                        size=14,
                        weight="bold",
                        color=ft.Colors("white"),
                    ),
                ),
                # Banner Description
                ft.Text("May 14-25, 2024", size=11, color=ft.Colors("white70")),
            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    ),  # <
    "Header text": ft.Container(
        content=ft.Column(
            controls=[
                # Banner Title
                ft.Text(
                    value="Good day healthy body",
                    size=32,
                    weight=ft.FontWeight.W_900,
                    color=ft.Colors("white"),
                ),
                # Banner Description
                ft.Text(
                    value="with this app you can try different types of activities and choose what the most enjoyable for you",
                    size=11,
                    color=ft.Colors("grey600"),
                ),
            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
    ),  # <
    "Dual text": ft.Container(
        content=ft.Column(
            controls=[
                # Banner Title
                ft.Text(
                    "Cannes Film Festival",
                    size=14,
                    weight="bold",
                    color=ft.Colors("white"),
                ),
                # Banner Description
                ft.Text("May 14-25, 2024", size=11, color=ft.Colors("white70")),
            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
    ),  # <
    "H Triple text": ft.Container(
        content=ft.Row(
            controls=[
                ft.Column(
                    expand=True,
                    controls=[
                        # Banner Title
                        ft.Text(
                            value="Cannes Film Festival",
                            size=13,
                            weight="bold",
                            color=ft.Colors("white"),
                        ),
                        # Banner Description
                        ft.Text(
                            value="Date: May 14-25, 2024",
                            size=12,
                            color=ft.Colors("white70"),
                        ),
                    ],
                    spacing=2,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                ),
                ft.Text("New york ", size=11, color=ft.Colors("white70")),
            ],
            spacing=2,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    ),  # <
    "Triple text": ft.Container(
        content=ft.Column(
            controls=[
                # Banner Title
                ft.Text(
                    value="Cannes Film Festival",
                    size=13,
                    weight="bold",
                    color=ft.Colors("white"),
                ),
                # Banner Description
                ft.Text(
                    value="Date: May 14-25, 2024",
                    size=12,
                    color=ft.Colors("white70"),
                ),
                ft.Text(value="New york ", size=11, color=ft.Colors("white70")),
            ],
            spacing=2,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
    ),  # <
    "Card text btn": ft.Container(
        width=320,
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        border=ft.border.only(
            left=ft.border.BorderSide(
                8,
                ft.Colors.with_opacity(opacity=0.6, color=ft.Colors("yellow900")),
            ),
            top=None,
            right=None,
            bottom=None,
        ),
        border_radius=ft.border_radius.all(12),
        padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
        content=ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        # Banner Title
                        ft.Row(
                            expand=True,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    value="Cannes Film Festival",
                                    size=14,
                                    weight="bold",
                                    color=ft.Colors("white"),
                                ),
                                ft.Text(
                                    value="$68",
                                    size=22,
                                    weight="bold",
                                    color=ft.Colors.with_opacity(
                                        opacity=0.6, color=ft.Colors("yellow900")
                                    ),
                                ),
                            ],
                        ),
                        # Banner Description
                        ft.Text(
                            value="May 14-25, 2024",
                            size=11,
                            color=ft.Colors("white70"),
                        ),
                    ],
                    spacing=0,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    run_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=2,
                            run_spacing=2,
                            controls=[
                                ft.Icon(
                                    ft.Icons.STAR_ROUNDED,
                                    size=12,
                                    color=ft.Colors.with_opacity(
                                        opacity=0.6, color=ft.Colors("yellow900")
                                    ),
                                ),
                                ft.Text(
                                    text_align=ft.TextAlign.LEFT,
                                    weight=ft.FontWeight.BOLD,
                                    font_family="Consolas",
                                    size=12,
                                    value="4.0",
                                ),
                            ],
                        ),
                        ft.Container(
                            padding=ft.padding.only(
                                left=12, right=12, bottom=8, top=8
                            ),
                            border_radius=ft.border_radius.only(
                                top_left=8,
                                top_right=8,
                                bottom_left=8,
                                bottom_right=8,
                            ),
                            alignment=ft.alignment.center,
                            ink_color=ft.Colors("yellow"),
                            bgcolor=ft.Colors.with_opacity(
                                opacity=0.6, color=ft.Colors("yellow900")
                            ),
                            content=ft.Text(
                                # expand=True,
                                value="Sport shoes",
                                text_align=ft.TextAlign.CENTER,
                                weight=ft.FontWeight.BOLD,
                                font_family="Consolas",
                                color=ft.Colors.with_opacity(
                                    opacity=0.6, color=ft.Colors("white")
                                ),
                            ),
                        ),
                    ],
                ),
            ],
        ),
    ),  # <
    "Card text": ft.Container(
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        border=ft.border.only(
            left=ft.border.BorderSide(8, "green"),
            top=None,
            right=None,
            bottom=None,
        ),
        border_radius=ft.border_radius.all(12),
        padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
        content=ft.Column(
            controls=[
                # Banner Title
                ft.Text(
                    "Cannes Film Festival",
                    size=14,
                    weight="bold",
                    color=ft.Colors("white"),
                ),
                # Banner Description
                ft.Text(
                    "May 14-25, 2024",
                    size=11,
                    color=ft.Colors("white70"),
                ),
            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
    ),  # <
    "Volumen": ft.Container(
        # expand=True,
        padding=ft.padding.only(left=0, top=0, right=8, bottom=0),
        # border_radius=ft.border_radius.all(32),
        width=320,
        # bgcolor=ft.Colors("grey900"),
        # shadow=ft.BoxShadow(
        #     spread_radius=1,
        #     blur_radius=15,
        #     color=ft.Colors("black"),
        #     offset=ft.Offset(0, 5),
        # ),
        # image=ft.DecorationImage(
        #     src="clothes.jpg",
        #     fit="cover",
        #     opacity=0.18,
        # ),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            spacing=0,
            run_spacing=0,
            controls=[
                ft.Container(
                    padding=ft.padding.only(left=24, top=0, right=0, bottom=0),
                    content=ft.Text(
                        # expand=True,
                        # bgcolor="red",
                        value="Volumen",
                        text_align=ft.TextAlign.START,
                        # weight=ft.FontWeight.BOLD,
                        font_family="Consolas",
                    ),
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    run_alignment=ft.CrossAxisAlignment.CENTER,
                    # expand=True,
                    spacing=0,
                    run_spacing=0,
                    controls=[
                        ft.Slider(expand=True, min=0, max=100, value=24),
                        ft.Icon("volume_up"),
                    ],
                ),
            ],
        ),
    ),  # <
    "Add remove": ft.Container(
        bgcolor=ft.Colors("transparent"),
        ink=True,
        ink_color=ft.Colors("red"),
        opacity=1.0,
        padding=ft.Padding(left=0, top=0, right=0, bottom=0),
        shadow=[],
        visible=True,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            # expand=True,
            spacing=8,
            run_spacing=8,
            controls=[
                ft.Container(
                    bgcolor=ft.Colors("grey900"),
                    border_radius=ft.border_radius.only(
                        top_left=32, top_right=32, bottom_left=32, bottom_right=32
                    ),
                    alignment=ft.alignment.center,
                    ink=True,
                    ink_color=ft.Colors("yellow"),
                    content=ft.Icon("remove_rounded"),
                    on_click=lambda arguments: safe_print("hello"),
                ),
                ft.Text(
                    value="0",
                    size=16,
                ),
                ft.Container(
                    bgcolor=ft.Colors("grey900"),
                    border_radius=ft.border_radius.only(
                        top_left=32, top_right=32, bottom_left=32, bottom_right=32
                    ),
                    alignment=ft.alignment.center,
                    ink=True,
                    ink_color=ft.Colors("yellow"),
                    content=ft.Icon("add_rounded"),
                    on_click=lambda arguments: safe_print("hello"),
                ),
            ],
        ),
    ),  # <
    "Stars": ft.Container(
        width=100,
        padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
        border_radius=ft.border_radius.all(24),
        expand=True,
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=6,
            run_spacing=8,
            controls=[
                ft.Icon("star_rounded", size=12),
                ft.Icon("star_rounded", size=12),
                ft.Icon("star_rounded", size=12),
                ft.Icon("star_rounded", size=12),
                ft.Icon("star_rounded", size=12),
            ],
        ),
    ),  # <
    "Best Textfield": ft.Container(
        padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
        border_radius=ft.border_radius.all(24),
        expand=True,
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        content=ft.Row(
            controls=[
                ft.TextField(
                    expand=True,
                    bgcolor="black12",
                    label="Search",
                    hint_text="Fill correct data",
                    border_width=0,
                    border_radius=ft.border_radius.all(18),
                    border_color=ft.Colors("transparent"),
                ),
                ft.Container(
                    border_radius=ft.border_radius.all(18),
                    bgcolor=ft.Colors.with_opacity(
                        opacity=0.8,
                        color=ft.Colors("blue"),
                    ),
                    padding=ft.padding.all(8),
                    content=Padding.all,
                ),
            ],
        ),
    ),  # <
    "Banner temp": ft.Container(
        # height=80,
        padding=ft.padding.only(left=12, top=16, right=12, bottom=16),
        border_radius=ft.border_radius.all(24),
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
            run_spacing=12,
            controls=[
                ft.Icon("ac_unit_rounded"),
                ft.Text(value="Room", weight="bold", size=10),
            ],
        ),
    ),  # <
    "Banner date": ft.Container(
        # height=80,
        padding=ft.padding.only(left=12, top=18, right=12, bottom=18),
        border_radius=ft.border_radius.all(18),
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        content=ft.Column(
            width=95,
            controls=[
                # Banner Title
                ft.Text(
                    "21",
                    size=50,
                    weight="bold",
                    color=ft.Colors("white"),
                ),
                # DIVIDER
                ft.Divider(
                    height=1,
                    color=ft.Colors.with_opacity(
                        opacity=0.1,
                        color=ft.Colors("white"),
                    ),
                    thickness=1,
                ),
                # Banner Description
                ft.Text(
                    "Film Festival",
                    size=11,
                    weight="bold",
                    color=ft.Colors("white"),
                ),
            ],
            spacing=12,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    ),  # <
    "Banner cloud": ft.Container(
        # height=80,
        padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
        border_radius=ft.border_radius.all(12),
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        content=ft.Row(
            controls=[
                # Banner Title
                ft.Container(
                    expand=True,
                    content=ft.Text(
                        value="Saturday Sep 19 New york",
                        size=13,
                        weight="bold",
                        color=ft.Colors("white"),
                        width=100,
                    ),
                ),
                # DIVIDER
                ft.Container(
                    border_radius=ft.border_radius.only(
                        top_left=8,
                        top_right=8,
                        bottom_left=8,
                        bottom_right=8,
                    ),
                    padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
                    height=50,
                    width=0.5,
                    bgcolor=ft.Colors.with_opacity(
                        opacity=0.2,
                        color=ft.Colors("white"),
                    ),
                ),
                # Banner Description
                ft.Text(
                    value="25",
                    size=34,
                    color=ft.Colors("white70"),
                ),
                ft.Column(
                    spacing=0,
                    run_spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Icon("cloud_rounded"),
                        ft.Text(
                            value="Cloud",
                            weight="bold",
                        ),
                    ],
                ),
            ],
            spacing=12,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    ),  # <
    "Buttom buy": ft.Container(
        width=320,
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        border_radius=ft.border_radius.only(
            top_left=18, top_right=18, bottom_left=18, bottom_right=18
        ),
        padding=ft.padding.only(left=12, top=12, right=12, bottom=12),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            # expand=True,
            spacing=8,
            run_spacing=8,
            controls=[
                ft.Container(
                    # attrib
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                        run_spacing=0,
                        controls=[
                            ft.Text(
                                value="Total",
                                text_align=ft.TextAlign.LEFT,
                                weight=ft.FontWeight.BOLD,
                                size=12,
                                font_family="Consolas",
                            ),
                            ft.Text(
                                size=20,
                                value="$ 45.00",
                                text_align=ft.TextAlign.LEFT,
                                weight=ft.FontWeight.BOLD,
                                font_family="Consolas",
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    padding=ft.padding.only(left=48, right=48, bottom=16, top=16),
                    border_radius=ft.border_radius.only(
                        top_left=18, top_right=18, bottom_left=18, bottom_right=18
                    ),
                    alignment=ft.alignment.center,
                    ink_color=ft.Colors("yellow"),
                    bgcolor=ft.Colors.with_opacity(
                        opacity=0.5, color=ft.Colors("yellow600")
                    ),
                    content=ft.Text(
                        value="Buy Ticket",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",
                    ),
                ),
            ],
        ),
    ),  # <
    "Buttom upload": ft.Container(
        expand=True,
        padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
        border_radius=ft.border_radius.all(12),
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        content=ft.Row(
            controls=[
                ft.Icon("add_a_photo_rounded"),
                ft.Text(
                    "Upload Picture",
                    size=14,
                    color=ft.Colors("grey"),
                    weight="bold",
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    ),  # <
    "Buttom left": ft.Container(
        expand=True,
        padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
        border_radius=ft.border_radius.all(12),
        width=220,
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        content=ft.Row(
            controls=[
                ft.Icon("navigate_next_rounded"),
                ft.Text(
                    value="Get Started",
                    size=14,
                    color=ft.Colors("grey"),
                    weight="bold",
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    ),  # <
    "Buttom right": ft.Container(
        expand=True,
        padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
        width=220,
        border_radius=ft.border_radius.all(12),
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        content=ft.Row(
            controls=[
                ft.Text(
                    value="Get Started",
                    size=14,
                    color=ft.Colors("grey"),
                    weight="bold",
                ),
                ft.Icon("navigate_next_rounded"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    ),  # <
    "Buttom double": ft.Container(
        # expand=True,
        padding=ft.padding.only(left=4, top=4, right=14, bottom=4),
        border_radius=ft.border_radius.all(32),
        width=220,
        # height=80,
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        content=ft.Row(
            expand=True,
            spacing=8,
            run_spacing=8,
            controls=[
                ft.Container(
                    padding=ft.padding.only(left=8, right=8, bottom=8, top=8),
                    border_radius=ft.border_radius.only(
                        top_left=32, top_right=32, bottom_left=32, bottom_right=32
                    ),
                    alignment=ft.alignment.center,
                    ink_color=ft.Colors("yellow"),
                    bgcolor=ft.Colors("white12"),
                    content=ft.Icon("navigate_next_rounded"),
                ),
                ft.Text(
                    "Get Started",
                    size=14,
                    color=ft.Colors("grey"),
                    weight="bold",
                ),
                ft.Icon("double_arrow_rounded"),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    ),  # <
    "Dapps app": ft.Container(
        padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
        border_radius=ft.border_radius.all(32),
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        content=ft.Column(
            controls=[
                ft.Stack(
                    controls=[
                        column_swap,
                        ft.Container(
                            border_radius=ft.border_radius.all(12),
                            bgcolor="black54",
                            left=column_swap.width / 2.3,
                            right=column_swap.width / 2.3,
                            top=column_swap.height / 2.4,
                            bottom=column_swap.height / 2.4,
                            content=ft.Icon("swap_vertical_circle_rounded"),
                        ),
                    ],
                ),
                ft.Container(
                    # height=80,
                    width=420,
                    padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
                    border_radius=ft.border_radius.all(24),
                    expand=True,
                    bgcolor=ft.Colors("grey900"),
                    content=ft.Dropdown(
                        autofocus=True,
                        hint_text="1 USDT = ???? ",
                        border_width=0,
                        options=[
                            ft.dropdown.Option("1 UST == 0.00064 ETH"),
                            ft.dropdown.Option("1 UST == 0.000000064 BTC"),
                            ft.dropdown.Option("1 UST == 1.5 TRX"),
                            ft.dropdown.Option("1 UST == 2.2 POL"),
                        ],
                    ),
                ),
                ft.Container(
                    width=420,
                    expand=True,
                    padding=ft.padding.only(left=12, top=12, right=12, bottom=12),
                    border_radius=ft.border_radius.all(24),
                    bgcolor=ft.Colors("blue900"),
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "Connect wallet",
                                size=14,
                                color=ft.Colors("grey"),
                                weight="bold",
                            ),
                            ft.Icon("navigate_next_rounded"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
            ]
        ),
    ),  # <
    "Dapps H bar": ft.Container(
        padding=ft.padding.only(left=0, top=8, right=0, bottom=8),
        border_radius=ft.border_radius.all(12),
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        content=ft.Row(
            height=32,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            run_spacing=0,
            spacing=12,
            controls=[
                ft.Container(
                    ink=True,
                    content=ft.Column(
                        run_spacing=0,
                        spacing=0,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon("account_balance_wallet", color="cyan"),
                            ft.Text(
                                value="wallet",
                                size=8,
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    ink=True,
                    content=ft.Column(
                        run_spacing=0,
                        spacing=0,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon("bar_chart_rounded", color="cyan"),
                            ft.Text(
                                value="market",
                                size=8,
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    ink=True,
                    content=ft.Column(
                        run_spacing=0,
                        spacing=0,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon("six_ft_apart_rounded", color="cyan"),
                            ft.Text(
                                value="transact",
                                size=8,
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    ink=True,
                    content=ft.Column(
                        run_spacing=0,
                        spacing=0,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon("flip_camera_android_rounded", color="cyan"),
                            ft.Text(
                                value="DApps",
                                size=8,
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    ink=True,
                    content=ft.Column(
                        run_spacing=0,
                        spacing=0,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon("currency_bitcoin_rounded", color="cyan"),
                            ft.Text(
                                value="Yield",
                                size=8,
                            ),
                        ],
                    ),
                ),
            ],
        ),
    ),  # <
    "Dapps V bar": ft.Container(
        padding=ft.padding.only(left=8, top=18, right=8, bottom=16),
        border_radius=ft.border_radius.all(12),
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        content=ft.Column(
            width=32,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            run_spacing=0,
            spacing=12,
            controls=[
                ft.Container(
                    ink=True,
                    content=ft.Column(
                        run_spacing=0,
                        spacing=0,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon("account_balance_wallet", color="cyan"),
                            ft.Text(
                                value="wallet",
                                size=8,
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    ink=True,
                    content=ft.Column(
                        run_spacing=0,
                        spacing=0,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon("bar_chart_rounded", color="cyan"),
                            ft.Text(
                                value="market",
                                size=8,
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    ink=True,
                    content=ft.Column(
                        run_spacing=0,
                        spacing=0,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon("six_ft_apart_rounded", color="cyan"),
                            ft.Text(
                                value="transact",
                                size=8,
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    ink=True,
                    content=ft.Column(
                        run_spacing=0,
                        spacing=0,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon("flip_camera_android_rounded", color="cyan"),
                            ft.Text(
                                value="DApps",
                                size=8,
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    ink=True,
                    content=ft.Column(
                        run_spacing=0,
                        spacing=0,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon("currency_bitcoin_rounded", color="cyan"),
                            ft.Text(
                                value="Yield",
                                size=8,
                            ),
                        ],
                    ),
                ),
            ],
        ),
    ),  # <
    "Card temp": ft.Container(
        padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
        width=160,
        border_radius=ft.border_radius.all(12),
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        height=200,
        image=ft.DecorationImage(
            src="whether.jpg",
            fit="cover",
            opacity=0.1,
        ),
        content=ft.Column(
            spacing=4,
            controls=[
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text(
                                    value="Humidler",
                                    size=24,
                                    weight="bold",
                                ),
                                ft.Icon("water_drop_rounded"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        ft.Text(
                            value="Humidler",
                            size=10,
                        ),
                        ft.Text(value="Air", size=11),
                    ]
                ),
                ft.Column(
                    controls=[
                        ft.Divider(),
                        ft.Row(
                            controls=[
                                ft.Text(value="On"),
                                ft.Switch(value=False, active_track_color="yellow"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    ),  # <
    "Card travel": ft.Container(
        # height=80,
        padding=ft.padding.only(left=16, top=16, right=16, bottom=16),
        border_radius=ft.border_radius.all(24),
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
            run_spacing=12,
            controls=[
                ft.Row(
                    controls=[
                        ft.TextField(
                            bgcolor=ft.Colors.with_opacity(
                                opacity=0.01,
                                color=ft.Colors("white"),
                            ),
                            # icon=ft.Icons.ACCOUNT_CIRCLE_ROUNDED,
                            hint_text="Ubication",
                            expand=True,
                            border_width=0,
                            border_radius=ft.border_radius.all(18),
                        ),
                        ft.Container(
                            border_radius=ft.border_radius.all(18),
                            border=ft.border.all(
                                width=1,
                                color=ft.Colors.with_opacity(
                                    opacity=0.05,
                                    color=ft.Colors("white"),
                                ),
                            ),
                            padding=ft.padding.all(8),
                            content=ft.Icon("navigate_next_rounded"),
                        ),
                    ],
                ),
                ft.RadioGroup(
                    value="RadioGroup",
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True,
                        spacing=8,
                        run_spacing=8,
                        controls=[
                            ft.Radio(
                                value="Cuba",
                                label="Cuba",
                                active_color="blue",
                                fill_color="blue700",
                            ),
                            ft.Radio(
                                value="Spain",
                                label="Spain",
                                active_color="blue",
                                fill_color="blue700",
                            ),
                            ft.Radio(
                                value="Germany",
                                label="Germany",
                                active_color="blue",
                                fill_color="blue700",
                            ),
                            ft.Radio(
                                value="Japan",
                                label="Japan",
                                active_color="blue",
                                fill_color="blue700",
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    expand=True,
                    padding=ft.padding.only(left=14, top=14, right=14, bottom=14),
                    border_radius=ft.border_radius.all(18),
                    # width=220,
                    bgcolor=ft.Colors.with_opacity(
                        opacity=0.4,
                        color=ft.Colors("blue900"),
                    ),
                    content=ft.Row(
                        controls=[
                            ft.Icon("navigate_next_rounded"),
                            ft.Text(
                                "Lets Go",
                                size=14,
                                color=ft.Colors("white"),
                                weight="bold",
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
            ],
        ),
    ),  # <
    "Regis formulary": ft.Container(
        padding=ft.padding.only(left=8, top=16, right=8, bottom=16),
        border_radius=ft.border_radius.all(24),
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=6,
            run_spacing=8,
            controls=[
                ft.Text(value="Verify your password", weight="bold", size=16),
                ft.Text(
                    width=240,
                    value="Flet is a framework that allows building web, desktop and mobile",
                    size=12,
                    color="white24",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(
                    padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
                    border_radius=ft.border_radius.all(24),
                    expand=True,
                    content=ft.TextField(
                        expand=True,
                        bgcolor="black12",
                        label="Username",
                        hint_text="Fill correct data",
                        border_width=0,
                        border_radius=ft.border_radius.all(18),
                    ),
                ),
                ft.Container(
                    padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
                    border_radius=ft.border_radius.all(24),
                    expand=True,
                    content=ft.TextField(
                        expand=True,
                        bgcolor="black12",
                        label="Email",
                        hint_text="Fill correct data",
                        border_width=0,
                        border_radius=ft.border_radius.all(18),
                    ),
                ),
                ft.Container(
                    padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
                    border_radius=ft.border_radius.all(24),
                    expand=True,
                    content=ft.TextField(
                        expand=True,
                        bgcolor="black12",
                        label="Password",
                        hint_text="Fill correct data",
                        password=True,
                        border_width=0,
                        border_radius=ft.border_radius.all(18),
                    ),
                ),
                ft.Container(
                    # height=80,
                    padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
                    border_radius=ft.border_radius.all(24),
                    expand=True,
                    content=ft.TextField(
                        expand=True,
                        bgcolor="black12",
                        label="Repeat password",
                        hint_text="Fill correct data",
                        password=True,
                        border_width=0,
                        border_radius=ft.border_radius.all(18),
                    ),
                ),
                ft.Text(value="Read fallow Roules", weight="bold", size=16),
                ft.Container(
                    padding=ft.padding.only(left=4, top=4, right=4, bottom=12),
                    content=ft.Row(
                        controls=[
                            ft.RadioGroup(
                                value="RadioGroup",
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    run_alignment=ft.CrossAxisAlignment.CENTER,
                                    expand=True,
                                    spacing=8,
                                    run_spacing=8,
                                    controls=[
                                        ft.Radio(
                                            value="Flet is a framework that allows building web, desktop and mobile",
                                        ),
                                    ],
                                ),
                            ),
                            ft.Text(
                                expand=True,
                                value="Flet is a framework that allows building web, desktop and mobile",
                                size=12,
                                color="white24",
                                text_align=ft.TextAlign.LEFT,
                            ),
                        ],
                    ),
                ),
                ft.Column(
                    spacing=8,
                    run_spacing=12,
                    controls=[
                        ft.Container(
                            expand=True,
                            padding=ft.padding.only(
                                left=12, top=12, right=12, bottom=12
                            ),
                            border_radius=ft.border_radius.all(18),
                            bgcolor=ft.Colors("white"),
                            content=ft.Row(
                                controls=[
                                    ft.Text(
                                        "Submit",
                                        size=14,
                                        color=ft.Colors("grey900"),
                                        weight="bold",
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ),
                        ft.Container(
                            expand=True,
                            padding=ft.padding.only(
                                left=12, top=12, right=12, bottom=12
                            ),
                            border_radius=ft.border_radius.all(18),
                            bgcolor=ft.Colors("red"),
                            content=ft.Row(
                                controls=[
                                    ft.Text(
                                        "Cancel",
                                        size=14,
                                        color=ft.Colors("white"),
                                        weight="bold",
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ),
                    ],
                ),
            ],
        ),
    ),  # <
    "Regis verify": ft.Container(
        padding=ft.padding.only(left=12, top=16, right=12, bottom=16),
        border_radius=ft.border_radius.all(24),
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
            run_spacing=12,
            controls=[
                ft.Text(value="Verify your password", weight="bold", size=18),
                ft.Text(
                    width=240,
                    value="Flet is a framework that allows building web, desktop and mobile",
                    size=12,
                    color="white24",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(
                    padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
                    border_radius=ft.border_radius.all(24),
                    expand=True,
                    content=ft.TextField(
                        expand=True,
                        bgcolor="black12",
                        label="Password",
                        hint_text="Fill correct data",
                        password=True,
                        border_width=0,
                        border_radius=ft.border_radius.all(18),
                    ),
                ),
                ft.Column(
                    controls=[
                        ft.Container(
                            expand=True,
                            padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
                            border_radius=ft.border_radius.all(16),
                            bgcolor=ft.Colors("white"),
                            content=ft.Row(
                                controls=[
                                    ft.Text(
                                        "Continue",
                                        size=14,
                                        color=ft.Colors("grey900"),
                                        weight="bold",
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ),
                        ft.Container(
                            expand=True,
                            padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
                            border_radius=ft.border_radius.all(16),
                            bgcolor=ft.Colors("red"),
                            content=ft.Row(
                                controls=[
                                    ft.Text(
                                        "Cancel",
                                        size=14,
                                        color=ft.Colors("white"),
                                        weight="bold",
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ),
                    ]
                ),
            ],
        ),
    ),  # <
    "Regis pin": ft.Container(
        padding=ft.padding.only(left=8, top=18, right=8, bottom=16),
        border_radius=ft.border_radius.all(24),
        bgcolor=ft.Colors("grey900"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black"),
            offset=ft.Offset(0, 5),
        ),
        content=ft.Column(
            width=280,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            run_spacing=12,
            controls=[
                ft.Container(
                    padding=ft.padding.only(left=8, right=8, bottom=0, top=0),
                    ink_color=ft.Colors("yellow"),
                    expand=True,
                    alignment=ft.alignment.center_left,
                    content=ft.IconButton(
                        icon="navigate_before_rounded",
                        bgcolor="black12",
                        icon_color="red",
                    ),
                ),
                ft.Container(
                    padding=ft.padding.only(left=8, right=8, bottom=8, top=0),
                    content=ft.Text(
                        expand=True,
                        value="Enter your pin",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",
                        size=18,
                    ),
                ),
                ft.Container(
                    padding=ft.padding.only(left=8, right=8, bottom=8, top=0),
                    content=ft.Row(
                        wrap=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=6,
                        run_spacing=8,
                        controls=[
                            ft.Container(
                                width=60,
                                height=60,
                                border_radius=ft.border_radius.all(12),
                                content=ft.TextField(
                                    bgcolor="black12",
                                    min_lines=1,
                                    shift_enter=False,
                                    max_length=1,
                                    text_align=ft.TextAlign.CENTER,
                                    text_vertical_align=ft.VerticalAlignment.CENTER,
                                    border_width=0,
                                    border_radius=ft.border_radius.all(18),
                                    password=True,
                                ),
                            ),
                            ft.Container(
                                width=60,
                                height=60,
                                border_radius=ft.border_radius.all(12),
                                content=ft.TextField(
                                    bgcolor="black12",
                                    min_lines=1,
                                    shift_enter=False,
                                    max_length=1,
                                    text_align=ft.TextAlign.CENTER,
                                    text_vertical_align=ft.VerticalAlignment.CENTER,
                                    border_width=0,
                                    border_radius=ft.border_radius.all(18),
                                    password=True,
                                ),
                            ),
                            ft.Container(
                                width=60,
                                height=60,
                                border_radius=ft.border_radius.all(12),
                                content=ft.TextField(
                                    bgcolor="black12",
                                    min_lines=1,
                                    shift_enter=False,
                                    max_length=1,
                                    text_align=ft.TextAlign.CENTER,
                                    text_vertical_align=ft.VerticalAlignment.CENTER,
                                    border_width=0,
                                    border_radius=ft.border_radius.all(18),
                                    password=True,
                                ),
                            ),
                            ft.Container(
                                width=60,
                                height=60,
                                border_radius=ft.border_radius.all(12),
                                content=ft.TextField(
                                    bgcolor="black12",
                                    min_lines=1,
                                    shift_enter=False,
                                    max_length=1,
                                    text_align=ft.TextAlign.CENTER,
                                    text_vertical_align=ft.VerticalAlignment.CENTER,
                                    border_width=0,
                                    border_radius=ft.border_radius.all(18),
                                    password=True,
                                ),
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    padding=ft.padding.only(left=12, top=12, right=12, bottom=12),
                    margin=ft.margin.only(left=8, top=0, right=8, bottom=0),
                    # width=220,
                    border_radius=ft.border_radius.all(18),
                    bgcolor=ft.Colors("black45"),
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "Confirm",
                                size=14,
                                color=ft.Colors("grey"),
                                weight="bold",
                            ),
                            ft.Icon("navigate_next_rounded"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
            ],
        ),
    ),  # <
}


def custom_widgets(get_widget: str = "", keys=True):

    if keys:
        return widget_dict.get(get_widget)
    else:
        return widget_dict.keys()


def custom_image_dict(get_widget: str = "", keys=True):

    widget_dict = {
        "Long text": "images/long_text.png",
        "Header text": "images/header_text.png",
        "H Dual text": "images/h_dual_text.png",
        "Dual text": "images/dual_text.png",
        "H Triple text": "images/h_triple.png",
        "Triple text": "images/tripletext.png",
        "Add remove": "images/add_remove.png",
        "Stars": "images/stars.png",
        "Volumen": "images/volumen.png",
        "Card text": "images/card_text.png",
        "Card text btn": "images/card_text_btn.png",
        "Best Textfield": "images/besttextfield.png",
        "H banner": "images/bannerh.png",
        "Banner Sales": "images/barnersales.png",
        "Banner title": "images/barnertitle.png",
        "Banner right": "images/barnerright.png",
        "Banner divider": "images/barnerdivider.png",
        "Banner temp": "images/barnertemp.png",
        "Banner date": "images/barnerdate.png",
        "Banner cloud": "images/barnercloud.png",
        "Banner programing": "images/banner_programing.png",
        "Buttom upload": "images/btnico.png",
        "Buttom buy": "images/btn_buy.png",
        "Buttom left": "images/btnl.png",
        "Buttom right": "images/btnr.png",
        "Buttom double": "images/btn_double.png",
        "Dapps app": "images/dapapp.png",
        "Dapps H bar": "images/daph.png",
        "Dapps V bar": "images/dapv.png",
        "Card presentation job": "images/card_presentation_job.png",
        "Card price decoration": "images/card_price_decoration.png",
        "Card pizza": "images/card_pizza.png",
        "Card pizza time": "images/pizza_time.png",
        "Card pizza text": "images/pizza_text.png",
        "Card songs": "images/card_songs.png",
        "Card hotel vacation": "images/card_hotel.png",
        "Card hotel vacation details": "images/card_hotel_details.png",
        "Card hotel vacation add ticket": "images/card_vacation_add_ticket.png",
        "Card breakfast": "images/card_saling_breakfast.png",
        "Card add songs": "images/card_add_songs.png",
        "Card amazon": "images/car_place.png",
        "Card H amazon": "images/card_amazon.png",
        "Card temp": "images/card_temp.png",
        "Card presentation": "images/cardpresentation.png",
        "Card stadium": "images/cardstadium.png",
        "Card shoes": "images/card_shoes.png",
        "Card shoes simple": "images/card_shoes_simple.png",
        "Card shoes add stars": "images/card_add_stars.png",
        "Card shoes add remove": "images/card_add_remove.png",
        "Card shoes out prices": "images/card_shoes_out_price.png",
        "Card shoes out star": "images/card_small_shoes_star.png",
        "Card sport shoes": "images/card_sport_shoes.png",
        "Card sport shopping shoes": "images/card_shoppin_add.png",
        "Card sport remove": "images/card_remove_product.png",
        "Card small": "images/small_card.png",
        "Card small price": "images/card_small_price.png",
        "Card small hotel": "images/small_card_hotel.png",
        "Card small hotel starts": "images/card_only_starts.png",
        "Card small starts": "images/samll_card_starts.png",
        "Card sale pc": "images/card_sale.png",
        "Card btn pc": "images/sellin_pc_btn.png",
        "Card hotel": "images/card_hote.png",
        "Card pop festival": "images/card_festival_concert.png",
        "Card music": "images/card_music.png",
        "Card festival music": "images/card_festival_music.png",
        "Card place": "images/card_place.png",
        "Card event": "images/card_festival.png",
        "Card travel": "images/card_travel.png",
        "Card pop list": "images/card_music_pop.png",
        "Card pop music": "images/card_pop.png",
        "Card pop blur": "images/card_pop_blur.png",
        "Card show": "images/cardshow.png",
        "Regis formulary": "images/regist_formulary.png",
        "Regis verify": "images/regis_verify.png",
        "Regis pin": "images/regis_pin.png",
    }

    if keys:
        return widget_dict.get(get_widget)
    else:
        return widget_dict.keys()


def parse_widget_to_string():
    # Get the path of the current file
    current_file_path = os.path.abspath(__file__)

    # Read the content of the current file
    with open(current_file_path, "r") as file:
        file_content = file.read()

    # Extract the get_data dictionary from the file content
    start_marker = "widget_dict = {"
    end_marker = "}"
    start_index = file_content.find(start_marker) + len(start_marker)
    end_index = file_content.find(end_marker, start_index) + 1

    # Extract the dictionary as a string
    widget_dict_str = file_content[start_index:end_index]

    # Perform replacements (example: replace ': ft' with ': """ft' and '),' with '),"""')
    modified_widget_dict_str = widget_dict_str.replace(": ft", ': """ft').replace(
        ",  # <", '""",'
    )

    # Print the modified widget_dict dictionary
    representation = "{" + modified_widget_dict_str
    original_dict = ast.literal_eval(representation)
    # returned_data = original_dict

    return original_dict
    # print(returned_data)
