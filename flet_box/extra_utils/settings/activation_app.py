import os
import time
import flet as ft

# import pyperclip # type: ignore

click_avalidation: bool = False


dictionary_contribution: dict = {
    "header": """
▎Flet-Box: The Future of Development, Built on Freedom""",
    "body": """Dear FletBox Community,

At FletBox, we strive to provide the best services and experiences for our users. Our mission is to continually enhance our platform, deliver innovative features, and support our growing community. However, to achieve these goals, we rely on the generosity of supporters like you.

Your donation will help us:

• Improve our infrastructure and ensure a seamless user experience.

• Develop new features that meet your needs and expectations.

• Maintain and enhance our existing services.

• Support our team in creating valuable content and resources.

Every contribution, no matter how small, makes a significant difference. Together, we can build a better FletBox for everyone. If you appreciate what we do and want to see us thrive, please consider making a donation today.

Thank you for your support!""",
    "crypto": {
        "Matic": {
            "address": "0x6d437bB66af8d2c44670eA18F059BE1417Dcd7bA",
            "path_image": "flet_box/assets/.wallet_matic.jpg",
            "red": "ERC-20",
        },
    },
}


class InfoProyect(ft.Container):
    """INFO PROYECT READ TEXT"""

    def __init__(
        self,
    ):
        super().__init__()
        self.expand = True
        self.ink = False
        self.bgcolor = ft.colors("black45")
        self.padding = ft.padding.all(8)
        self.margin = ft.margin.all(0)
        self.alignment = ft.alignment.top_center
        self.border_radius = ft.border_radius.all(36)
        self.border = ft.border.all(2, ft.colors("black"))
        self.height = 590
        self.shadow = ft.BoxShadow(
            spread_radius=0,
            blur_radius=18,
            color=ft.Colors.with_opacity(opacity=0.8, color=ft.colors("black")),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )
        self.gradient = ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_left,
            colors=[
                ft.colors("black"),
                ft.colors("black12"),
                ft.colors("black"),
            ],
        )

    def build(self):
        self.content = ft.Column(
            scroll="Hidden",
            controls=[
                ft.Text(
                    spans=[
                        ft.TextSpan(
                            f"{dictionary_contribution.get('header')}\n\n",
                            ft.TextStyle(
                                size=18,
                                color=ft.colors("red"),
                                weight=ft.FontWeight.BOLD,
                            ),
                        ),
                        ft.TextSpan(
                            dictionary_contribution.get("body"),
                            ft.TextStyle(
                                size=15,
                                color=ft.colors("white"),
                            ),
                        ),
                    ],
                ),
            ],
        )


class CardPrice(ft.Container):
    """PRICE OF THE CARDS"""

    def __init__(
        self,
        card_color: bool = False,
        card_plan: int = 1,
        card_price: int = 1,
        card_type: str = "",
    ):
        super().__init__()

        self.card_color = card_color
        self.card_plan = card_plan
        self.card_type = card_type
        self.card_price = card_price
        self.gold_color = (
            ft.colors("yellow") if self.card_color else ft.colors("blue900")
        )

        if self.card_plan == 1:
            self.buy_card = [True, False, False, False, False]
        if self.card_plan == 2:
            self.buy_card = [True, True, False, False, False]
        if self.card_plan == 3:
            self.buy_card = [True, True, True, True, True]

        self.expand = True
        self.ink = False
        self.bgcolor = ft.colors("black45")
        self.padding = ft.padding.all(8)
        self.margin = ft.margin.all(8)
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(30)
        self.height = 360
        self.border = ft.border.all(6, ft.colors("black45"))
        self.shadow = ft.BoxShadow(
            spread_radius=0,
            blur_radius=16,
            color=ft.Colors.with_opacity(0.8, ft.colors("black26")),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )
        self.gradient = ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_left,
            colors=[
                ft.colors("black"),
                self.gold_color,
                ft.colors("black"),
            ],
        )

    def build(self):
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            run_spacing=15,
            controls=[
                ft.Text(value=self.card_type, size=16, weight=ft.FontWeight.BOLD),
                ft.Text(
                    spans=[
                        ft.TextSpan(
                            f"${self.card_price}",
                            ft.TextStyle(
                                size=24,
                                color=ft.colors("white38"),
                                weight=ft.FontWeight.BOLD,
                                decoration=ft.TextDecoration.LINE_THROUGH,
                            ),
                        ),
                        ft.TextSpan(
                            f"${self.card_price//2} ",
                            ft.TextStyle(
                                size=45,
                                color=ft.colors("white"),
                                weight=ft.FontWeight.BOLD,
                            ),
                        ),
                    ],
                ),
                ft.Text(
                    value="Per Month",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Checkbox(label="Core Plataform Features", value=self.buy_card[0]),
                ft.Checkbox(label="Unlimit Compilate App", value=self.buy_card[1]),
                ft.Checkbox(label="Code Download", value=self.buy_card[2]),
                ft.Checkbox(label="GitHub Integration", value=self.buy_card[3]),
                ft.Checkbox(label="App & Play Store Dev", value=self.buy_card[4]),
                ft.ElevatedButton(
                    text="Is free no need Pay",
                    bgcolor=ft.colors("black45"),
                ),
            ],
        )


