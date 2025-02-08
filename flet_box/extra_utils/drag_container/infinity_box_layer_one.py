import flet as ft
import datetime

from .categories import widgets_by_categories

md1 = """## Code blocks

Formatted Dart code looks really pretty too:

```
void main() {
    runApp(MaterialApp(
        home: Scaffold(
        body: ft.Markdown(data: markdownData),
    ),
    ));
}
```"""
PRESENTATION_TEXT: str = """Ready to make your first app!!"""
numWidget: int = 1

same_image = ft.Image(
    src="logo.png",
    width=200,
    height=200,
    fit=ft.ImageFit.NONE,
    repeat=ft.ImageRepeat.NO_REPEAT,
    border_radius=ft.border_radius.all(10),
)


class Container(ft.Container):

    def __init__(
        self,
        page: object = ft.Page,
        content: object = None,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page

        self.bgcolor = ft.Colors.with_opacity(opacity=0.02, color=ft.colors("white"))
        self.alignment = ft.alignment.center
        self.padding = ft.padding.all(6)
        self.border = ft.border.all(2, ft.colors("cyan900"))
        self.tooltip = "Row"
        self.ink = True
        self.ink_color = "cyan"

        self.content = content
        self.on_click = event_manager


class DragTarget(ft.DragTarget):
    """
    NOTE:

    1. THIS IS VERY IMPORTANT WIDGET TO DRAGG AND DROP
    IS A LOOP DRAGGTARGET THAT WILL CONTAIN ALL WIDGET INSIDE.

    AND IT SELF WILL ADD WIDGETS DEPENDIND
    ROW , COLUMN , GRIDVIEW ... USE CONTROLS=[ WIDGETS, WIDGETS... ]
    REST WIDGETS USE CONTENT = WIDGET()

    2. Make widget need
    """

    md1 = """# Markdown Example Markdown allows you to easily include formatted text, images, and even formatted Dart code in your app.\n## Titles"""

    long_text = "Flet is a framework that allows building web, desktop and mobile applications in Python without prior experience in frontend development.\n\nYou can build a UI for your program with Flet controls which are based on Flutter by Google. Flet goes beyond merely wrapping Flutter widgets. It adds its own touch by combining smaller widgets, simplifying complexities, implementing UI best practices, and applying sensible defaults. This ensures that your applications look stylish and polished without requiring additional design efforts on your part."

    def __init__(self, dataPassed: str = str(), page: object = ft.Page):
        super().__init__(content=ft.Container())
        self.group = "GroupDragg"
        self.page = page
        self.dataPassed = "CLICK_EVENT"
        self.clip_behavior = ft.ClipBehavior.NONE

        # self.widgets = {
        #     #: SPACE LAYOUTS
        #     "Divider": [
        #         ft.Container(
        #             bgcolor=ft.colors("transparent"),
        #             alignment=ft.alignment.center,
        #             padding=ft.padding.all(6),
        #             margin=ft.margin.all(0),
        #             border=ft.border.all(0, ft.colors("transparent")),
        #             tooltip="Divider",
        #             ink=True,
        #             ink_color="red",
        #             on_click=lambda _: self.touch_widget_in_phone(
        #                 selected_widget=self.infinityDropWidget
        #             ),
        #             content=ft.Divider(),
        #         ),
        #     ],
        # }

        self.alert_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Text("Do you really want to delete all those files?"),
            actions=[
                ft.TextButton("Yes", on_click=lambda _: print("hello")),
                ft.TextButton(
                    "No",
                    on_click=lambda _: self.page.close(self.alert_dialog),
                ),
            ],
        )
        self.alert_barner = ft.Banner(
            bgcolor=ft.Colors.AMBER_100,
            leading=ft.Icon(
                ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.AMBER, size=40
            ),
            content=ft.Text(
                value="Oops, there were some errors while trying to delete the file. What would you like me to do?",
                color=ft.Colors.BLACK,
            ),
            actions=[
                ft.TextButton(
                    text="Retry",
                    style=ft.ButtonStyle(color=ft.Colors("blue")),
                    # on_click=self.page.close(self.alert_barner),
                ),
                ft.TextButton(
                    text="Ignore",
                    style=ft.ButtonStyle(color=ft.Colors("blue")),
                    # on_click=self.page.close(self.alert_barner),
                ),
                ft.TextButton(
                    text="Cancel",
                    style=ft.ButtonStyle(color=ft.Colors("blue")),
                    # on_click=self.page.close(self.alert_barner),
                ),
            ],
        )

        data_1 = [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 1),
                    ft.LineChartDataPoint(3, 1.5),
                    ft.LineChartDataPoint(5, 1.4),
                    ft.LineChartDataPoint(7, 3.4),
                    ft.LineChartDataPoint(10, 2),
                    ft.LineChartDataPoint(12, 2.2),
                    ft.LineChartDataPoint(13, 1.8),
                ],
                stroke_width=8,
                color=ft.Colors.LIGHT_GREEN,
                curved=True,
                stroke_cap_round=True,
            ),
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 1),
                    ft.LineChartDataPoint(3, 2.8),
                    ft.LineChartDataPoint(7, 1.2),
                    ft.LineChartDataPoint(10, 2.8),
                    ft.LineChartDataPoint(12, 2.6),
                    ft.LineChartDataPoint(13, 3.9),
                ],
                color=ft.Colors.PINK,
                below_line_bgcolor=ft.Colors.with_opacity(0, ft.Colors.PINK),
                stroke_width=8,
                curved=True,
                stroke_cap_round=True,
            ),
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 2.8),
                    ft.LineChartDataPoint(3, 1.9),
                    ft.LineChartDataPoint(6, 3),
                    ft.LineChartDataPoint(10, 1.3),
                    ft.LineChartDataPoint(13, 2.5),
                ],
                color=ft.Colors.CYAN,
                stroke_width=8,
                curved=True,
                stroke_cap_round=True,
            ),
        ]
        self.animation_container_1 = ft.Container(
            content=ft.Text(value="Hello!"),
            alignment=ft.alignment.center,
            width=200,
            height=200,
            bgcolor=ft.Colors.GREEN,
            on_click=lambda _: self.animate(widget=_.control.parent),
        )

        self.animation_container_2 = ft.Container(
            content=ft.Text(value="Bye!"),
            alignment=ft.alignment.center,
            width=200,
            height=200,
            bgcolor=ft.Colors("blue"),
            on_click=lambda _: self.animate(widget=_.control.parent),
        )

        self.animated_switcher = ft.AnimatedSwitcher(
            visible=True,
            transition=ft.AnimatedSwitcherTransition.SCALE,
            duration=500,
            reverse_duration=100,
            switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
            switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
            content=self.animation_container_1,
        )
        self.image = "image97.jpeg"
        self.column_swap = ft.Column(
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
                    padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
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
                                content=ft.Icon(name="search"),
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
                                content=ft.Icon(name="search"),
                            ),
                        ],
                    ),
                ),
            ],
        )
        self.widgets = {
            # CUSTOM BUTTON
            # TEXT
            "long_text": ft.Column(
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
                        value=self.long_text,
                        size=11,
                        color=ft.Colors("white70"),
                    ),
                ],
                spacing=16,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            "doble_l_text": ft.Row(
                controls=[
                    # Banner Title
                    ft.Container(
                        expand=True,
                        content=ft.Text(
                            "Cannes Film Festival",
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
            "doble_text": ft.Column(
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
            "triple_l_text": ft.Row(
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
            "triple_text": ft.Column(
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
            "star": ft.Row(
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
            # CARDS UI DESIGN
            "film_festival_banner": ft.Container(
                # film_festival_banner
                width=400,
                height=200,
                border_radius=10,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=[ft.Colors("black12"), ft.Colors("black87")],
                ),
                content=ft.Column(
                    controls=[
                        # Banner Title
                        ft.Text(
                            "Cannes Film Festival",
                            size=24,
                            weight="bold",
                            color=ft.Colors("white"),
                        ),
                        # Banner Description
                        ft.Text("May 14-25, 2024", size=16, color=ft.Colors("white70")),
                    ],
                    spacing=5,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            "left_banner": ft.Container(
                padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
                border_radius=ft.border_radius.all(12),
                bgcolor=ft.Colors("black45"),
                content=ft.Row(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Image(
                                    src=self.image,
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
            ),
            "swap_dapp": ft.Container(
                # height=80,
                padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
                border_radius=ft.border_radius.all(32),
                bgcolor=ft.Colors("black45"),
                content=ft.Column(
                    controls=[
                        ft.Stack(
                            controls=[
                                self.column_swap,
                                ft.Container(
                                    border_radius=ft.border_radius.all(12),
                                    bgcolor="black54",
                                    left=self.column_swap.width / 2.3,
                                    right=self.column_swap.width / 2.3,
                                    top=self.column_swap.height / 2.4,
                                    bottom=self.column_swap.height / 2.4,
                                    content=ft.Icon(
                                        name="swap_vertical_circle_rounded"
                                    ),
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
                                icon_disabled_color=True,
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
                            padding=ft.padding.only(
                                left=12, top=12, right=12, bottom=12
                            ),
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
                                    ft.Icon(name="navigate_next_rounded"),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ),
                    ]
                ),
            ),
            "sales_banner": ft.Container(
                # height=80,
                padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
                border_radius=ft.border_radius.all(12),
                bgcolor=ft.Colors("black45"),
                # width=200,
                # gradient=ft.LinearGradient(
                #     begin=ft.alignment.top_left,
                #     end=ft.alignment.bottom_right,
                #     colors=[ft.colors.PURPLE, ft.Colors("blue")],
                # ),
                content=ft.Row(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Image(
                                    src=self.image,
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
            ),
            "sales_title_banner": ft.Container(
                # height=80,
                padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
                border_radius=ft.border_radius.all(12),
                bgcolor=ft.Colors("black45"),
                # width=200,
                # gradient=ft.LinearGradient(
                #     begin=ft.alignment.top_left,
                #     end=ft.alignment.bottom_right,
                #     colors=[ft.colors.PURPLE, ft.Colors("blue")],
                # ),
                content=ft.Row(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Image(
                                    src=self.image,
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
            ),
            "right_banner": ft.Container(
                # height=80,
                padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
                border_radius=ft.border_radius.all(12),
                bgcolor=ft.Colors("black45"),
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
                            src=self.image,
                            width=40,
                            height=40,
                            fit=ft.ImageFit.COVER,
                            border_radius=ft.border_radius.all(32),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            "right_divider_banner": ft.Container(
                # height=80,
                padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
                border_radius=ft.border_radius.all(12),
                bgcolor=ft.Colors("black45"),
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
                            src=self.image,
                            width=40,
                            height=40,
                            fit=ft.ImageFit.COVER,
                            border_radius=ft.border_radius.all(32),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            "custom FextField": ft.Container(
                # height=80,
                padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
                border_radius=ft.border_radius.all(24),
                expand=True,
                bgcolor=ft.Colors("black45"),
                content=ft.Row(
                    controls=[
                        ft.TextField(
                            expand=True,
                            bgcolor="black12",
                            label="Search",
                            # icon=ft.Icons.ACCOUNT_CIRCLE_ROUNDED,
                            hint_text="Fill correct data",
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
                            content=ft.Icon(name="search"),
                        ),
                    ],
                ),
            ),
            "date_banner": ft.Container(
                # height=80,
                padding=ft.padding.only(left=12, top=18, right=12, bottom=18),
                border_radius=ft.border_radius.all(18),
                bgcolor=ft.Colors("black45"),
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
            ),
            "cloud_barnner": ft.Container(
                # height=80,
                padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
                border_radius=ft.border_radius.all(12),
                bgcolor=ft.Colors("black45"),
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
                                ft.Icon(name="cloud_rounded"),
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
            ),
            "upload_buttom": ft.Container(
                expand=True,
                padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
                border_radius=ft.border_radius.all(12),
                bgcolor=ft.Colors("black45"),
                content=ft.Row(
                    controls=[
                        ft.Icon(name="add_a_photo_rounded"),
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
            ),
            "buttom_left": ft.Container(
                expand=True,
                padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
                border_radius=ft.border_radius.all(12),
                width=220,
                bgcolor=ft.Colors("black45"),
                content=ft.Row(
                    controls=[
                        ft.Icon(name="navigate_next_rounded"),
                        ft.Text(
                            "Get Start",
                            size=14,
                            color=ft.Colors("grey"),
                            weight="bold",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            "buttom_right": ft.Container(
                expand=True,
                padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
                width=220,
                border_radius=ft.border_radius.all(12),
                bgcolor=ft.Colors("black45"),
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "Get Start",
                            size=14,
                            color=ft.Colors("grey"),
                            weight="bold",
                        ),
                        ft.Icon(name="navigate_next_rounded"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            "horizontal_bar": ft.Container(
                # height=80,
                padding=ft.padding.only(left=0, top=8, right=0, bottom=8),
                border_radius=ft.border_radius.all(12),
                bgcolor=ft.Colors("grey900"),
                content=ft.Row(
                    height=32,
                    # height=200,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    # spacing=16,
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
                                    ft.Icon(
                                        name="account_balance_wallet", color="cyan"
                                    ),
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
                                    ft.Icon(name="bar_chart_rounded", color="cyan"),
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
                                    ft.Icon(name="six_ft_apart_rounded", color="cyan"),
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
                                    ft.Icon(
                                        name="flip_camera_android_rounded", color="cyan"
                                    ),
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
                                    ft.Icon(
                                        name="currency_bitcoin_rounded", color="cyan"
                                    ),
                                    ft.Text(
                                        value="Yield",
                                        size=8,
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ),
            "vertical_bar": ft.Container(
                # height=80,
                padding=ft.padding.only(left=8, top=18, right=8, bottom=16),
                border_radius=ft.border_radius.all(12),
                bgcolor=ft.Colors("grey900"),
                content=ft.Column(
                    width=32,
                    # height=200,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    # spacing=16,
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
                                    ft.Icon(
                                        name="account_balance_wallet", color="cyan"
                                    ),
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
                                    ft.Icon(name="bar_chart_rounded", color="cyan"),
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
                                    ft.Icon(name="six_ft_apart_rounded", color="cyan"),
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
                                    ft.Icon(
                                        name="flip_camera_android_rounded", color="cyan"
                                    ),
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
                                    ft.Icon(
                                        name="currency_bitcoin_rounded", color="cyan"
                                    ),
                                    ft.Text(
                                        value="Yield",
                                        size=8,
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ),
            "enter pin": ft.Container(
                # height=80,
                padding=ft.padding.only(left=8, top=18, right=8, bottom=16),
                border_radius=ft.border_radius.all(24),
                bgcolor=ft.Colors("black54"),
                content=ft.Column(
                    width=280,
                    # height=200,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    # spacing=16,
                    run_spacing=12,
                    controls=[
                        ft.Container(
                            #: [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                            # tooltip='Container',
                            padding=ft.padding.only(left=8, right=8, bottom=0, top=0),
                            # border_radius=ft.border_radius.only(top_left=8, top_right=8, bottom_left=8, bottom_right=8),
                            # border=ft.border.all(width=2, color=ft.colors('black12')),
                            # gradient=ft.LinearGradient(begin=ft.alignment.top_center, end=ft.alignment.bottom_center,colors=[ft.colors('transparent'), ft.colors('black12'),],),
                            # shadow=ft.BoxShadow(spread_radius=1, blur_radius =15, color=ft.colors('bluegrey300'), offset=ft.Offset(0,0), blur_style=ft.ShadowBlurStyle.OUTER,),
                            # height=150,
                            # width=150,
                            # ink=True,
                            ink_color=ft.colors("yellow"),
                            expand=True,
                            alignment=ft.alignment.center_left,
                            content=ft.IconButton(
                                icon="navigate_before_rounded",
                                bgcolor="black12",
                                icon_color="red",
                            ),
                            # on_click=lambda tmp_widget: print(tmp_widget.controls),
                            # on_hover=lambda tmp_widget: print(tmp_widget.controls),
                            # on_long_press=lambda tmp_widget: print(tmp_widget.controls),
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
                            padding=ft.padding.only(
                                left=12, top=12, right=12, bottom=12
                            ),
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
                                    ft.Icon(name="navigate_next_rounded"),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ),
                    ],
                ),
            ),
            "offer_card": ft.Container(
                expand=True,
                padding=ft.padding.only(left=12, top=12, right=12, bottom=12),
                border_radius=ft.border_radius.all(12),
                width=340,
                bgcolor=ft.Colors("bluegrey900"),
                image=ft.DecorationImage(
                    src="Ebay icon.png",
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
                                    bgcolor=ft.Colors("black45"),
                                    content=ft.Text(
                                        value="Buy Now ",
                                        size=11,
                                        color=ft.Colors("white70"),
                                    ),
                                ),
                            ],
                            spacing=2,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                        ),
                        ft.Image(
                            src=self.image,
                            width=100,
                            height=100,
                            fit=ft.ImageFit.COVER,
                            border_radius=ft.border_radius.all(32),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            "verify_password": ft.Container(
                # height=80,
                padding=ft.padding.only(left=12, top=16, right=12, bottom=16),
                border_radius=ft.border_radius.all(24),
                bgcolor=ft.Colors("grey900"),
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
                            # height=80,
                            padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
                            border_radius=ft.border_radius.all(24),
                            expand=True,
                            # bgcolor=ft.Colors("black45"),
                            content=ft.TextField(
                                expand=True,
                                bgcolor="black12",
                                label="Password",
                                # icon=ft.Icons.ACCOUNT_CIRCLE_ROUNDED,
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
                                    padding=ft.padding.only(
                                        left=12, top=8, right=12, bottom=8
                                    ),
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
                                    padding=ft.padding.only(
                                        left=12, top=8, right=12, bottom=8
                                    ),
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
            ),
            "offer_left_card": ft.Container(
                expand=True,
                padding=ft.padding.only(left=12, top=12, right=12, bottom=12),
                border_radius=ft.border_radius.all(12),
                width=340,
                bgcolor=ft.Colors("bluegrey900"),
                image=ft.DecorationImage(
                    src="Ebay icon.png",
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
                            bgcolor=ft.Colors("black45"),
                            content=ft.Text(
                                value="Buy Now ",
                                size=11,
                                color=ft.Colors("white70"),
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            "temperature_button": ft.Container(
                # height=80,
                padding=ft.padding.only(left=12, top=16, right=12, bottom=16),
                border_radius=ft.border_radius.all(24),
                bgcolor=ft.Colors("grey900"),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    run_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                    run_spacing=12,
                    controls=[
                        ft.Icon(name="ac_unit_rounded"),
                        ft.Text(value="Room", weight="bold", size=10),
                    ],
                ),
            ),
            "temperature_card": ft.Container(
                padding=ft.padding.only(left=12, top=8, right=12, bottom=8),
                width=160,
                border_radius=ft.border_radius.all(12),
                bgcolor=ft.Colors("bluegrey900"),
                height=200,
                image=ft.DecorationImage(
                    src="Ebay icon.png",
                    fit="cover",
                    opacity=0.18,
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
                                        ft.Icon(name="water_drop_rounded"),
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
                                        ft.Switch(value=False),
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
            ),
            "ubication_car": ft.Container(
                # height=80,
                padding=ft.padding.only(left=14, top=14, right=14, bottom=14),
                border_radius=ft.border_radius.all(24),
                bgcolor=ft.Colors("black45"),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    run_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                    run_spacing=12,
                    controls=[
                        ft.Container(
                            bgcolor="red",
                            border_radius=ft.border_radius.all(24),
                            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
                            # width=240,
                            height=200,
                            expand=True,
                            image=ft.DecorationImage(
                                src=self.image,
                                fit=ft.ImageFit.COVER,
                                opacity=0.8,
                            ),
                            content=ft.Column(
                                spacing=8,
                                run_spacing=8,
                                controls=[
                                    ft.IconButton(
                                        icon="favorite",
                                        bgcolor="black45",
                                        icon_color="red",
                                    ),
                                    ft.Container(),
                                ],
                            ),
                        ),
                        ft.Container(
                            padding=ft.padding.only(left=4, top=8, right=4, bottom=8),
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
                                        "Flet is a framework that allows building web, desktop and mobile applications in Python.",
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
            ),
            "iphone_sales_card": ft.Container(
                width=300,
                height=250,
                border_radius=10,
                bgcolor=ft.Colors("white"),
                image=ft.DecorationImage(
                    src="apple.png",
                    fit="cover",
                    opacity=0.18,
                ),
                padding=ft.padding.all(10),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors("black38"),
                    offset=ft.Offset(0, 5),
                ),
                content=ft.Column(
                    controls=[
                        # iPhone Image
                        ft.Image(
                            src=self.image,
                            width=300,
                            height=150,
                            fit=ft.ImageFit.COVER,
                            border_radius=ft.border_radius.only(
                                top_left=10, top_right=10
                            ),
                        ),
                        # iPhone Model
                        ft.Text(
                            "iPhone 15 Pro",
                            size=18,
                            weight="bold",
                            color=ft.Colors("black87"),
                        ),
                        # Price
                        ft.Text(
                            "$999", size=16, color=ft.Colors("blue"), weight="bold"
                        ),
                    ],
                    spacing=5,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                ),
            ),
            "tech_conference_card": ft.Container(
                width=300,
                height=200,
                border_radius=10,
                bgcolor=ft.Colors("white"),
                padding=ft.padding.all(20),
                image=ft.DecorationImage(
                    src="apple.png",
                    fit="cover",
                    opacity=0.18,
                ),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors("black38"),
                    offset=ft.Offset(0, 5),
                ),
                content=ft.Column(
                    controls=[
                        # Conference Name
                        ft.Text(
                            "Tech Summit 2024",
                            size=20,
                            weight="bold",
                            color=ft.Colors("black87"),
                        ),
                        # Date
                        ft.Text(
                            "October 10-12, 2024", size=14, color=ft.Colors("grey")
                        ),
                        # Location
                        ft.Text("San Francisco, CA", size=14, color=ft.Colors("grey")),
                    ],
                    spacing=5,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            "hotel_booking_card": ft.Container(
                width=300,
                height=200,
                border_radius=10,
                bgcolor=ft.Colors("white"),
                padding=ft.padding.all(10),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors("black38"),
                    offset=ft.Offset(0, 5),
                ),
                image=ft.DecorationImage(
                    src="apple.png",
                    fit="cover",
                    opacity=0.18,
                ),
                content=ft.Column(
                    controls=[
                        # Hotel Image
                        ft.Image(
                            src=self.image,
                            width=300,
                            height=150,
                            fit=ft.ImageFit.COVER,
                            border_radius=ft.border_radius.only(
                                top_left=10, top_right=10
                            ),
                        ),
                        # Hotel Name
                        ft.Text(
                            "Luxury Resort",
                            size=18,
                            weight="bold",
                            color=ft.Colors("black87"),
                        ),
                        # Location
                        ft.Text("Maldives", size=14, color=ft.Colors("grey")),
                        # Price
                        ft.Text(
                            "$299/night",
                            size=16,
                            color=ft.Colors("blue"),
                            weight="bold",
                        ),
                    ],
                    spacing=5,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                ),
            ),
            # 9. Event Ticket Card
            "event_ticket_card": ft.Container(
                width=300,
                # height=150,
                border_radius=10,
                bgcolor=ft.Colors("white"),
                padding=ft.padding.only(left=8, top=8, right=8, bottom=18),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors("black38"),
                    offset=ft.Offset(0, 5),
                ),
                image=ft.DecorationImage(
                    src="apple.png",
                    fit="cover",
                    opacity=0.18,
                ),
                content=ft.Column(
                    controls=[
                        ft.Image(
                            src=self.image,
                            width=300,
                            height=150,
                            fit=ft.ImageFit.COVER,
                            border_radius=ft.border_radius.only(
                                top_left=10,
                                top_right=10,
                                bottom_left=10,
                                bottom_right=10,
                            ),
                        ),
                        # Event Name
                        ft.Text(
                            "Music Festival 2024",
                            size=20,
                            weight="bold",
                            color=ft.Colors("black87"),
                        ),
                        # Date
                        ft.Text("June 15, 2024", size=14, color=ft.Colors("grey600")),
                        # Price
                        ft.Text(
                            "$99.99", size=16, color=ft.Colors("blue600"), weight="bold"
                        ),
                    ],
                    spacing=5,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                ),
            ),
            "fill_formulary": ft.Container(
                # height=80,
                padding=ft.padding.only(left=8, top=16, right=8, bottom=16),
                border_radius=ft.border_radius.all(24),
                bgcolor=ft.Colors("grey900"),
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
                            # height=80,
                            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
                            border_radius=ft.border_radius.all(24),
                            expand=True,
                            # bgcolor=ft.Colors("black45"),
                            content=ft.TextField(
                                expand=True,
                                bgcolor="black12",
                                label="Username",
                                # icon=ft.Icons.ACCOUNT_CIRCLE_ROUNDED,
                                hint_text="Fill correct data",
                                border_width=0,
                                border_radius=ft.border_radius.all(18),
                            ),
                        ),
                        ft.Container(
                            # height=80,
                            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
                            border_radius=ft.border_radius.all(24),
                            expand=True,
                            # bgcolor=ft.Colors("black45"),
                            content=ft.TextField(
                                expand=True,
                                bgcolor="black12",
                                label="Email",
                                # icon=ft.Icons.ACCOUNT_CIRCLE_ROUNDED,
                                hint_text="Fill correct data",
                                border_width=0,
                                border_radius=ft.border_radius.all(18),
                            ),
                        ),
                        ft.Container(
                            # height=80,
                            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
                            border_radius=ft.border_radius.all(24),
                            expand=True,
                            # bgcolor=ft.Colors("black45"),
                            content=ft.TextField(
                                expand=True,
                                bgcolor="black12",
                                label="Password",
                                # icon=ft.Icons.ACCOUNT_CIRCLE_ROUNDED,
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
                            # bgcolor=ft.Colors("black45"),
                            content=ft.TextField(
                                expand=True,
                                bgcolor="black12",
                                label="Repeat password",
                                # icon=ft.Icons.ACCOUNT_CIRCLE_ROUNDED,
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
                                        # label="Select RadioGroup",
                                        # label_position=ft.LabelPosition.RIGHT,
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
                                        # width=200,
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
            ),
            "travel_card": ft.Container(
                # height=80,
                padding=ft.padding.only(left=16, top=16, right=16, bottom=16),
                border_radius=ft.border_radius.all(24),
                bgcolor=ft.Colors("black45"),
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
                                    content=ft.Icon(name="navigate_next_rounded"),
                                ),
                            ],
                        ),
                        ft.RadioGroup(
                            # label="Select RadioGroup",
                            # label_position=ft.LabelPosition.RIGHT,
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
                            padding=ft.padding.only(
                                left=14, top=14, right=14, bottom=14
                            ),
                            border_radius=ft.border_radius.all(18),
                            # width=220,
                            bgcolor=ft.Colors.with_opacity(
                                opacity=0.4,
                                color=ft.Colors("blue900"),
                            ),
                            content=ft.Row(
                                controls=[
                                    ft.Icon(name="navigate_next_rounded"),
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
            ),
            "brand_showcase_card": ft.Container(
                width=300,
                height=200,
                border_radius=10,
                padding=ft.padding.all(20),
                bgcolor=ft.Colors("white"),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors("black38"),
                    offset=ft.Offset(0, 5),
                ),
                image=ft.DecorationImage(
                    src="image_avatar.png",
                    fit="cover",
                    opacity=0.3,
                ),
                content=ft.Column(
                    controls=[
                        # Brand Name
                        ft.Text(
                            "World Famous Brands",
                            size=20,
                            weight="bold",
                            color=ft.Colors("black87"),
                        ),
                        # Description
                        ft.Text(
                            "More Than 45 Brands", size=14, color=ft.Colors("grey600")
                        ),
                        # Price and Discount
                        ft.Row(
                            controls=[
                                ft.Text(
                                    "$49.00",
                                    size=16,
                                    color=ft.Colors("grey600"),
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(
                                    "$19.00",
                                    size=16,
                                    color=ft.Colors("red600"),
                                    weight=ft.FontWeight.BOLD,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=5,
                        ),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            # 4. Business Card
            "business_card": ft.Container(
                width=300,
                height=150,
                border_radius=10,
                padding=ft.padding.all(20),
                bgcolor=ft.Colors("white"),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors("black38"),
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
                            size=20,
                            weight="bold",
                            color=ft.Colors("black87"),
                        ),
                        # Contact Info
                        ft.Text(
                            value="Email: info@techsolutions.com",
                            size=14,
                            color=ft.Colors("grey600"),
                        ),
                        ft.Text(
                            value="Phone: +1 234 567 890",
                            size=14,
                            color=ft.Colors("grey600"),
                            weight="bold",
                        ),
                    ],
                    spacing=5,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            # CUSTOM WIDGETS
            "Custom Card": ft.Card(
                elevation=12,
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.ALBUM),
                                title=ft.Text("The Enchanted Nightingale"),
                                subtitle=ft.Text(
                                    "Music by Julie Gable. Lyrics by Sidney Stein."
                                ),
                            ),
                            ft.Row(
                                [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                        ]
                    ),
                    width=400,
                    padding=10,
                ),
            ),
            "Custom Dismissible": ft.ListView(
                expand=True,
                controls=[
                    ft.Dismissible(
                        content=ft.ListTile(title=ft.Text(f"Item {i}")),
                        dismiss_direction=ft.DismissDirection.HORIZONTAL,
                        # background=ft.Container(bgcolor=ft.Colors("green")),
                        secondary_background=ft.Container(bgcolor=ft.Colors("red")),
                        # on_dismiss=handle_dismiss,
                        # on_update=handle_update,
                        # on_confirm_dismiss=handle_confirm_dismiss,
                        dismiss_thresholds={
                            ft.DismissDirection.END_TO_START: 0.2,
                            ft.DismissDirection.START_TO_END: 0.2,
                        },
                    )
                    for i in range(5)
                ],
            ),
            # DIVIDERS
            "Divider": ft.Divider(
                height=1,
                color=ft.Colors.with_opacity(
                    opacity=0.2,
                    color=ft.Colors("white"),
                ),
                thickness=3,
            ),
            # TABS
            "Tabs": ft.Tabs(height=450, tabs=[]),
            "Tab": ft.Tab(
                text="Tab 1",
                content=ft.Container(
                    bgcolor="white12",
                    content=ft.Column(),
                ),
            ),
            # NAVIGATIONS
            "NavigationRail": ft.Row(
                controls=[
                    ft.NavigationRail(
                        height=800,
                        selected_index=0,
                        label_type=ft.NavigationRailLabelType.ALL,
                        extended=True,
                        min_width=50,
                        min_extended_width=100,
                        leading=ft.FloatingActionButton(
                            icon=ft.Icons.CREATE, text="Add"
                        ),
                        group_alignment=-0.9,
                        destinations=[
                            ft.NavigationRailDestination(
                                icon=ft.Icons.FAVORITE_BORDER,
                                selected_icon=ft.Icons.FAVORITE,
                                label="First",
                            ),
                            ft.NavigationRailDestination(
                                icon=ft.Icon(ft.Icons.BOOKMARK_BORDER),
                                selected_icon=ft.Icon(ft.Icons.BOOKMARK),
                                label="Second",
                            ),
                            ft.NavigationRailDestination(
                                icon=ft.Icons.SETTINGS_OUTLINED,
                                selected_icon=ft.Icon(ft.Icons.SETTINGS),
                                label_content=ft.Text("Settings"),
                            ),
                        ],
                        # on_change=lambda e: print(
                        #     "Selected destination:", e.control.selected_index
                        # ),
                    ),
                ]
            ),
            # LAYOUTS
            "Card": ft.Card(
                elevation=12,
                content=ft.Container(),
            ),
            "Column": ft.Column(),
            "Container": ft.Container(),
            "GridView": ft.GridView(
                runs_count=2,
                run_spacing=4,
                padding=ft.padding.all(6),
            ),
            "ListView": ft.ListView(),
            "ResponsiveRow": ft.ResponsiveRow(),
            "Row": ft.Row(),
            "Stack": ft.Stack(),
            # BUTTONS
            "Button": ft.Button(
                text="hello world dev",
            ),
            "ElevatedButton": ft.ElevatedButton(
                text="hello world dev",
            ),
            "FilledButton": ft.FilledButton(
                text="hello world dev",
            ),
            "FilledTonalButton": ft.FilledTonalButton(
                text="hello world dev",
            ),
            "FloatingActionButton": ft.FloatingActionButton(
                icon=ft.Icons.FAVORITE,
            ),
            "IconButton": ft.IconButton(
                icon=ft.Icons.FAVORITE,
            ),
            "Icon": ft.Icon(
                name=ft.Icons.FAVORITE,
            ),
            "OutlinedButton": ft.OutlinedButton(
                text="hello world dev",
            ),
            # CONTROLS
            "MenuItemButton": ft.MenuBar(
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("BgColors"),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Blue"),
                                leading=ft.Icon(ft.Icons.COLORIZE),
                                style=ft.ButtonStyle(
                                    bgcolor={ft.ControlState.HOVERED: ft.Colors("blue")}
                                ),
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Green"),
                                leading=ft.Icon(ft.Icons.COLORIZE),
                                style=ft.ButtonStyle(
                                    bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN}
                                ),
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Red"),
                                leading=ft.Icon(ft.Icons.COLORIZE),
                                style=ft.ButtonStyle(
                                    bgcolor={ft.ControlState.HOVERED: ft.Colors.RED}
                                ),
                            ),
                        ],
                    ),
                ]
            ),
            "SubmenuButton": ft.MenuBar(
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("BgColors"),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Blue"),
                                leading=ft.Icon(ft.Icons.COLORIZE),
                                style=ft.ButtonStyle(
                                    bgcolor={ft.ControlState.HOVERED: ft.Colors("blue")}
                                ),
                                # on_click=lambda e: print("MenuItemButton clicked!"),
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Green"),
                                leading=ft.Icon(ft.Icons.COLORIZE),
                                style=ft.ButtonStyle(
                                    bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN}
                                ),
                                # on_click=lambda e: print("MenuItemButton clicked!"),
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Red"),
                                leading=ft.Icon(ft.Icons.COLORIZE),
                                style=ft.ButtonStyle(
                                    bgcolor={ft.ControlState.HOVERED: ft.Colors.RED}
                                ),
                                # on_click=lambda e: print("MenuItemButton clicked!"),
                            ),
                        ],
                    ),
                ]
            ),
            "SegmentedButton": ft.SegmentedButton(
                expand=True,
                on_change=lambda e: print("MenuItemButton clicked!"),
                selected_icon=ft.Icon(ft.Icons.ONETWOTHREE),
                selected={"1", "4"},
                allow_multiple_selection=True,
                segments=[
                    ft.Segment(
                        value="1",
                        label=ft.Text("1"),
                        icon=ft.Icon(ft.Icons.LOOKS_ONE),
                    ),
                    ft.Segment(
                        value="2",
                        label=ft.Text("2"),
                        icon=ft.Icon(ft.Icons.LOOKS_TWO),
                    ),
                    ft.Segment(
                        value="3",
                        label=ft.Text("3"),
                        icon=ft.Icon(ft.Icons.LOOKS_3),
                    ),
                    ft.Segment(
                        value="4",
                        label=ft.Text("4"),
                        icon=ft.Icon(ft.Icons.LOOKS_4),
                    ),
                ],
            ),
            "TextButton": ft.TextButton(text="hello world dev"),
            "CupertinoTimerPicker": ft.CupertinoTimerPicker(
                value=3600,
                second_interval=10,
                minute_interval=1,
                mode=ft.CupertinoTimerPickerMode.HOUR_MINUTE_SECONDS,
                # on_change=handle_timer_picker_change,
            ),
            # CONTENT
            "PopupMenuButton": ft.PopupMenuButton(
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.HOURGLASS_TOP_OUTLINED),
                        ft.Text("Item with a custom content"),
                    ]
                ),
            ),
            # CUPERTINO CONTENT
            "CupertinoFilledButton": ft.CupertinoFilledButton(
                opacity_on_click=0.3,
                content=ft.Text("CupertinoFilled"),
                # on_click = event_manager
            ),
            # CUPERTINO CONTROLS
            "CupertinoButton": ft.CupertinoButton(
                text="hello world dev",
            ),
            "CupertinoSegmentedButton": ft.CupertinoSegmentedButton(
                expand=True,
                on_change=lambda e: print("MenuItemButton clicked!"),
                selected_color=ft.Colors.RED,
                selected_index=0,
                controls=[
                    ft.Text("One"),
                    ft.Container(
                        padding=ft.padding.symmetric(0, 30),
                        content=ft.Text("Two"),
                    ),
                    ft.Container(
                        padding=ft.padding.symmetric(0, 10),
                        content=ft.Text("Three"),
                    ),
                ],
            ),
            "CupertinoSlidingSegmentedButton": ft.CupertinoSlidingSegmentedButton(
                expand=True,
                selected_index=0,
                thumb_color=ft.Colors("blue"),
                padding=ft.padding.symmetric(0, 10),
                controls=[
                    ft.Text("One"),
                    ft.Text("Two"),
                    ft.Text("Three"),
                ],
            ),
            "CupertinoContextMenu": ft.CupertinoContextMenu(
                enable_haptic_feedback=True,
                # expand=True,
                content=ft.Image(
                    "splash.jpg",
                    width=100,
                    height=100,
                ),
                actions=[
                    ft.CupertinoContextMenuAction(
                        text="Action 1",
                        is_default_action=True,
                        trailing_icon=ft.Icons.CHECK,
                        # on_click=lambda e: print("Action 1"),
                    ),
                    ft.CupertinoContextMenuAction(
                        text="Action 2",
                        trailing_icon=ft.Icons.MORE,
                        # on_click=lambda e: print("Action 2"),
                    ),
                    ft.CupertinoContextMenuAction(
                        text="Action 3",
                        is_destructive_action=True,
                        trailing_icon=ft.Icons.CANCEL,
                        # on_click=lambda e: print("Action 3"),
                    ),
                ],
            ),
            "CupertinoActionSheet": ft.CupertinoActionSheet(
                title=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Title"),
                    ],
                ),
                message=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Description"),
                    ],
                ),
                cancel=ft.CupertinoActionSheetAction(
                    content=ft.Text("Cancel"),
                ),
                actions=[
                    ft.CupertinoActionSheetAction(
                        content=ft.Text("Default Action"),
                        is_default_action=True,
                        # on_click=lambda e: print("Action 3"),
                    ),
                    ft.CupertinoActionSheetAction(
                        content=ft.Text("Normal Action"),
                        # on_click=lambda e: print("Action 3"),
                    ),
                    ft.CupertinoActionSheetAction(
                        content=ft.Text("Destructive Action"),
                        is_destructive_action=True,
                        # on_click=lambda e: print("Action 3"),
                    ),
                ],
            ),
            # ALERTS
            "DatePicker": ft.ElevatedButton(
                text="Pick date",
                icon=ft.Icons.CALENDAR_MONTH,
                on_click=lambda e: self.page.open(
                    ft.DatePicker(
                        first_date=datetime.datetime(year=2023, month=10, day=1),
                        last_date=datetime.datetime(year=2024, month=10, day=1),
                        # on_change=handle_change,
                        # on_dismiss=handle_dismissal,
                    )
                ),
            ),
            "TimePicker": ft.ElevatedButton(
                text="Pick time",
                icon=ft.Icons.ACCESS_TIME_FILLED_ROUNDED,
                on_click=lambda e: self.page.open(
                    ft.TimePicker(
                        confirm_text="Confirm",
                        error_invalid_text="Time out of range",
                        help_text="Pick your time slot",
                        # on_change=handle_change,
                        # on_dismiss=handle_dismissal,
                        # on_entry_mode_change=handle_entry_mode_change,
                    )
                ),
            ),
            "AlertDialog": ft.ElevatedButton(
                text="Alert Dialog",
                icon=ft.Icons.ADD_ALERT_ROUNDED,
                on_click=lambda e: self.page.open(self.alert_dialog),
            ),
            "Banner": ft.ElevatedButton(
                text="Alert Barner",
                icon=ft.Icons.ADD_ALERT_ROUNDED,
                on_click=lambda e: self.page.open(self.alert_barner),
            ),
            # TEXT
            "CupertinoTextField": ft.CupertinoTextField(
                placeholder_text="Placeholder", bgcolor=ft.Colors("black12")
            ),
            "Markdown": ft.Markdown(
                selectable=True,
                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                value=md1,
            ),
            "Text": ft.Text(
                value="Size 15, Normal",
                size=15,
                color=ft.Colors("white"),
                bgcolor=ft.Colors.ORANGE_800,
                weight=ft.FontWeight.NORMAL,
            ),
            "TextField": ft.TextField(
                bgcolor="white12",
                label="TextField with icon",
                icon=ft.Icons.ACCOUNT_CIRCLE_ROUNDED,
                hint_text="Fill correct data",
                border_radius=ft.border_radius.all(12),
            ),
            # IMAGE
            "Image": ft.Image(
                src="logo.png",
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            ),
            "Same Image": same_image,
            "CircleAvatar": ft.Stack(
                width=40,
                height=40,
                controls=[
                    ft.CircleAvatar(foreground_image_src=".my_avatar.png"),
                    ft.Container(
                        content=ft.CircleAvatar(bgcolor=ft.Colors.YELLOW, radius=5),
                        alignment=ft.alignment.bottom_left,
                    ),
                ],
            ),
            # SELECTION
            "AnimatedSwitcher": self.animated_switcher,
            "Checkbox": ft.Checkbox(
                label="Normal Checkbox",
                label_position=ft.LabelPosition.RIGHT,
                value=False,
            ),
            "Dropdown": ft.Dropdown(
                label="Select Dropdown",
                # label_position=ft.LabelPosition.RIGHT,
                value="Dropdown",
                options=[
                    ft.dropdown.Option("Red"),
                    ft.dropdown.Option("Green"),
                    ft.dropdown.Option("Blue"),
                ],
            ),
            "RadioGroup": ft.RadioGroup(
                # label="Select RadioGroup",
                # label_position=ft.LabelPosition.RIGHT,
                value="RadioGroup",
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    run_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                    spacing=8,
                    run_spacing=8,
                    controls=[
                        ft.Radio(value="red", label="Red"),
                        ft.Radio(value="green", label="Green"),
                        ft.Radio(value="blue", label="Blue"),
                    ],
                ),
            ),
            "RangeSlider": ft.RangeSlider(
                label="Range Slider",
                min=0,
                max=50,
                divisions=10,
                start_value=10,
                end_value=20,
                inactive_color=ft.Colors("black12"),
                active_color=ft.Colors("blue"),
                overlay_color=ft.Colors.YELLOW,
            ),
            "Slider": ft.Slider(
                label="Range Slider",
                min=0,
                max=50,
                divisions=10,
                # start_value=10,
                # end_value=20,
                inactive_color=ft.Colors("black12"),
                active_color=ft.Colors("blue"),
                overlay_color=ft.Colors.YELLOW,
            ),
            "Switch": ft.Switch(label="Switch", value=False),
            # CUPERTINO SELECTION
            "CupertinoCheckbox": ft.CupertinoCheckbox(
                label="Cupertino Checkbox",
                label_position=ft.LabelPosition.RIGHT,
                value=False,
            ),
            "CupertinoSlider": ft.CupertinoSlider(
                min=0,
                max=50,
                divisions=10,
            ),
            "CupertinoSwitch": ft.CupertinoSwitch(
                label="Cupertino Switch",
                value=True,
            ),
            # PROGRESS
            "ProgressBar": ft.ProgressBar(
                width=400, color=ft.Colors("yellow"), bgcolor=ft.Colors("black12")
            ),
            "ProgressRing": ft.ProgressRing(
                width=16,
                height=16,
                stroke_width=2,
                color=ft.Colors("yellow"),
                bgcolor=ft.Colors("black12"),
            ),
            # CHARTS
            "BarChart": ft.BarChart(
                tooltip_bgcolor=ft.Colors.with_opacity(0.5, ft.Colors("grey300")),
                max_y=110,
                interactive=True,
                border=ft.border.all(1, ft.Colors("grey400")),
                expand=True,
                horizontal_grid_lines=ft.ChartGridLines(
                    color=ft.Colors("grey300"), width=1, dash_pattern=[3, 3]
                ),
                bar_groups=[
                    ft.BarChartGroup(
                        x=0,
                        bar_rods=[
                            ft.BarChartRod(
                                from_y=0,
                                to_y=40,
                                width=40,
                                color=ft.Colors("amber"),
                                tooltip="Apple",
                                border_radius=0,
                            ),
                        ],
                    ),
                    ft.BarChartGroup(
                        x=1,
                        bar_rods=[
                            ft.BarChartRod(
                                from_y=0,
                                to_y=100,
                                width=40,
                                color=ft.Colors("blue"),
                                tooltip="Blueberry",
                                border_radius=0,
                            ),
                        ],
                    ),
                    ft.BarChartGroup(
                        x=2,
                        bar_rods=[
                            ft.BarChartRod(
                                from_y=0,
                                to_y=30,
                                width=40,
                                color=ft.Colors.RED,
                                tooltip="Cherry",
                                border_radius=0,
                            ),
                        ],
                    ),
                    ft.BarChartGroup(
                        x=3,
                        bar_rods=[
                            ft.BarChartRod(
                                from_y=0,
                                to_y=60,
                                width=40,
                                color=ft.Colors.ORANGE,
                                tooltip="Orange",
                                border_radius=0,
                            ),
                        ],
                    ),
                ],
                left_axis=ft.ChartAxis(
                    labels_size=40, title=ft.Text("Fruit supply"), title_size=40
                ),
                bottom_axis=ft.ChartAxis(
                    labels=[
                        ft.ChartAxisLabel(
                            value=0, label=ft.Container(ft.Text("Apple"), padding=10)
                        ),
                        ft.ChartAxisLabel(
                            value=1,
                            label=ft.Container(ft.Text("Blueberry"), padding=10),
                        ),
                        ft.ChartAxisLabel(
                            value=2, label=ft.Container(ft.Text("Cherry"), padding=10)
                        ),
                        ft.ChartAxisLabel(
                            value=3, label=ft.Container(ft.Text("Orange"), padding=10)
                        ),
                    ],
                    labels_size=40,
                ),
            ),
            "LineChart": ft.LineChart(
                tooltip_bgcolor=ft.Colors.with_opacity(0.8, ft.Colors("bluegrey")),
                min_y=0,
                max_y=4,
                min_x=0,
                max_x=14,
                expand=True,
                border=ft.Border(
                    bottom=ft.BorderSide(
                        4, ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE)
                    )
                ),
                left_axis=ft.ChartAxis(
                    labels=[
                        ft.ChartAxisLabel(
                            value=1,
                            label=ft.Text("1m", size=14, weight=ft.FontWeight.BOLD),
                        ),
                        ft.ChartAxisLabel(
                            value=2,
                            label=ft.Text("2m", size=14, weight=ft.FontWeight.BOLD),
                        ),
                        ft.ChartAxisLabel(
                            value=3,
                            label=ft.Text("3m", size=14, weight=ft.FontWeight.BOLD),
                        ),
                        ft.ChartAxisLabel(
                            value=4,
                            label=ft.Text("4m", size=14, weight=ft.FontWeight.BOLD),
                        ),
                        ft.ChartAxisLabel(
                            value=5,
                            label=ft.Text("5m", size=14, weight=ft.FontWeight.BOLD),
                        ),
                        ft.ChartAxisLabel(
                            value=6,
                            label=ft.Text("6m", size=14, weight=ft.FontWeight.BOLD),
                        ),
                    ],
                    labels_size=40,
                ),
                data_series=data_1,
                bottom_axis=ft.ChartAxis(
                    labels=[
                        ft.ChartAxisLabel(
                            value=2,
                            label=ft.Container(
                                ft.Text(
                                    "SEP",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.with_opacity(
                                        0.5, ft.Colors.ON_SURFACE
                                    ),
                                ),
                                margin=ft.margin.only(top=10),
                            ),
                        ),
                        ft.ChartAxisLabel(
                            value=7,
                            label=ft.Container(
                                ft.Text(
                                    "OCT",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.with_opacity(
                                        0.5, ft.Colors.ON_SURFACE
                                    ),
                                ),
                                margin=ft.margin.only(top=10),
                            ),
                        ),
                        ft.ChartAxisLabel(
                            value=12,
                            label=ft.Container(
                                ft.Text(
                                    "DEC",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.with_opacity(
                                        0.5, ft.Colors.ON_SURFACE
                                    ),
                                ),
                                margin=ft.margin.only(top=10),
                            ),
                        ),
                    ],
                    labels_size=32,
                ),
            ),
            "LineChartData": ft.LineChartData(),
            "LineChartDataPoint": ft.LineChartDataPoint(),
            "PieChart": ft.PieChart(
                sections_space=1,
                center_space_radius=0,
                expand=True,
                # hovered_border = ft.BorderSide(6, ft.Colors("white"))
                # on_chart_event = lambda _: print(_)
                sections=[
                    ft.PieChartSection(
                        25,
                        color=ft.Colors("blue"),
                        radius=80,
                        border_side=ft.BorderSide(
                            0, ft.Colors.with_opacity(0, ft.Colors("white"))
                        ),
                    ),
                    ft.PieChartSection(
                        25,
                        color=ft.Colors.YELLOW,
                        radius=65,
                        border_side=ft.BorderSide(
                            0, ft.Colors.with_opacity(0, ft.Colors("white"))
                        ),
                    ),
                    ft.PieChartSection(
                        25,
                        color=ft.Colors.PINK,
                        radius=60,
                        border_side=ft.BorderSide(
                            0, ft.Colors.with_opacity(0, ft.Colors("white"))
                        ),
                    ),
                    ft.PieChartSection(
                        25,
                        color=ft.Colors.GREEN,
                        radius=70,
                        border_side=ft.BorderSide(
                            0, ft.Colors.with_opacity(0, ft.Colors("white"))
                        ),
                    ),
                ],
            ),
            "PieChartSection": ft.PieChartSection(),
            # TABLES
            "DataTable": ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("First name")),
                    ft.DataColumn(ft.Text("Last name")),
                    ft.DataColumn(ft.Text("Age"), numeric=True),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("John")),
                            ft.DataCell(ft.Text("Smith")),
                            ft.DataCell(ft.Text("43")),
                        ],
                    ),
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("Jack")),
                            ft.DataCell(ft.Text("Brown")),
                            ft.DataCell(ft.Text("19")),
                        ],
                    ),
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("Alice")),
                            ft.DataCell(ft.Text("Wong")),
                            ft.DataCell(ft.Text("25")),
                        ],
                    ),
                ],
            ),
        }

        for full_categoryes in widgets_by_categories:
            for _ in widgets_by_categories.get(full_categoryes):
                check = self.widgets.get(_, None)
                self.widgets[f"{_}"] = [
                    ft.Container(
                        tooltip=f"{_}",
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.2, color=ft.colors("white")
                        ),
                        padding=ft.padding.all(8),
                        margin=ft.margin.all(0),
                        border=ft.border.all(0, ft.colors("transparent")),
                        ink=True,
                        ink_color="red",
                        on_click=lambda _: self.touch_widget_in_phone(
                            selected_widget=self.infinityDropWidget
                        ),
                        content=check,
                    )
                ]

    def animate(self, widget: object = None):
        self.animated_switcher.content = (
            self.animation_container_2
            if self.animated_switcher.content == self.animation_container_1
            else self.animation_container_1
        )

        self.animated_switcher.update()

    def build(self):
        global numWidget

        session_id = self.page._session_id
        selectWidgetBox = self.page.session.get(session_id)

        print(selectWidgetBox, "<<<<<data <<")
        self.infinityDropWidget = self.widgets.get(selectWidgetBox)
        print(
            f" ID: <<< drag_dropped: [infinity_box_layer_one.py]  number: {numWidget} "
        )

        # MAIN WIDGET THAT WILL BE DROPPED EACH TIME THAT DRAG ACCEPT
        print(self.infinityDropWidget[0].parent)
        self.content = self.infinityDropWidget[0]
        self.on_will_accept = self.drag_will_accept  # Traslate Drop
        self.on_leave = self.drag_leave  # Leafing Drop Line Border
        self.on_accept = lambda widget_passed: self.drag_accept(
            DragTargetEvent=widget_passed
        )

        # INDEX OF WIDGET ADDED
        numWidget += 1

        self.page.session.set("dict_widget", self.widgets)

    def show_text_dragg_selected(self, name_selected: str = "") -> None:
        self.name_selected = name_selected
        self.widget_selected = self.page.session.get("SHOW_TEXT_SELECTED_DRAGG_WIDGET")
        self.draggs_selected = self.page.session.get("SHOW_TEXT_SELECTED_PHONE_WIDGET")

        self.widget_selected.content.controls[1].content.spans[0].text = "None"
        self.draggs_selected.content.controls[1].content.spans[
            0
        ].text = self.name_selected

        self.widget_selected.bgcolor = ft.colors("black12")
        self.draggs_selected.bgcolor = "cyan,0.1"

        self.widget_selected.update()
        self.draggs_selected.update()

    def switch_border_selected(self, selected: object = None):
        selected_widget = self.page.session.get("SELECTED_CONTAINER")

        if not selected_widget == None:
            selected_widget.border = ft.border.all(2, ft.colors("transparent"))
            selected_widget.update()

        selected.border = ft.border.all(2, ft.colors("yellow900"))
        selected.update()

        self.show_text_dragg_selected(
            name_selected=selected.content._get_control_name()
        )

    def set_selected_widget(self, selected):
        self.page.session.set("SELECTED_CONTAINER", selected)

    def set_selected_widget_id(self, selected):
        self.page.session.set("SELECTED_CONTAINER_ID", selected.uid)

    def touch_widget_in_phone(self, selected_widget: object = None):
        # def touch_widget_in_phone(self,listWidget,e: ft.ContainerTapEvent):
        """
        NOTE:

        WE CAPTURE THE CLICK SELECTION_WIDGET SHOWING BORDER COLOR YELLOW

        IF PRESS IN OTHER WIDGET WE COMPARE tmp_list listWidgetUpdate
        IF IS DIFERENT SHOW BLACK COLOR THE PREVIEW SELECT_WIDGET

        NOTE:

        WE PASS TO Build_Editor => self.infinityDropWidget[0] THAT IS CLICKED SELECTION
        Build_Editor.update_widget_attributes(widget_cliked=ft.Container(content=ft.Text()))

        """

        # SWITCH BORDER COLOR IN SELECTED CONTAINER PHONE
        self.selected = selected_widget[0]
        self.page.session.set("cover_widget", self.selected.parent.parent)

        self.switch_border_selected(selected=selected_widget[0])
        self.set_selected_widget(selected=self.selected)
        self.set_selected_widget_id(selected=self.selected)

        print(
            f"[-] {self.selected.tooltip} ID: <<< touch_widget_in_phone: [infinity_box_layer_one.py]"
        )

    def return_new_widget(self, selected_widget: str = str()) -> object:
        """
        return selected widget

        :param      selected_widget:  The selected widget
        :type       selected_widget:  str
        """
        widget_selected = self.widgets.get(selected_widget)
        self.page.update()

        return widget_selected

    def drag_accept(self, DragTargetEvent: object = None) -> object:

        # ROW COLUMN GRIDVIEW
        self.widgetFilter = self.page.session.get("ONLY_CONTROLS_ADDING_IN_APP")

        session_id = self.page._session_id
        selectWidgetBox = self.page.session.get(session_id)

        self.InstanceNewWidget = DragTarget(dataPassed=selectWidgetBox, page=self.page)
        self.right_control = DragTargetEvent.control.content.content._get_control_name()

        if self.right_control in self.widgetFilter:
            self.is_control = (
                DragTargetEvent.control.content.content._get_control_name()
            )

            print(self.is_control, "<++++++++")
            if self.is_control == "tabs":

                self.payload = ft.Container(
                    content=self.widgets.get("column"),
                )

                DragTargetEvent.control.content.content.tabs.append(
                    ft.Tab(text="Tabs", content=self.InstanceNewWidget)
                )

            elif (
                self.is_control == "column"
                or self.is_control == "row"
                or self.is_control == "stack"
                or self.is_control == "responsiverow"
                or self.is_control == "listview"
                or self.is_control == "gridview"
            ):

                DragTargetEvent.control.content.content.controls.append(
                    self.InstanceNewWidget
                )

        else:
            if self.right_control in self.widgetFilter:
                DragTargetEvent.control.content.content.controls.append(
                    self.InstanceNewWidget
                )

            else:
                # SWITCH IF IS CONTENT
                self.over_write_selected = self.return_new_widget(
                    selected_widget=selectWidgetBox
                )
                DragTargetEvent.control.content.content = self.over_write_selected[
                    0
                ].content

        # #: UPDATE COLOR WIDGET
        DragTargetEvent.control.content.border = True
        DragTargetEvent.control.content.border = ft.border.all(
            0, ft.colors("transparent")
        )
        DragTargetEvent.control.update()

        self.page.update()

        # RUN ONLY IN PRODUCTION
        # print(selectWidgetBox,"==",self.right_control)

    def drag_will_accept(self, DragTargetEvent: object = None):

        DragTargetEvent.control.content.border = None
        DragTargetEvent.control.content.border = ft.border.all(4, ft.colors("cyan900"))

        DragTargetEvent.control.update()
        self.page.update()

    def drag_leave(self, DragTargetEvent):

        DragTargetEvent.control.content.border = True
        DragTargetEvent.control.content.border = ft.border.all(
            0, ft.colors("transparent")
        )

        DragTargetEvent.control.update()
        self.page.update()
