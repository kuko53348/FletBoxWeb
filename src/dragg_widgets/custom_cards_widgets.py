import flet as ft
import ast
import os

image = "image97.jpeg"

medium_text = "Flet is a framework that allows building web, desktop and mobile applications in Python without prior experience in frontend development."
few_medium_text = (
    "Flet is a framework that allows building web, desktop and mobile applications"
)


def custom_cards_witgets(get_widget: str = "", keys=True):

    widget_dict = {
        "H banner": ft.Container(
            width=320,
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
                    ft.Row(
                        controls=[
                            ft.Image(
                                src=image,
                                width=40,
                                height=40,
                                fit=ft.ImageFit.COVER,
                                border_radius=ft.border_radius.all(32),
                            ),
                            ft.Column(
                                controls=[
                                    # Banner Title
                                    ft.Text(
                                        "Cannes Film Festival",
                                        size=11,
                                        weight="bold",
                                        color=ft.Colors("white"),
                                    ),
                                    # Banner Description
                                    ft.Text(
                                        "May 14-25, 2024",
                                        size=10,
                                        color=ft.Colors("white70"),
                                    ),
                                ],
                                spacing=5,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                            ),
                        ],
                    ),
                ],
            ),
        ),  # <
        "Banner programing": ft.Container(
            width=320,
            padding=ft.padding.only(left=8, top=8, right=12, bottom=8),
            border_radius=ft.border_radius.all(16),
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            content=ft.Row(
                controls=[
                    ft.Image(
                        src="coding.jpg",
                        width=80,
                        height=80,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(16),
                    ),
                    ft.Column(
                        expand=True,
                        run_spacing=8,
                        spacing=5,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            # Banner Title
                            ft.Text(
                                # expand=True,
                                value="Python programing",
                                size=11,
                                weight="bold",
                                color=ft.Colors("white"),
                            ),
                            ft.Text(
                                value="Flet tutorial",
                                size=10,
                                color=ft.Colors("white70"),
                            ),
                            # Banner Description
                            #
                            ft.Row(
                                spacing=8,
                                run_spacing=8,
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                # expand=True,
                                controls=[
                                    # Banner Title
                                    ft.Text(
                                        # expand=True,
                                        value="12 hrs",
                                        size=11,
                                        weight="bold",
                                        color=ft.Colors("white"),
                                    ),
                                    # Banner Description
                                    ft.Row(
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        run_alignment=ft.CrossAxisAlignment.CENTER,
                                        run_spacing=4,
                                        spacing=4,
                                        controls=[
                                            ft.Icon(name="favorite", size=16),
                                            ft.Text(
                                                value="15 k",
                                                weight="bold",
                                                size=16,
                                                color=ft.Colors("white70"),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ),  # <
        "Banner title": ft.Container(
            width=320,
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
                    ft.Row(
                        controls=[
                            ft.Image(
                                src=image,
                                width=40,
                                height=40,
                                fit=ft.ImageFit.COVER,
                                border_radius=ft.border_radius.all(32),
                            ),
                            ft.Column(
                                controls=[
                                    # Banner Title
                                    ft.Text(
                                        "Cannes Film Festival",
                                        size=11,
                                        weight="bold",
                                        color=ft.Colors("white"),
                                    ),
                                    # Banner Description
                                    ft.Text(
                                        "May 14-25, 2024",
                                        size=10,
                                        color=ft.Colors("white70"),
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Icon(name="place_rounded", size=12),
                                            ft.Text(
                                                value="Addres of presentation",
                                                size=10,
                                                color=ft.Colors("white70"),
                                            ),
                                        ]
                                    ),
                                ],
                                spacing=5,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                            ),
                        ],
                    ),
                    ft.Container(
                        content=ft.Text(
                            value="$999",
                            size=16,
                            # color=ft.Colors("blue"),
                            weight="bold",
                        ),
                        expand=True,
                        padding=ft.padding.only(right=4),
                        alignment=ft.alignment.center_right,
                    ),
                ],
            ),
        ),  # <
        "Banner Sales": ft.Container(
            width=320,
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
                    ft.Row(
                        controls=[
                            ft.Image(
                                src=image,
                                width=40,
                                height=40,
                                fit=ft.ImageFit.COVER,
                                border_radius=ft.border_radius.all(32),
                            ),
                            ft.Column(
                                controls=[
                                    # Banner Title
                                    ft.Text(
                                        "Cannes Film Festival",
                                        size=11,
                                        weight="bold",
                                        color=ft.Colors("white"),
                                    ),
                                    # Banner Description
                                    ft.Text(
                                        "May 14-25, 2024",
                                        size=10,
                                        color=ft.Colors("white70"),
                                    ),
                                ],
                                spacing=5,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                            ),
                        ],
                    ),
                    ft.Container(
                        content=ft.Text(
                            value="$999",
                            size=16,
                            # color=ft.Colors("blue"),
                            weight="bold",
                        ),
                        expand=True,
                        padding=ft.padding.only(right=4),
                        alignment=ft.alignment.center_right,
                    ),
                ],
            ),
        ),  # <
        "Card songs": ft.Container(
            # height=80,
            width=320,
            padding=ft.padding.only(left=8, top=8, right=12, bottom=8),
            border_radius=ft.border_radius.all(24),
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                width=60,
                                height=60,
                                border_radius=ft.border_radius.all(18),
                                content=ft.Image(
                                    src="avatar1.jpg",
                                    fit=ft.ImageFit.COVER,
                                ),
                            ),
                            ft.Column(
                                controls=[
                                    # Banner Title
                                    ft.Text(
                                        value="Lara Craft",
                                        size=14,
                                        weight="bold",
                                        color=ft.Colors("white"),
                                    ),
                                    # Banner Description
                                    ft.Text(
                                        value="843 peopes in a room",
                                        size=12,
                                        color=ft.Colors("white70"),
                                    ),
                                ],
                                spacing=5,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                            ),
                        ],
                    ),
                    ft.Container(
                        height=60,
                        width=60,
                        border_radius=ft.border_radius.all(32),
                        content=ft.Icon(
                            name="mic_rounded",
                        ),
                    ),
                ],
            ),
        ),  # <
        "Card add songs": ft.Container(
            # height=80,
            width=320,
            padding=ft.padding.only(left=8, top=8, right=12, bottom=8),
            border_radius=ft.border_radius.all(24),
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.START,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=12,
                        run_spacing=12,
                        controls=[
                            ft.Container(
                                width=60,
                                height=60,
                                border_radius=ft.border_radius.all(18),
                                content=ft.Image(
                                    src="avatar1.jpg",
                                    fit=ft.ImageFit.COVER,
                                ),
                            ),
                            ft.Column(
                                controls=[
                                    # Banner Title
                                    ft.Text(
                                        value="Lara Craft",
                                        size=14,
                                        weight="bold",
                                        color=ft.Colors("white"),
                                    ),
                                    # Banner Description
                                    ft.Text(
                                        value="843 peopes in a room",
                                        size=12,
                                        color=ft.Colors("white70"),
                                    ),
                                ],
                                spacing=5,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                run_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ],
                    ),
                    ft.Container(
                        bgcolor="white12",
                        # height=60,
                        # width=60,
                        border_radius=ft.border_radius.all(32),
                        content=ft.Icon(
                            name="add_rounded",
                        ),
                    ),
                ],
            ),
        ),  # <
        "Banner right": ft.Container(
            width=320,
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
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    # Banner Title
                                    ft.Text(
                                        "Cannes Film Festival",
                                        size=11,
                                        weight="bold",
                                        color=ft.Colors("white"),
                                    ),
                                    # Banner Description
                                    ft.Text(
                                        "May 14-25, 2024",
                                        size=10,
                                        color=ft.Colors("white70"),
                                    ),
                                ],
                                spacing=5,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                            ),
                        ],
                    ),
                    ft.Image(
                        src=image,
                        width=40,
                        height=40,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(32),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),  # <
        "Banner divider": ft.Container(
            width=320,
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
                    ft.Row(
                        controls=[
                            ft.Column(
                                wrap=True,
                                controls=[
                                    # Banner Title
                                    ft.Text(
                                        "Cannes Film Festival",
                                        size=11,
                                        weight="bold",
                                        color=ft.Colors("white"),
                                    ),
                                    ft.Container(
                                        border_radius=ft.border_radius.only(
                                            top_left=8,
                                            top_right=8,
                                            bottom_left=8,
                                            bottom_right=8,
                                        ),
                                        height=1,
                                        width=140,
                                        bgcolor=ft.Colors.with_opacity(
                                            opacity=0.2,
                                            color=ft.Colors("white"),
                                        ),
                                    ),
                                    # Banner Description
                                    ft.Text(
                                        value="Flet is a framework that allows building web, \ndesktop and mobile applications in Python.",
                                        size=10,
                                        color=ft.Colors("white70"),
                                    ),
                                ],
                                spacing=5,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                            ),
                        ],
                    ),
                    ft.Image(
                        src=image,
                        width=40,
                        height=40,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(32),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),  # <
        "Card price decoration": ft.Container(
            width=300,
            height=200,
            border_radius=ft.border_radius.all(32),
            padding=ft.padding.all(20),
            bgcolor=ft.Colors("white"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="image_avatar.png",
                fit="cover",
                opacity=0.3,
            ),
            content=ft.Column(
                # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                spacing=10,
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    # Brand Name
                    ft.Text(
                        value="World Famous Brands",
                        size=16,
                        weight="bold",
                        color=ft.Colors("grey600"),
                    ),
                    # Description
                    ft.Text(
                        value="More Than 45 Brands",
                        size=28,
                        weight=ft.FontWeight.W_900,
                        color=ft.Colors("grey900"),
                    ),
                    # Price and Discount
                    ft.Row(
                        controls=[
                            ft.Text(
                                value="$19.00",
                                size=18,
                                color=ft.Colors("red600"),
                                weight=ft.FontWeight.W_900,
                                style=ft.TextStyle(
                                    decoration=ft.TextDecoration.LINE_THROUGH,
                                    decoration_color="red",
                                ),  # OVERLINE, UNDERLINE, LINE_THROUGH
                            ),
                            ft.Text(
                                value="$49.00",
                                size=32,
                                color=ft.Colors("grey600"),
                                weight=ft.FontWeight.W_900,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=5,
                    ),
                ],
            ),
        ),  # <
        "Card presentation job": ft.Container(
            width=300,
            height=150,
            border_radius=ft.border_radius.all(32),
            padding=ft.padding.all(20),
            bgcolor=ft.Colors("white"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="apple.png",
                fit="cover",
                opacity=0.18,
            ),
            content=ft.Column(
                controls=[
                    # Business Name
                    ft.Text(
                        value="Tech Solutions Inc.",
                        size=26,
                        weight=ft.FontWeight.W_900,
                        color=ft.Colors("grey800"),
                    ),
                    # Contact Info
                    ft.Text(
                        value="Email: info@techsolutions.com",
                        size=16,
                        weight=ft.FontWeight.W_500,
                        color=ft.Colors("grey600"),
                    ),
                    ft.Text(
                        value="Phone: +1 234 567 890",
                        size=16,
                        color=ft.Colors("grey600"),
                        weight=ft.FontWeight.W_900,
                    ),
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),  # <
        "Card pizza": ft.Container(
            # expand=True,
            padding=ft.padding.only(left=12, top=12, right=12, bottom=12),
            border_radius=ft.border_radius.all(12),
            width=320,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="pizza_get.jpg",
                fit="cover",
                opacity=0.18,
            ),
            content=ft.Column(
                controls=[
                    # Banner Title
                    ft.Text(
                        value="35% OFF",
                        size=18,
                        weight="bold",
                        color=ft.Colors("white"),
                    ),
                    # Banner Description
                    ft.Text(
                        value="Get Best offer now",
                        size=12,
                        color=ft.Colors("white70"),
                    ),
                    ft.Container(
                        # expand=True,
                        margin=ft.margin.only(
                            top=16,
                        ),
                        padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
                        border_radius=ft.border_radius.all(12),
                        ink_color=ft.colors("yellow"),
                        alignment=ft.alignment.center,
                        width=100,
                        bgcolor=ft.Colors("red900"),
                        content=ft.Text(
                            value="Buy Now ",
                            size=11,
                            weight="bold",
                            color=ft.Colors("white70"),
                        ),
                    ),
                ],
                spacing=2,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
        ),  # <
        "Card pizza time": ft.Container(
            # expand=True,
            padding=ft.padding.only(left=0, top=0, right=0, bottom=0),
            border_radius=ft.border_radius.all(32),
            width=320,
            height=160,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="pizza_get.jpg",
                fit="cover",
                opacity=0.5,
            ),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.END,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=8,
                run_spacing=8,
                controls=[
                    ft.Container(
                        padding=ft.padding.only(left=24, right=24, bottom=8, top=8),
                        border_radius=ft.border_radius.only(
                            top_left=0, top_right=32, bottom_left=0, bottom_right=0
                        ),
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.8, color=ft.Colors("red")
                        ),
                        content=ft.Text(
                            width=80,
                            weight=ft.FontWeight.BOLD,
                            font_family="Consolas",
                            value="25-30 min",
                        ),
                    ),
                ],
            ),
        ),  # <
        "Card pizza text": ft.Container(
            # expand=True,
            padding=ft.padding.only(left=0, top=0, right=0, bottom=0),
            border_radius=ft.border_radius.all(32),
            width=320,
            height=160,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="pizza_get.jpg",
                fit="cover",
                opacity=0.5,
            ),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.END,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=8,
                run_spacing=8,
                controls=[
                    ft.Container(
                        padding=ft.padding.only(left=24, right=24, bottom=8, top=8),
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.8, color=ft.Colors("grey900")
                        ),
                        expand=True,
                        content=ft.Text(
                            text_align=ft.TextAlign.RIGHT,
                            width=100,
                            weight=ft.FontWeight.BOLD,
                            font_family="Consolas",
                            size=18,
                            value="Can you hear the bass boom? I'm ready",
                        ),
                    ),
                ],
            ),
        ),  # <
        "Card amazon": ft.Container(
            expand=True,
            padding=ft.padding.only(left=12, top=12, right=12, bottom=12),
            border_radius=ft.border_radius.all(12),
            width=320,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="amazon.jpg",
                fit="cover",
                opacity=0.18,
            ),
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            # Banner Title
                            ft.Text(
                                value="35% OFF",
                                size=18,
                                weight="bold",
                                color=ft.Colors("white"),
                            ),
                            # Banner Description
                            ft.Text(
                                value="Get Best offer now",
                                size=12,
                                color=ft.Colors("white70"),
                            ),
                            ft.Container(
                                expand=True,
                                margin=ft.margin.only(
                                    top=16,
                                ),
                                padding=ft.padding.only(
                                    left=12, top=8, right=12, bottom=8
                                ),
                                border_radius=ft.border_radius.all(12),
                                ink_color=ft.colors("yellow"),
                                alignment=ft.alignment.center,
                                width=100,
                                bgcolor=ft.Colors("red900"),
                                content=ft.Text(
                                    value="Buy Now ",
                                    size=11,
                                    weight="bold",
                                    color=ft.Colors("white70"),
                                ),
                            ),
                        ],
                        spacing=2,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Image(
                        src="audifonos1.jpg",
                        width=100,
                        height=100,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(32),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),  # <
        "Card shoes": ft.Container(
            # expand=True,
            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
            border_radius=ft.border_radius.all(32),
            width=320,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="clothes.jpg",
                fit="cover",
                opacity=0.18,
            ),
            content=ft.Row(
                controls=[
                    ft.Image(
                        src="shoes.jpg",
                        width=150,
                        height=150,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(32),
                    ),
                    ft.Column(
                        # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                        # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True,
                        spacing=12,
                        run_spacing=12,
                        controls=[
                            # Banner Title
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        value="35% OFF",
                                        size=18,
                                        weight="bold",
                                        color=ft.Colors("white"),
                                    ),
                                    # Banner Description
                                    ft.Text(
                                        value="Get Best offer now",
                                        size=12,
                                        color=ft.Colors("white70"),
                                    ),
                                ]
                            ),
                            ft.Container(
                                expand=True,
                                margin=ft.margin.only(
                                    top=16,
                                ),
                                padding=ft.padding.only(
                                    left=12, top=8, right=12, bottom=8
                                ),
                                border_radius=ft.border_radius.all(24),
                                ink_color=ft.colors("yellow"),
                                alignment=ft.alignment.center,
                                width=100,
                                bgcolor=ft.Colors("red900"),
                                content=ft.Text(
                                    value="Buy Now ",
                                    size=11,
                                    weight="bold",
                                    color=ft.Colors("white70"),
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        ),  # <
        "Card shoes add stars": ft.Container(
            # expand=True,
            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
            border_radius=ft.border_radius.all(32),
            width=320,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="clothes.jpg",
                fit="cover",
                opacity=0.18,
            ),
            content=ft.Row(
                controls=[
                    ft.Image(
                        src="shoes.jpg",
                        width=150,
                        height=150,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(32),
                    ),
                    ft.Column(
                        # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                        # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        # expand=True,
                        spacing=16,
                        run_spacing=16,
                        controls=[
                            # Banner Title
                            ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                run_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=0,
                                run_spacing=0,
                                controls=[
                                    ft.Text(
                                        value="Shoes",
                                        size=24,
                                        weight="bold",
                                        color=ft.Colors("white70"),
                                    ),
                                    # Banner Description
                                    ft.Text(
                                        value="$149.7",
                                        weight="bold",
                                        size=38,
                                        color=ft.Colors("white"),
                                    ),
                                    ft.Row(
                                        # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        # vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        # run_alignment=ft.CrossAxisAlignment.CENTER,
                                        # expand=True,
                                        spacing=12,
                                        run_spacing=12,
                                        controls=[
                                            ft.Row(
                                                # expand=True,
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                run_alignment=ft.CrossAxisAlignment.CENTER,
                                                spacing=4,
                                                run_spacing=4,
                                                controls=[
                                                    ft.Icon(
                                                        name="star",
                                                        size=12,
                                                        color=ft.Colors("yellow"),
                                                    ),
                                                    ft.Text(
                                                        value="4.0",
                                                        weight="bold",
                                                        size=12,
                                                        color=ft.Colors("white"),
                                                    ),
                                                ],
                                            ),
                                            ft.Row(
                                                # expand=True,
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                run_alignment=ft.CrossAxisAlignment.CENTER,
                                                spacing=4,
                                                run_spacing=4,
                                                controls=[
                                                    ft.Text(
                                                        value="343",
                                                        weight="bold",
                                                        size=12,
                                                        color=ft.Colors("white"),
                                                    ),
                                                    ft.Text(
                                                        value="reviews",
                                                        weight="bold",
                                                        size=12,
                                                        color=ft.Colors("white"),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            ft.Container(
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
                                            padding=ft.padding.all(2),
                                            bgcolor=ft.Colors("grey700"),
                                            border_radius=ft.border_radius.only(
                                                top_left=32,
                                                top_right=32,
                                                bottom_left=32,
                                                bottom_right=32,
                                            ),
                                            alignment=ft.alignment.center,
                                            ink=True,
                                            ink_color=ft.colors("yellow"),
                                            content=ft.Icon(name="remove_rounded"),
                                            on_click=lambda arguments: print("hello"),
                                        ),
                                        ft.Text(
                                            value="0",
                                            size=16,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        ft.Container(
                                            padding=ft.padding.all(2),
                                            bgcolor=ft.Colors("grey700"),
                                            border_radius=ft.border_radius.only(
                                                top_left=32,
                                                top_right=32,
                                                bottom_left=32,
                                                bottom_right=32,
                                            ),
                                            alignment=ft.alignment.center,
                                            ink=True,
                                            ink_color=ft.colors("yellow"),
                                            content=ft.Icon(name="add_rounded"),
                                            on_click=lambda arguments: print("hello"),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        ),  # <
        "Card shoes add remove": ft.Container(
            # expand=True,
            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
            border_radius=ft.border_radius.all(32),
            width=320,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="clothes.jpg",
                fit="cover",
                opacity=0.18,
            ),
            content=ft.Row(
                controls=[
                    ft.Image(
                        src="shoes.jpg",
                        width=150,
                        height=150,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(32),
                    ),
                    ft.Column(
                        # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                        # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        # expand=True,
                        spacing=16,
                        run_spacing=16,
                        controls=[
                            # Banner Title
                            ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                run_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=0,
                                run_spacing=0,
                                controls=[
                                    ft.Text(
                                        value="Shoes",
                                        size=24,
                                        weight="bold",
                                        color=ft.Colors("white70"),
                                    ),
                                    # Banner Description
                                    ft.Text(
                                        value="$149.7",
                                        weight="bold",
                                        size=38,
                                        color=ft.Colors("white"),
                                    ),
                                ],
                            ),
                            ft.Container(
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
                                            padding=ft.padding.all(2),
                                            bgcolor=ft.Colors("grey700"),
                                            border_radius=ft.border_radius.only(
                                                top_left=32,
                                                top_right=32,
                                                bottom_left=32,
                                                bottom_right=32,
                                            ),
                                            alignment=ft.alignment.center,
                                            ink=True,
                                            ink_color=ft.colors("yellow"),
                                            content=ft.Icon(name="remove_rounded"),
                                            on_click=lambda arguments: print("hello"),
                                        ),
                                        ft.Text(
                                            value="0",
                                            size=16,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        ft.Container(
                                            padding=ft.padding.all(2),
                                            bgcolor=ft.Colors("grey700"),
                                            border_radius=ft.border_radius.only(
                                                top_left=32,
                                                top_right=32,
                                                bottom_left=32,
                                                bottom_right=32,
                                            ),
                                            alignment=ft.alignment.center,
                                            ink=True,
                                            ink_color=ft.colors("yellow"),
                                            content=ft.Icon(name="add_rounded"),
                                            on_click=lambda arguments: print("hello"),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        ),  # <
        "Card sport remove": ft.Container(
            # expand=True,
            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
            border_radius=ft.border_radius.all(32),
            width=320,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            # image=ft.DecorationImage(
            #     src="clothes.jpg",
            #     fit="cover",
            #     opacity=0.18,
            # ),
            content=ft.Row(
                controls=[
                    ft.Image(
                        src="shoes.jpg",
                        width=150,
                        height=150,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(32),
                    ),
                    ft.Column(
                        # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                        # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        # expand=True,
                        spacing=16,
                        run_spacing=16,
                        controls=[
                            # Banner Title
                            ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                run_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=0,
                                run_spacing=0,
                                controls=[
                                    ft.Column(
                                        expand=True,
                                        controls=[
                                            ft.Text(
                                                # expand=True,
                                                value="Remove a product",
                                                size=14,
                                                weight="bold",
                                                color=ft.Colors("white"),
                                            ),
                                            # Banner Description
                                            ft.Text(
                                                value="Do you want to remove fresh from your cart?",
                                                weight="bold",
                                                size=12,
                                                width=160,
                                                # expand=True,
                                                color=ft.Colors("white70"),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            ft.Container(
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
                                        ft.ElevatedButton(text="No", bgcolor="grey900"),
                                        ft.ElevatedButton(
                                            text="Remove",
                                            bgcolor="red900",
                                            color="white",
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        ),  # <
        "Card shoes simple": ft.Container(
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            border_radius=ft.border_radius.all(32),
            padding=ft.padding.only(left=0, top=0, right=0, bottom=8),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        # expand=True,
                        padding=ft.padding.only(left=8, top=8, right=8, bottom=12),
                        border_radius=ft.border_radius.all(32),
                        width=200,
                        height=200,
                        image=ft.DecorationImage(
                            src="image_search_1740143908354.jpg",
                            fit="cover",
                            opacity=0.8,
                        ),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            horizontal_alignment=ft.CrossAxisAlignment.END,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            expand=True,
                            spacing=0,
                            run_spacing=0,
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(
                                        left=8, right=8, bottom=8, top=8
                                    ),
                                    # bgcolor=ft.Colors.with_opacity(
                                    #     opacity=0.8, color=ft.Colors("grey900")
                                    # ),
                                    border_radius=ft.border_radius.only(
                                        top_left=32,
                                        top_right=32,
                                        bottom_left=32,
                                        bottom_right=32,
                                    ),
                                    # expand=True,
                                    content=ft.Icon(
                                        name="favorite",
                                        color=ft.Colors.with_opacity(
                                            opacity=0.8, color=ft.Colors("red900")
                                        ),
                                    ),
                                ),
                                ft.Container(
                                    padding=ft.padding.only(
                                        left=8, right=8, bottom=8, top=8
                                    ),
                                    bgcolor=ft.Colors.with_opacity(
                                        opacity=0.8, color=ft.Colors("grey900")
                                    ),
                                    border_radius=ft.border_radius.only(
                                        top_left=32,
                                        top_right=32,
                                        bottom_left=32,
                                        bottom_right=32,
                                    ),
                                    # expand=True,
                                    content=ft.Icon(
                                        name="shopping_cart_checkout_sharp",
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        ),  # <
        "Card sport shopping shoes": ft.Container(
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            border_radius=ft.border_radius.all(32),
            padding=ft.padding.only(left=0, top=0, right=0, bottom=8),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        # expand=True,
                        padding=ft.padding.only(left=8, top=8, right=8, bottom=12),
                        border_radius=ft.border_radius.all(32),
                        width=200,
                        height=200,
                        image=ft.DecorationImage(
                            src="image_search_1740143908354.jpg",
                            fit="cover",
                            opacity=0.8,
                        ),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            expand=True,
                            spacing=0,
                            run_spacing=0,
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(
                                        left=8, right=8, bottom=8, top=8
                                    ),
                                    bgcolor=ft.Colors.with_opacity(
                                        opacity=0.8, color=ft.Colors("grey900")
                                    ),
                                    border_radius=ft.border_radius.only(
                                        top_left=32,
                                        top_right=32,
                                        bottom_left=32,
                                        bottom_right=32,
                                    ),
                                    # expand=True,
                                    content=ft.Icon(
                                        name="shopping_cart_checkout_sharp",
                                    ),
                                ),
                            ],
                        ),
                    ),
                    ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True,
                        spacing=0,
                        run_spacing=0,
                        controls=[
                            ft.Container(
                                content=ft.Text(
                                    text_align=ft.TextAlign.LEFT,
                                    weight=ft.FontWeight.BOLD,
                                    font_family="Consolas",
                                    size=24,
                                    value="$156.99 ",
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        ),  # <
        "Card sport shoes": ft.Container(
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
                    ft.Container(
                        # expand=True,
                        padding=ft.padding.only(left=8, top=0, right=8, bottom=12),
                        border_radius=ft.border_radius.all(32),
                        width=200,
                        height=200,
                        image=ft.DecorationImage(
                            src="image_search_1740143908354.jpg",
                            fit="cover",
                            opacity=0.8,
                        ),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.END,
                            horizontal_alignment=ft.CrossAxisAlignment.END,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            expand=True,
                            spacing=0,
                            run_spacing=0,
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(
                                        left=8, right=8, bottom=8, top=8
                                    ),
                                    bgcolor=ft.Colors.with_opacity(
                                        opacity=0.8, color=ft.Colors("grey900")
                                    ),
                                    border_radius=ft.border_radius.only(
                                        top_left=32,
                                        top_right=32,
                                        bottom_left=32,
                                        bottom_right=32,
                                    ),
                                    # expand=True,
                                    content=ft.Icon(
                                        name="shopify_rounded",
                                    ),
                                ),
                            ],
                        ),
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
                                value="Sport shoes",
                                text_align=ft.TextAlign.CENTER,
                                weight=ft.FontWeight.BOLD,
                                font_family="Consolas",
                                color=ft.Colors.with_opacity(
                                    opacity=0.6, color=ft.Colors("white")
                                ),
                            ),
                            ft.Container(
                                content=ft.Text(
                                    text_align=ft.TextAlign.LEFT,
                                    weight=ft.FontWeight.BOLD,
                                    font_family="Consolas",
                                    size=24,
                                    value="$156.99 ",
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        ),  # <
        "Card shoes out prices": ft.Container(
            # bgcolor=ft.Colors("grey900"),
            # shadow=ft.BoxShadow(
            #     spread_radius=1,
            #     blur_radius=15,
            #     color=ft.Colors("black"),
            #     offset=ft.Offset(0, 5),
            # ),
            border_radius=ft.border_radius.all(32),
            padding=ft.padding.only(left=4, top=0, right=4, bottom=18),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        # expand=True,
                        padding=ft.padding.only(left=8, top=0, right=8, bottom=12),
                        border_radius=ft.border_radius.all(32),
                        width=200,
                        height=200,
                        image=ft.DecorationImage(
                            src="image_search_1740143908354.jpg",
                            fit="cover",
                            opacity=0.8,
                        ),
                        bgcolor=ft.Colors("grey900"),
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=4,
                            color=ft.Colors("black"),
                            offset=ft.Offset(0, 5),
                        ),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.END,
                            horizontal_alignment=ft.CrossAxisAlignment.END,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            expand=True,
                            spacing=0,
                            run_spacing=0,
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(
                                        left=8, right=8, bottom=8, top=8
                                    ),
                                    bgcolor=ft.Colors.with_opacity(
                                        opacity=0.8, color=ft.Colors("grey900")
                                    ),
                                    border_radius=ft.border_radius.only(
                                        top_left=32,
                                        top_right=32,
                                        bottom_left=32,
                                        bottom_right=32,
                                    ),
                                    # expand=True,
                                    content=ft.Icon(
                                        name="shopify_rounded",
                                    ),
                                ),
                            ],
                        ),
                    ),
                    ft.Container(
                        padding=ft.padding.only(left=8, right=0, bottom=0, top=0),
                        expand=True,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            expand=True,
                            spacing=0,
                            run_spacing=0,
                            controls=[
                                ft.Text(
                                    expand=True,
                                    value="Sport shoes",
                                    text_align=ft.TextAlign.CENTER,
                                    weight=ft.FontWeight.BOLD,
                                    font_family="Consolas",
                                    color=ft.Colors.with_opacity(
                                        opacity=0.6, color=ft.Colors("white")
                                    ),
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        text_align=ft.TextAlign.LEFT,
                                        weight=ft.FontWeight.BOLD,
                                        font_family="Consolas",
                                        size=24,
                                        value="$156.99 ",
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        ),  # <
        "Card shoes out star": ft.Container(
            # bgcolor=ft.Colors("grey900"),
            # shadow=ft.BoxShadow(
            #     spread_radius=1,
            #     blur_radius=15,
            #     color=ft.Colors("black"),
            #     offset=ft.Offset(0, 5),
            # ),
            padding=ft.padding.only(left=4, top=0, right=4, bottom=18),
            width=200,
            content=ft.Column(
                # width=220,
                # alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        # expand=True,
                        padding=ft.padding.only(left=8, top=0, right=8, bottom=12),
                        border_radius=ft.border_radius.all(32),
                        width=200,
                        height=200,
                        image=ft.DecorationImage(
                            src="image_search_1740143908354.jpg",
                            fit="cover",
                            opacity=0.8,
                        ),
                        bgcolor=ft.Colors("grey900"),
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=4,
                            color=ft.Colors("black"),
                            offset=ft.Offset(0, 5),
                        ),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.END,
                            horizontal_alignment=ft.CrossAxisAlignment.END,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0,
                            run_spacing=0,
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(
                                        left=8, right=8, bottom=8, top=8
                                    ),
                                    bgcolor=ft.Colors.with_opacity(
                                        opacity=0.8, color=ft.Colors("grey900")
                                    ),
                                    border_radius=ft.border_radius.only(
                                        top_left=32,
                                        top_right=32,
                                        bottom_left=32,
                                        bottom_right=32,
                                    ),
                                    # expand=True,
                                    content=ft.Icon(
                                        name="shopify_rounded",
                                    ),
                                ),
                            ],
                        ),
                    ),
                    ft.Container(
                        padding=ft.padding.only(left=8, right=8, bottom=0, top=0),
                        # expand=True,
                        content=ft.Column(
                            spacing=0,
                            run_spacing=0,
                            controls=[
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    run_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            # expand=True,
                                            value="Sport shoes",
                                            text_align=ft.TextAlign.CENTER,
                                            weight=ft.FontWeight.BOLD,
                                            font_family="Consolas",
                                            color=ft.Colors.with_opacity(
                                                opacity=0.6, color=ft.Colors("white")
                                            ),
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                            run_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=2,
                                            run_spacing=2,
                                            controls=[
                                                ft.Icon(
                                                    name="star", size=12, color="yellow"
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
                                    ],
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        text_align=ft.TextAlign.LEFT,
                                        weight=ft.FontWeight.BOLD,
                                        font_family="Consolas",
                                        size=24,
                                        value="$156.99 ",
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        ),  # <
        "Card H amazon": ft.Container(
            expand=True,
            padding=ft.padding.only(left=12, top=12, right=12, bottom=12),
            border_radius=ft.border_radius.all(12),
            width=320,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="amazon.jpg",
                fit="cover",
                opacity=0.18,
            ),
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            # Banner Title
                            ft.Text(
                                value="35% OFF",
                                size=18,
                                weight="bold",
                                color=ft.Colors("white"),
                            ),
                            # Banner Description
                            ft.Text(
                                value="Get Best offer now",
                                size=12,
                                color=ft.Colors("white70"),
                            ),
                        ],
                        spacing=2,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Container(
                        expand=True,
                        padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
                        border_radius=ft.border_radius.all(12),
                        ink_color=ft.colors("yellow"),
                        alignment=ft.alignment.center,
                        width=100,
                        bgcolor=ft.Colors("red900"),
                        content=ft.Text(
                            value="Buy Now ",
                            size=11,
                            weight="bold",
                            color=ft.Colors("white70"),
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),  # <
        "Card hotel vacation": ft.Container(
            # expand=True,
            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
            border_radius=ft.border_radius.all(32),
            width=320,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="image_search_1740142228438.jpg",
                fit="cover",
                opacity=0.18,
            ),
            content=ft.Row(
                controls=[
                    ft.Image(
                        src="image_search_1740142228438.jpg",
                        width=150,
                        height=150,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(32),
                    ),
                    ft.Column(
                        # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                        # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True,
                        spacing=12,
                        run_spacing=12,
                        controls=[
                            # Banner Title
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        value="Global Hotel",
                                        size=18,
                                        weight="bold",
                                        color=ft.Colors("white"),
                                    ),
                                    ft.Container(
                                        # width=100,
                                        border_radius=ft.border_radius.all(24),
                                        expand=True,
                                        content=ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                            run_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=6,
                                            run_spacing=8,
                                            controls=[
                                                ft.Icon(
                                                    name="star_rounded",
                                                    size=16,
                                                    color="yellow600",
                                                ),
                                                ft.Icon(
                                                    name="star_rounded",
                                                    size=16,
                                                    color="yellow600",
                                                ),
                                                ft.Icon(
                                                    name="star_rounded",
                                                    size=16,
                                                    color="yellow600",
                                                ),
                                                ft.Icon(
                                                    name="star_rounded",
                                                    size=16,
                                                    color="yellow600",
                                                ),
                                                ft.Icon(
                                                    name="star_rounded",
                                                    size=16,
                                                    color="yellow600",
                                                ),
                                            ],
                                        ),
                                    ),
                                ]
                            ),
                            ft.Container(
                                expand=True,
                                margin=ft.margin.only(
                                    top=16,
                                ),
                                padding=ft.padding.only(
                                    left=8, top=8, right=8, bottom=8
                                ),
                                border_radius=ft.border_radius.all(18),
                                ink_color=ft.colors("yellow"),
                                alignment=ft.alignment.center,
                                width=100,
                                bgcolor=ft.Colors("white54"),
                                content=ft.Text(
                                    value="Details",
                                    size=16,
                                    weight="bold",
                                    color=ft.Colors("grey900"),
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        ),  # <
        "Card hotel vacation details": ft.Container(
            # expand=True,
            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
            border_radius=ft.border_radius.all(32),
            width=320,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="image_search_1740142228438.jpg",
                fit="cover",
                opacity=0.18,
            ),
            content=ft.Row(
                controls=[
                    ft.Image(
                        src="image_search_1740142228438.jpg",
                        width=150,
                        height=150,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(32),
                    ),
                    ft.Column(
                        # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                        # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True,
                        spacing=0,
                        run_spacing=0,
                        controls=[
                            # Banner Title
                            ft.Column(
                                spacing=8,
                                run_spacing=8,
                                controls=[
                                    ft.Text(
                                        value="Global Hotel",
                                        size=18,
                                        weight=ft.FontWeight.W_900,
                                        color=ft.Colors("white"),
                                    ),
                                    ft.Text(
                                        value=few_medium_text,
                                        size=11,
                                        color=ft.Colors("white70"),
                                    ),
                                    ft.Container(
                                        expand=True,
                                        padding=ft.padding.only(
                                            left=8, top=8, right=8, bottom=8
                                        ),
                                        border_radius=ft.border_radius.all(18),
                                        ink_color=ft.colors("yellow"),
                                        alignment=ft.alignment.center,
                                        width=100,
                                        bgcolor=ft.Colors("white54"),
                                        content=ft.Text(
                                            value="Details",
                                            size=16,
                                            weight="bold",
                                            color=ft.Colors("grey900"),
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ),  # <
        "Card hotel vacation add ticket": ft.Container(
            # expand=True,
            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
            border_radius=ft.border_radius.all(32),
            width=320,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="image_search_1740142228438.jpg",
                fit="cover",
                opacity=0.18,
            ),
            content=ft.Row(
                controls=[
                    ft.Image(
                        src="image_search_1740142228438.jpg",
                        width=150,
                        height=150,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(32),
                    ),
                    ft.Column(
                        # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                        # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True,
                        spacing=0,
                        run_spacing=0,
                        controls=[
                            # Banner Title
                            ft.Column(
                                spacing=8,
                                run_spacing=8,
                                controls=[
                                    ft.Text(
                                        value="Global Hotel",
                                        size=18,
                                        weight=ft.FontWeight.W_900,
                                        color=ft.Colors("white"),
                                    ),
                                    ft.Text(
                                        value=few_medium_text,
                                        size=11,
                                        color=ft.Colors("white70"),
                                    ),
                                    ft.Container(
                                        expand=True,
                                        # border_radius=ft.border_radius.all(8),
                                        ink_color=ft.colors("yellow"),
                                        alignment=ft.alignment.center,
                                        # width=100,
                                        # padding=ft.padding.only(
                                        #     left=0, top=0, right=0, bottom=0
                                        # ),
                                        # bgcolor=ft.Colors("white54"),
                                        content=ft.Row(
                                            # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                            # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                            run_alignment=ft.CrossAxisAlignment.CENTER,
                                            # expand=True,
                                            spacing=8,
                                            run_spacing=8,
                                            controls=[
                                                # Banner Title
                                                ft.Text(
                                                    value="$12.00",
                                                    size=16,
                                                    weight="bold",
                                                    color=ft.Colors("white"),
                                                ),
                                                ft.Container(
                                                    bgcolor=ft.Colors("grey800"),
                                                    ink=True,
                                                    ink_color=ft.Colors("red"),
                                                    opacity=1.0,
                                                    padding=ft.Padding(
                                                        left=2, top=2, right=2, bottom=2
                                                    ),
                                                    border_radius=ft.border_radius.all(
                                                        8
                                                    ),
                                                    shadow=[],
                                                    visible=True,
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                        run_alignment=ft.CrossAxisAlignment.CENTER,
                                                        # expand=True,
                                                        spacing=4,
                                                        run_spacing=4,
                                                        controls=[
                                                            ft.Container(
                                                                bgcolor=ft.Colors(
                                                                    "white54"
                                                                ),
                                                                border_radius=ft.border_radius.only(
                                                                    top_left=8,
                                                                    top_right=8,
                                                                    bottom_left=8,
                                                                    bottom_right=8,
                                                                ),
                                                                alignment=ft.alignment.center,
                                                                ink=True,
                                                                ink_color=ft.colors(
                                                                    "yellow"
                                                                ),
                                                                content=ft.Icon(
                                                                    name="remove_rounded",
                                                                    color=ft.Colors(
                                                                        "grey800"
                                                                    ),
                                                                ),
                                                                on_click=lambda arguments: print(
                                                                    "hello"
                                                                ),
                                                            ),
                                                            ft.Text(
                                                                value="0",
                                                                size=16,
                                                            ),
                                                            ft.Container(
                                                                bgcolor=ft.Colors(
                                                                    "white54"
                                                                ),
                                                                border_radius=ft.border_radius.only(
                                                                    top_left=8,
                                                                    top_right=8,
                                                                    bottom_left=8,
                                                                    bottom_right=8,
                                                                ),
                                                                alignment=ft.alignment.center,
                                                                ink=True,
                                                                ink_color=ft.colors(
                                                                    "yellow"
                                                                ),
                                                                content=ft.Icon(
                                                                    name="add_rounded",
                                                                    color=ft.Colors(
                                                                        "grey800"
                                                                    ),
                                                                ),
                                                                on_click=lambda arguments: print(
                                                                    "hello"
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ),  # <
        "Card breakfast": ft.Container(
            bgcolor=ft.Colors("black12"),
            border_radius=ft.BorderRadius(
                top_left=32, top_right=32, bottom_left=32, bottom_right=32
            ),
            image=ft.DecorationImage(
                src="image_search_1740143480957.webp",
                fit=ft.ImageFit.COVER,
                opacity=0.5,
            ),  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors("black"),
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            ink=True,
            ink_color=ft.Colors("red"),
            margin=ft.Margin(left=0, top=0, right=0, bottom=0),
            offset=ft.Offset(x=0, y=0),
            opacity=1.0,
            padding=ft.Padding(left=16, top=16, right=16, bottom=16),
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
                        bgcolor=ft.Colors("transparent"),
                        border_radius=ft.BorderRadius(
                            top_left=0, top_right=0, bottom_left=0, bottom_right=0
                        ),
                        ink=True,
                        ink_color=ft.Colors("red"),
                        margin=ft.Margin(left=0, top=0, right=0, bottom=0),
                        offset=ft.Offset(x=0, y=0),
                        opacity=1.0,
                        padding=ft.Padding(left=8, top=8, right=8, bottom=8),
                        shadow=[],
                        visible=True,
                        content=ft.Text(
                            color=ft.Colors("white"),
                            enable_interactive_selection=True,
                            offset=ft.Offset(x=0, y=0),
                            opacity=1.0,
                            selection_cursor_width=2.0,
                            size=15,
                            value="New year sale",
                            visible=True,
                            weight=ft.FontWeight.W_500,
                        ),
                    ),
                    ft.Container(
                        bgcolor=ft.Colors("transparent"),
                        border_radius=ft.BorderRadius(
                            top_left=0, top_right=0, bottom_left=0, bottom_right=0
                        ),
                        ink=True,
                        ink_color=ft.Colors("red"),
                        margin=ft.Margin(left=0, top=0, right=0, bottom=0),
                        offset=ft.Offset(x=0, y=0),
                        opacity=1.0,
                        padding=ft.Padding(left=8, top=8, right=8, bottom=8),
                        shadow=[],
                        visible=True,
                        content=ft.Text(
                            color=ft.Colors("white"),
                            enable_interactive_selection=True,
                            offset=ft.Offset(x=0, y=0),
                            opacity=1.0,
                            selection_cursor_width=2.0,
                            size=24.0,
                            value="Change text OFF",
                            visible=True,
                            weight=ft.FontWeight.W_900,
                        ),
                    ),
                    ft.Container(
                        bgcolor=ft.Colors("transparent"),
                        ink=True,
                        ink_color=ft.Colors("red"),
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
                                    bgcolor=ft.Colors("grey900"),
                                    border_radius=ft.BorderRadius(
                                        top_left=12,
                                        top_right=12,
                                        bottom_left=12,
                                        bottom_right=12,
                                    ),
                                    padding=ft.Padding(
                                        left=12, top=8, right=12, bottom=8
                                    ),
                                    shadow=[],
                                    visible=True,
                                    content=ft.Text(
                                        color=ft.Colors("white"),
                                        enable_interactive_selection=True,
                                        offset=ft.Offset(x=0, y=0),
                                        opacity=1.0,
                                        selection_cursor_width=2.0,
                                        size=15,
                                        value="Small",
                                        visible=True,
                                        weight=ft.FontWeight.W_600,
                                    ),
                                ),
                                ft.Container(
                                    bgcolor=ft.Colors("grey900"),
                                    border_radius=ft.BorderRadius(
                                        top_left=12,
                                        top_right=12,
                                        bottom_left=12,
                                        bottom_right=12,
                                    ),
                                    padding=ft.Padding(
                                        left=12, top=8, right=12, bottom=8
                                    ),
                                    shadow=[],
                                    visible=True,
                                    content=ft.Text(
                                        color=ft.Colors("white"),
                                        enable_interactive_selection=True,
                                        offset=ft.Offset(x=0, y=0),
                                        opacity=1.0,
                                        selection_cursor_width=2.0,
                                        size=15,
                                        value="Medium",
                                        visible=True,
                                        weight=ft.FontWeight.W_600,
                                    ),
                                ),
                                ft.Container(
                                    bgcolor=ft.Colors("yellow600"),
                                    border_radius=ft.BorderRadius(
                                        top_left=12,
                                        top_right=12,
                                        bottom_left=12,
                                        bottom_right=12,
                                    ),
                                    padding=ft.Padding(
                                        left=12, top=8, right=12, bottom=8
                                    ),
                                    shadow=[],
                                    visible=True,
                                    content=ft.Text(
                                        color=ft.Colors("grey800"),
                                        enable_interactive_selection=True,
                                        offset=ft.Offset(x=0, y=0),
                                        opacity=1.0,
                                        selection_cursor_width=2.0,
                                        size=15,
                                        value="Extra large",
                                        visible=True,
                                        weight=ft.FontWeight.W_900,
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        ),  # <
        "Card sale pc": ft.Container(
            width=300,
            height=250,
            border_radius=ft.border_radius.all(32),
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="pc5.png",
                fit="fill",
                # opacity=0.18,
            ),
            padding=ft.padding.all(24),
            alignment=ft.alignment.bottom_center,
            content=ft.Column(
                controls=[
                    # iPhone Model
                    ft.Text(
                        value="Pc Pro Gamer",
                        size=18,
                        weight="bold",
                        color=ft.Colors("white"),
                    ),
                    ft.Row(
                        controls=[
                            ft.Text(
                                value="Discount: ",
                                size=18,
                                weight="bold",
                                color=ft.Colors("white"),
                            ),
                            # Price
                            ft.Text(
                                value="$999",
                                size=16,
                                color=ft.Colors("blue"),
                                weight="bold",
                                spans=[
                                    ft.TextSpan(
                                        " $1200",
                                        ft.TextStyle(
                                            decoration=ft.TextDecoration.LINE_THROUGH,
                                            size=20,
                                            color=ft.Colors("white"),
                                        ),
                                    ),
                                ],
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.END,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
        ),  # <
        "Card btn pc": ft.Container(
            width=300,
            height=250,
            border_radius=ft.border_radius.all(32),
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="pc5.png",
                fit="fill",
                # opacity=0.18,
            ),
            padding=ft.padding.all(24),
            alignment=ft.alignment.bottom_center,
            content=ft.Column(
                controls=[
                    # iPhone Model
                    ft.Text(
                        value="Pc Pro Gamer",
                        size=18,
                        weight="bold",
                        color=ft.Colors("white"),
                    ),
                    ft.Row(
                        controls=[
                            # Price
                            ft.Text(
                                value="$999 ",
                                size=24,
                                color=ft.Colors("blue"),
                                weight="bold",
                                spans=[
                                    ft.TextSpan(
                                        "$1200",
                                        ft.TextStyle(
                                            decoration=ft.TextDecoration.LINE_THROUGH,
                                            size=16,
                                            color=ft.Colors("white"),
                                        ),
                                    ),
                                ],
                            ),
                            ft.IconButton(icon="shopify_rounded", bgcolor="red"),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.END,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
        ),  # <
        "Card music": ft.Container(
            # card_music_festival
            width=400,
            height=200,
            border_radius=ft.border_radius.only(
                top_left=32, top_right=32, bottom_left=32, bottom_right=32
            ),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(src="pop.jpg", fit=ft.ImageFit.COVER, opacity=0.7),
            content=ft.Column(
                controls=[
                    # Banner Title
                    ft.Text(
                        value="Pop music festival",
                        size=24,
                        weight="bold",
                        color=ft.Colors("white"),
                    ),
                    # Banner Description
                    ft.Text("May 14-25, 2024", size=16, color=ft.Colors("white")),
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),  # <
        "Card hotel": ft.Container(
            width=300,
            # height=200,
            border_radius=ft.border_radius.all(32),
            padding=ft.padding.all(6),
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="hotel.jpg",
                fit="cover",
                opacity=0.06,
            ),
            content=ft.Column(
                controls=[
                    # Hotel Image
                    ft.Image(
                        src="hotel.jpg",
                        width=300,
                        height=150,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(32),
                    ),
                    # Hotel Name
                    ft.Container(
                        padding=ft.padding.only(left=6, top=6, right=6, bottom=6),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            # expand = True,
                            spacing=8,
                            run_spacing=8,
                            controls=[
                                ft.Text(
                                    value="Luxury Resort",
                                    size=18,
                                    weight="bold",
                                    color=ft.Colors("white"),
                                ),
                                # Location
                                ft.Text(
                                    value="Maldives",
                                    size=14,
                                    color=ft.Colors("white"),
                                ),
                                # Price
                                ft.Text(
                                    value="$299/night",
                                    size=16,
                                    color=ft.Colors("blue400"),
                                    weight="bold",
                                ),
                            ],
                        ),
                    ),
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
        ),  # <
        "Card place": ft.Container(
            # height=80,
            padding=ft.padding.only(left=14, top=14, right=14, bottom=14),
            border_radius=ft.border_radius.all(24),
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="stadium.jpg",
                fit="cover",
                opacity=0.1,
            ),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8,
                run_spacing=12,
                controls=[
                    ft.Container(
                        bgcolor="red",
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(24),
                        padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
                        # width=240,
                        # height=200,
                        expand=True,
                        image=ft.DecorationImage(
                            src="concert1.jpg",
                            fit=ft.ImageFit.COVER,
                            opacity=0.8,
                        ),
                        content=ft.Column(
                            spacing=8,
                            expand=True,
                            run_spacing=8,
                            width=240,
                            height=200,
                            controls=[
                                ft.IconButton(
                                    icon="favorite",
                                    bgcolor="black45",
                                    icon_color="red",
                                ),
                            ],
                        ),
                    ),
                    ft.Container(
                        padding=ft.padding.only(left=4, top=8, right=4, bottom=8),
                        content=ft.Column(
                            controls=[
                                # Banner Title
                                ft.Text(
                                    value="Cannes Film Festival",
                                    size=14,
                                    weight="bold",
                                    color=ft.Colors("white"),
                                ),
                                # Banner Description
                                ft.Text(
                                    value="Flet is a framework that allows building web, desktop and mobile applications in Python.",
                                    size=11,
                                    color=ft.Colors("white24"),
                                ),
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                        ),
                    ),
                    ft.Row(
                        controls=[
                            ft.TextField(
                                bgcolor=ft.Colors.with_opacity(
                                    opacity=0.01,
                                    color=ft.Colors("white"),
                                ),
                                border_color=ft.Colors("transparent"),
                                # icon=ft.Icons.ACCOUNT_CIRCLE_ROUNDED,
                                hint_text="Ubication",
                                expand=True,
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
                                content=ft.Icon(name="navigate_next_rounded"),
                            ),
                        ],
                    ),
                ],
            ),
        ),  # <
        "Card event": ft.Container(
            width=300,
            # height=150,
            border_radius=ft.border_radius.all(32),
            padding=ft.padding.only(left=6, top=6, right=6, bottom=16),
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="stadium.jpg",
                fit="cover",
                opacity=0.1,
            ),
            content=ft.Column(
                controls=[
                    ft.Image(
                        src="concert2.jpg",
                        width=300,
                        height=150,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(32),
                    ),
                    # Event Name
                    ft.Text(
                        value="Music Festival 2024",
                        size=20,
                        weight="bold",
                        color=ft.Colors("white"),
                    ),
                    # Date
                    ft.Text(value="June 15, 2024", size=14, color=ft.Colors("white")),
                    # Price
                    ft.Text(
                        value="$99.99",
                        size=16,
                        color=ft.Colors("blue400"),
                        weight="bold",
                    ),
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
        ),  # <
        "Card pop music": ft.Container(
            width=300,
            # height=200,
            border_radius=ft.border_radius.all(32),
            padding=ft.padding.all(8),
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            # image=ft.DecorationImage(
            #     src="pop.jpg",
            #     fit="cover",
            #     opacity=0.18,
            # ),
            content=ft.Column(
                controls=[
                    # Hotel Image
                    ft.Image(
                        src="pop.jpg",
                        width=300,
                        height=150,
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(32),
                    ),
                    # Hotel Name
                    ft.Column(
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True,
                        spacing=8,
                        run_spacing=8,
                        controls=[
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        # Banner Title
                                        ft.Text(
                                            value="Cannes Film Festival",
                                            size=14,
                                            weight="bold",
                                            color=ft.Colors("white"),
                                        ),
                                        # Banner Description
                                        ft.Text(
                                            value="May 14-25, 2024",
                                            size=11,
                                            color=ft.Colors("white70"),
                                        ),
                                    ],
                                    spacing=5,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.START,
                                ),
                            ),  #
                            ft.Text(
                                value=medium_text,
                                size=11,
                                color=ft.Colors("white70"),
                            ),
                            ft.Container(
                                expand=True,
                                padding=ft.padding.only(
                                    left=12, top=8, right=12, bottom=8
                                ),
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
                                        ft.Icon(name="arrow_right"),
                                        ft.Text(
                                            value="Listen now",
                                            size=14,
                                            color=ft.Colors("grey"),
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
                spacing=5,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
        ),  # <
        "Card small": ft.Container(
            # card_music_festival
            width=150,
            height=200,
            border_radius=ft.border_radius.only(
                top_left=10, top_right=10, bottom_left=10, bottom_right=10
            ),
            padding=ft.padding.all(12),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(src="pop.jpg", fit=ft.ImageFit.COVER, opacity=0.2),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=8,
                run_spacing=8,
                controls=[
                    ft.Container(
                        border_radius=ft.border_radius.only(
                            top_left=32, top_right=32, bottom_left=32, bottom_right=32
                        ),
                        border=ft.border.all(width=2, color=ft.colors("white12")),
                        image=ft.DecorationImage(
                            src="pop.jpg",
                            fit=ft.ImageFit.COVER,
                        ),  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
                        alignment=ft.alignment.center,
                        height=48,
                        width=48,
                        ink_color=ft.colors("yellow"),
                        bgcolor=ft.colors("black12"),
                    ),
                    ft.Column(
                        spacing=8,
                        run_spacing=8,
                        controls=[
                            # Banner Title
                            ft.Text(
                                value="Pop music festival",
                                size=16,
                                weight="bold",
                                color=ft.Colors("white"),
                            ),
                            # Banner Description
                            ft.Text(
                                value="May 14-25, 2024",
                                size=12,
                                color=ft.Colors("white"),
                            ),
                            ft.ElevatedButton(
                                text="View",
                                bgcolor=ft.Colors.with_opacity(
                                    opacity=0.4, color=ft.Colors("orange900")
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                ],
            ),
        ),  # <
        "Card small price": ft.Container(
            # card_music_festival
            width=120,
            height=120,
            border_radius=ft.border_radius.only(
                top_left=32, top_right=32, bottom_left=32, bottom_right=32
            ),
            padding=ft.padding.all(12),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(src="pop.jpg", fit=ft.ImageFit.COVER, opacity=0.1),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=8,
                run_spacing=8,
                controls=[
                    ft.Container(
                        border_radius=ft.border_radius.only(
                            top_left=32, top_right=32, bottom_left=32, bottom_right=32
                        ),
                        border=ft.border.all(width=2, color=ft.colors("white12")),
                        image=ft.DecorationImage(
                            src="pop.jpg",
                            fit=ft.ImageFit.COVER,
                        ),  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
                        alignment=ft.alignment.center,
                        height=48,
                        width=48,
                        ink_color=ft.colors("yellow"),
                        bgcolor=ft.colors("black12"),
                    ),
                    ft.Column(
                        spacing=0,
                        run_spacing=0,
                        controls=[
                            # Banner Title
                            ft.Text(
                                value="UI/UIX Course",
                                size=12,
                                color=ft.Colors("white"),
                            ),
                            # Banner Description
                            ft.Text(
                                value="$50.00",
                                size=17,
                                weight="bold",
                                color=ft.Colors("white"),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                ],
            ),
        ),  # <
        "Card small hotel": ft.Container(
            # expand=True,
            padding=ft.padding.only(left=8, top=0, right=8, bottom=12),
            border_radius=ft.border_radius.all(32),
            width=200,
            height=200,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="hotel.jpg",
                fit="cover",
                opacity=0.2,
            ),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.END,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=0,
                run_spacing=0,
                controls=[
                    ft.Container(
                        content=ft.Text(
                            text_align=ft.TextAlign.LEFT,
                            weight=ft.FontWeight.BOLD,
                            font_family="Consolas",
                            size=16,
                            value="Sawat, Pakistan",
                        ),
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                padding=ft.padding.only(
                                    left=0, right=0, bottom=0, top=0
                                ),
                                content=ft.Text(
                                    text_align=ft.TextAlign.LEFT,
                                    weight=ft.FontWeight.BOLD,
                                    font_family="Consolas",
                                    size=18,
                                    value="104 $/ person",
                                ),
                            ),
                            ft.Container(
                                padding=ft.padding.only(
                                    left=8, right=8, bottom=8, top=8
                                ),
                                bgcolor=ft.Colors.with_opacity(
                                    opacity=0.2, color=ft.Colors("white")
                                ),
                                border_radius=ft.border_radius.only(
                                    top_left=32,
                                    top_right=32,
                                    bottom_left=32,
                                    bottom_right=32,
                                ),
                                # expand=True,
                                content=ft.Icon(
                                    name="favorite",
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        ),  # <
        "Card small hotel starts": ft.Container(
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
        ),  # <
        "Card small starts": ft.Container(
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
                    ft.Container(
                        # expand=True,
                        padding=ft.padding.only(left=8, top=0, right=8, bottom=12),
                        border_radius=ft.border_radius.all(32),
                        width=200,
                        height=200,
                        image=ft.DecorationImage(
                            src="hotel.jpg",
                            fit="cover",
                            opacity=0.2,
                        ),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.END,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            expand=True,
                            spacing=0,
                            run_spacing=0,
                            controls=[
                                ft.Container(
                                    content=ft.Text(
                                        text_align=ft.TextAlign.LEFT,
                                        weight=ft.FontWeight.BOLD,
                                        font_family="Consolas",
                                        size=16,
                                        value="Sawat, Pakistan",
                                    ),
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    run_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Container(
                                            padding=ft.padding.only(
                                                left=0, right=0, bottom=0, top=0
                                            ),
                                            content=ft.Text(
                                                text_align=ft.TextAlign.LEFT,
                                                weight=ft.FontWeight.BOLD,
                                                font_family="Consolas",
                                                size=18,
                                                value="104 $/ person",
                                            ),
                                        ),
                                        ft.Container(
                                            padding=ft.padding.only(
                                                left=8, right=8, bottom=8, top=8
                                            ),
                                            bgcolor=ft.Colors.with_opacity(
                                                opacity=0.2, color=ft.Colors("white")
                                            ),
                                            border_radius=ft.border_radius.only(
                                                top_left=32,
                                                top_right=32,
                                                bottom_left=32,
                                                bottom_right=32,
                                            ),
                                            # expand=True,
                                            content=ft.Icon(
                                                name="favorite",
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
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
        ),  # <
        "Card stadium": ft.Container(
            # card_music_festival
            width=200,
            height=280,
            border_radius=ft.border_radius.only(
                top_left=18,
                top_right=18,
                bottom_left=18,
                bottom_right=18,
            ),
            padding=ft.padding.all(0),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="stadium.jpg",
                fit=ft.ImageFit.COVER,
                opacity=0.8,
            ),
            content=ft.Column(
                # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                alignment=ft.MainAxisAlignment.END,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        blur=(12, 12),
                        padding=ft.padding.only(left=12, right=12, bottom=12, top=12),
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[
                                ft.colors("transparent"),
                                ft.colors("black"),
                            ],
                        ),
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            controls=[
                                # Banner Title
                                ft.Text(
                                    value="Pop music festival",
                                    size=18,
                                    weight="bold",
                                    color=ft.Colors("white"),
                                ),
                                # Banner Description
                                ft.Row(
                                    controls=[
                                        ft.Icon(name="share", size=15),
                                        ft.Text(
                                            value="8 hr with best music",
                                            size=12,
                                            color=ft.Colors("white"),
                                        ),
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                            width=100,
                                            padding=ft.padding.only(
                                                left=8, top=8, right=8, bottom=8
                                            ),
                                            border_radius=ft.border_radius.all(24),
                                            expand=True,
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.START,
                                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                run_alignment=ft.CrossAxisAlignment.CENTER,
                                                spacing=6,
                                                run_spacing=8,
                                                controls=[
                                                    ft.Icon(
                                                        name="star_rounded", size=12
                                                    ),
                                                    ft.Icon(
                                                        name="star_rounded", size=12
                                                    ),
                                                    ft.Icon(
                                                        name="star_rounded", size=12
                                                    ),
                                                    ft.Icon(
                                                        name="star_rounded", size=12
                                                    ),
                                                    ft.Icon(
                                                        name="star_rounded", size=12
                                                    ),
                                                ],
                                            ),
                                        ),
                                        ft.Container(
                                            #: [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                            # tooltip = 'Container',
                                            padding=ft.padding.only(
                                                left=8, right=8, bottom=8, top=8
                                            ),
                                            border_radius=ft.border_radius.only(
                                                top_left=32,
                                                top_right=32,
                                                bottom_left=32,
                                                bottom_right=32,
                                            ),
                                            alignment=ft.alignment.center,
                                            ink_color=ft.colors("yellow"),
                                            bgcolor=ft.colors("white12"),
                                            content=ft.Icon(name="favorite"),
                                        ),
                                    ]
                                ),
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.END,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                        ),
                    ),
                ],
            ),
        ),  # <
        "Card festival music": ft.Container(
            # card_music_festival
            width=200,
            height=280,
            border_radius=ft.border_radius.only(
                top_left=18,
                top_right=18,
                bottom_left=18,
                bottom_right=18,
            ),
            padding=ft.padding.all(0),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="stadium.jpg",
                fit=ft.ImageFit.COVER,
                opacity=0.8,
            ),
            content=ft.Column(
                # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                alignment=ft.MainAxisAlignment.END,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        padding=ft.padding.only(left=12, right=12, bottom=12, top=12),
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[
                                ft.colors("transparent"),
                                ft.colors("black"),
                            ],
                        ),
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            controls=[
                                # Banner Title
                                ft.Container(
                                    padding=ft.padding.all(8),
                                    content=ft.Column(
                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                        horizontal_alignment=ft.CrossAxisAlignment.START,
                                        run_alignment=ft.CrossAxisAlignment.CENTER,
                                        expand=True,
                                        spacing=0,
                                        run_spacing=0,
                                        controls=[
                                            ft.Text(
                                                value="Pop music festival",
                                                size=18,
                                                weight="bold",
                                                color=ft.Colors("white"),
                                            ),
                                            # Banner Description
                                            ft.Text(
                                                value="8 hr with best music",
                                                size=12,
                                                color=ft.Colors("white"),
                                            ),
                                        ],
                                    ),
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                            width=100,
                                            padding=ft.padding.only(
                                                left=8, top=8, right=8, bottom=8
                                            ),
                                            border_radius=ft.border_radius.all(24),
                                            expand=True,
                                            content=ft.Text(
                                                size=28,
                                                expand=True,
                                                value="$ 650",
                                                text_align=ft.TextAlign.START,
                                                weight=ft.FontWeight.BOLD,
                                                font_family="Consolas",
                                            ),
                                        ),
                                        ft.Container(
                                            #: [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                            # tooltip = 'Container',
                                            padding=ft.padding.only(
                                                left=8, right=8, bottom=8, top=8
                                            ),
                                            border_radius=ft.border_radius.only(
                                                top_left=32,
                                                top_right=32,
                                                bottom_left=32,
                                                bottom_right=32,
                                            ),
                                            alignment=ft.alignment.center,
                                            ink_color=ft.colors("yellow"),
                                            bgcolor=ft.colors("white12"),
                                            content=ft.Icon(name="add_rounded"),
                                        ),
                                    ]
                                ),
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.END,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                        ),
                    ),
                ],
            ),
        ),  # <
        "Card pop list": ft.Container(
            # card_music_festival
            width=400,
            height=200,
            border_radius=ft.border_radius.only(
                top_left=10, top_right=10, bottom_left=10, bottom_right=10
            ),
            padding=ft.padding.all(12),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(src="pop.jpg", fit=ft.ImageFit.COVER, opacity=0.2),
            content=ft.Row(
                # alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.END,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=8,
                run_spacing=8,
                controls=[
                    ft.Container(
                        border_radius=ft.border_radius.only(
                            top_left=32, top_right=32, bottom_left=32, bottom_right=32
                        ),
                        border=ft.border.all(width=2, color=ft.colors("white12")),
                        image=ft.DecorationImage(
                            src="pop.jpg",
                            fit=ft.ImageFit.COVER,
                        ),  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
                        alignment=ft.alignment.center,
                        height=48,
                        width=48,
                        ink_color=ft.colors("yellow"),
                        bgcolor=ft.colors("black12"),
                    ),
                    ft.Column(
                        controls=[
                            # Banner Title
                            ft.Text(
                                value="Pop music festival",
                                size=18,
                                weight="bold",
                                color=ft.Colors("white"),
                            ),
                            # Banner Description
                            ft.Text(
                                "May 14-25, 2024",
                                size=12,
                                color=ft.Colors("white"),
                            ),
                        ],
                        spacing=5,
                        alignment=ft.MainAxisAlignment.END,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                ],
            ),
        ),  # <
        "Card pop festival": ft.Container(
            # card_music_festival
            width=400,
            height=200,
            border_radius=ft.border_radius.only(
                top_left=10, top_right=10, bottom_left=10, bottom_right=10
            ),
            padding=ft.padding.all(0),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="stadium.jpg", fit=ft.ImageFit.COVER, opacity=0.4
            ),
            content=ft.Column(
                controls=[
                    ft.Container(
                        alignment=ft.alignment.top_right,
                        ink_color=ft.colors("yellow"),
                        padding=ft.padding.only(left=12, right=12, bottom=12, top=12),
                        expand=True,
                        bgcolor=ft.colors("black12"),
                        content=ft.Icon(name="favorite_rounded"),
                    ),
                    ft.Container(
                        padding=ft.padding.only(left=12, right=12, bottom=12, top=12),
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[
                                ft.colors("transparent"),
                                ft.colors("black"),
                            ],
                        ),
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            controls=[
                                # Banner Title
                                ft.Text(
                                    value="Pop music festival",
                                    size=18,
                                    weight="bold",
                                    color=ft.Colors("white"),
                                ),
                                # Banner Description
                                ft.Row(
                                    controls=[
                                        ft.Icon(name="add_location_rounded", size=15),
                                        ft.Text(
                                            "May 14-25, 2024",
                                            size=12,
                                            color=ft.Colors("white"),
                                        ),
                                    ]
                                ),
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.END,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                        ),
                    ),
                ]
            ),
        ),  # <
        "Card pop blur": ft.Container(
            # card_music_festival
            width=400,
            height=200,
            border_radius=ft.border_radius.only(
                top_left=10, top_right=10, bottom_left=10, bottom_right=10
            ),
            padding=ft.padding.all(0),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="stadium.jpg", fit=ft.ImageFit.COVER, opacity=0.4
            ),
            content=ft.Column(
                controls=[
                    ft.Container(
                        alignment=ft.alignment.top_right,
                        ink_color=ft.colors("yellow"),
                        padding=ft.padding.only(left=12, right=12, bottom=12, top=12),
                        expand=True,
                        bgcolor=ft.colors("black12"),
                        content=ft.Icon(name="favorite_rounded"),
                    ),
                    ft.Container(
                        blur=(12, 12),
                        padding=ft.padding.only(left=12, right=12, bottom=12, top=12),
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[
                                ft.colors("transparent"),
                                ft.colors("black"),
                            ],
                        ),
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            controls=[
                                # Banner Title
                                ft.Text(
                                    value="Pop music festival",
                                    size=18,
                                    weight="bold",
                                    color=ft.Colors("white"),
                                ),
                                # Banner Description
                                ft.Row(
                                    controls=[
                                        ft.Icon(name="share", size=15),
                                        ft.Text(
                                            value="8 hr with best music",
                                            size=12,
                                            color=ft.Colors("white"),
                                        ),
                                    ]
                                ),
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.END,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                        ),
                    ),
                ]
            ),
        ),  # <
        "Card show": ft.Container(
            # card_music_festival
            width=250,
            height=250,
            border_radius=ft.border_radius.only(
                top_left=10, top_right=10, bottom_left=10, bottom_right=10
            ),
            padding=ft.padding.all(0),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="stadium.jpg", fit=ft.ImageFit.COVER, opacity=0.4
            ),
            content=ft.Column(
                controls=[
                    ft.Container(
                        alignment=ft.alignment.top_right,
                        ink_color=ft.colors("yellow"),
                        padding=ft.padding.only(left=8, right=8, bottom=8, top=8),
                        expand=True,
                        bgcolor=ft.colors("black12"),
                        content=ft.Icon(name="live_tv_rounded"),
                    ),
                    ft.Container(
                        # blur=(12, 12),
                        border_radius=ft.border_radius.only(
                            top_left=16, top_right=16, bottom_left=16, bottom_right=16
                        ),
                        margin=ft.margin.only(left=8, right=8, bottom=8, top=8),
                        padding=ft.padding.only(left=12, right=12, bottom=12, top=12),
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.9,
                            color=ft.Colors("grey900"),
                        ),
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            controls=[
                                # Banner Title
                                ft.Text(
                                    value="Live concert now",
                                    size=18,
                                    weight="bold",
                                    color=ft.Colors("white"),
                                ),
                                # Banner Description
                                ft.Row(
                                    expand=True,
                                    controls=[
                                        ft.Icon(
                                            name="local_attraction_outlined",
                                            # size=15,
                                        ),
                                        ft.Text(
                                            expand=True,
                                            value="Watch your favorite Artist in live in action",
                                            size=12,
                                            color=ft.Colors("white"),
                                        ),
                                    ],
                                ),
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.END,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                        ),
                    ),
                ]
            ),
        ),  # <
        "Card presentation": ft.Container(
            # card_music_festival
            width=250,
            height=250,
            border_radius=ft.border_radius.only(
                top_left=24, top_right=24, bottom_left=24, bottom_right=24
            ),
            padding=ft.padding.all(0),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            bgcolor=ft.Colors.with_opacity(opacity=0.5, color=ft.Colors("grey900")),
            alignment=ft.alignment.bottom_right,
            image=ft.DecorationImage(
                src="stadium.jpg", fit=ft.ImageFit.COVER, opacity=0.4
            ),
            content=ft.Stack(
                controls=[
                    ft.Container(
                        blur=(2, 2),
                        border_radius=ft.border_radius.only(
                            top_left=24, top_right=24, bottom_left=24, bottom_right=120
                        ),
                        border=ft.border.all(width=2, color=ft.colors("grey900")),
                        alignment=ft.alignment.bottom_right,
                        ink_color=ft.colors("yellow"),
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.1, color=ft.Colors("white")
                        ),
                    ),
                    ft.Container(
                        # left=32,
                        padding=ft.padding.all(16),
                        alignment=ft.alignment.bottom_right,
                        content=ft.Container(
                            bgcolor=ft.Colors("grey900"),
                            border_radius=ft.border_radius.only(
                                top_left=32,
                                top_right=32,
                                bottom_left=32,
                                bottom_right=32,
                            ),
                            border=ft.border.all(
                                width=2,
                                color=ft.Colors.with_opacity(
                                    opacity=0.4, color=ft.Colors("transparent")
                                ),
                            ),
                            padding=ft.padding.all(12),
                            content=ft.Icon(name="keyboard_arrow_right_rounded"),
                        ),
                    ),
                    ft.Container(
                        padding=ft.padding.all(16),
                        expand=True,
                        content=ft.Row(
                            controls=[
                                ft.Column(
                                    controls=[
                                        # Banner Title
                                        ft.Text(
                                            value="Cannes Film Festival",
                                            size=18,
                                            weight="bold",
                                            color=ft.Colors("white"),
                                        ),
                                        # Banner Description
                                        ft.Text(
                                            value="Date: May 14-25, 2024",
                                            size=16,
                                            color=ft.Colors("white70"),
                                        ),
                                    ],
                                    spacing=2,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.START,
                                ),
                            ],
                            spacing=2,
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                        ),
                    ),
                ]
            ),
        ),  # <
    }

    if keys:
        return widget_dict.get(get_widget)
    else:
        return widget_dict.keys()


def parse_cards_widget_to_string():
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