class price_container(ft.Container):

    def __init__(self):
        super().__init__()
        self.expand = True
        self.ink = False
        self.bgcolor = ft.colors("black26")
        self.padding = ft.padding.only(left=8, right=8, bottom=1, top=1)
        self.margin = ft.margin.all(0)
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(36)
        self.border = ft.border.all(2, ft.colors("black"))

    def build(self):
        self.content = ft.Row(
            scroll="Hidden",
            controls=[
                CardPrice(card_plan=1, card_price=110, card_type="Standar"),
                CardPrice(
                    card_plan=3, card_price=200, card_type="Pro", card_color=True
                ),
                CardPrice(card_plan=2, card_price=160, card_type="Teams"),
            ],
        )


class wallet_container(ft.Container):
    token_crypto = "0x6d437bB66af8d2c44670eA18F059BE1417Dcd7bA"

    def __init__(self, data="Erase this test"):
        super().__init__()
        self.title = data
        self.bgcolor = ft.colors("black45")
        self.padding = ft.padding.all(0)
        self.margin = ft.margin.all(0)
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(30)
        self.border = ft.border.all(2, ft.colors("black"))
        self.image = ft.DecorationImage(
            src=".cripto.webp",
            opacity=0.05,
            fit="COVER",
        )

    def build(self):
        self.alert_dialog = ft.Container(
            visible=False,
            width=110,
            bgcolor="red",
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(16),
            content=ft.Text(
                value="Done",
            ),
        )
        self.box_wallet_addres = ft.Container(
            bgcolor=ft.colors("black26"),
            padding=ft.padding.only(left=12, top=24, right=8, bottom=8),
            margin=ft.margin.all(8),
            border_radius=ft.border_radius.all(24),
            content=ft.Column(
                run_spacing=8,
                spacing=8,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            ft.Text(
                                value="ERC-20 Matic", size=24, weight=ft.FontWeight.BOLD
                            ),
                            self.alert_dialog,
                        ],
                    ),
                    ft.Row(
                        run_spacing=0,
                        spacing=4,
                        controls=[
                            ft.ElevatedButton(
                                text="Copy",
                                elevation=12,
                                bgcolor=ft.colors("red800"),
                                on_click=lambda _: self.copy_clipboad(
                                    value="0x6d437bB66af8d2c44670eA18F059BE1417Dcd7bA"
                                ),
                            ),
                            ft.TextButton(
                                text="0x6d437bB66af8d2c44670eA18F059BE1417Dcd7bA",
                                height=40,
                            ),
                        ],
                    ),
                    ft.Text(
                        spans=[
                            ft.TextSpan(
                                "Hello Dev:   You may invite me a beer ;)\n",
                                ft.TextStyle(
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.colors("blueaccent200"),
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )
        self.image_box = ft.Image(
            src=".wallet_matic.jpg",
            fit=ft.ImageFit.COVER,
            border_radius=ft.border_radius.all(30),
        )
        self.content = ft.Row(
            controls=[
                ft.Container(
                    ink=False,
                    bgcolor=ft.colors("black45"),
                    padding=ft.padding.all(8),
                    margin=ft.margin.all(4),
                    alignment=ft.alignment.center,
                    height=190,
                    border_radius=ft.border_radius.all(30),
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=18,
                        color=ft.Colors.with_opacity(0.8, ft.colors("black")),
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    content=self.image_box,
                ),
                ft.Container(
                    ink=False,
                    padding=ft.padding.all(8),
                    margin=ft.margin.all(8),
                    alignment=ft.alignment.center_left,
                    border_radius=ft.border_radius.all(30),
                    content=ft.Column(
                        controls=[
                            ft.ElevatedButton(
                                text="Matic",
                                elevation=12,
                                bgcolor=ft.colors("blue800"),
                            ),
                        ]
                    ),
                ),
                self.box_wallet_addres,
            ]
        )

    def copy_clipboad(self, value: str = str()):
        self.page.set_clipboard(value=value)
        self.alert_dialog.visible = True
        self.alert_dialog.content.value = f"Done:"
        self.alert_dialog.update()
        time.sleep(0.5)
        self.alert_dialog.visible = False
        self.alert_dialog.update()


class sponsor_page(ft.Container):

    def __init__(self, page: object = None):
        super().__init__()
        self.page = page
        self.ink = False
        self.bgcolor = ft.colors("black12")
        self.padding = ft.padding.all(32)
        self.margin = ft.margin.all(8)
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(30)
        self.border = ft.border.all(1, ft.colors("white12"))
        self.expand = True
        self.blur = (60, 60)

    def build(self):
        self.on_click = lambda _: self.go_home_page()
        self.content = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            price_container(),
                            wallet_container(),
                        ]
                    )
                ),
                InfoProyect(),
            ],
        )

    def go_home_page(self):
        self.page.go("/")


if __name__ == "__main__":

    def main(page: ft.Page):

        page.scroll = "HIDDEN"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        page.theme_mode = ft.ThemeMode.DARK
        page.window_bgcolor = ft.colors.RED_100

        page.window_left = 3
        page.window_top = 3
        page.window_height = 700

        page.padding = 0
        page.spacing = 0
        page.add(sponsor_page())

    ft.app(target=main, assets_dir="assets")
