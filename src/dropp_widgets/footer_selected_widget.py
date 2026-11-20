import flet as ft


class footer_selected_widget(ft.Container):
    """ONLY FUNCTION IS SHOW SELECTED WIDGET IN PHONE"""

    def __init__(
        self,
        page: object = None,
        widget_selected: str = "Container",
        type_widget: str = "None",
        icon_widget: str = "select_all_rounded",
        side: str = "",
    ):
        super().__init__()
        self.page = page
        self.alignment = ft.alignment.center_left
        self.bgcolor = ft.Colors.with_opacity(0.02, "white")
        # self.border = ft.border.all(2, ft.Colors.with_opacity(0.02, "red"))
        self.border_radius = ft.border_radius.all(30)
        self.icon_widget = icon_widget
        self.ink = False
        self.margin = ft.margin.all(0)
        self.padding = ft.padding.all(0)
        self.type_widget = type_widget
        self.side = side
        self.widget_selected = type_widget
        self.width = 200

        self.border_radius = ft.border_radius.only(
            top_left=32,
            top_right=32,
            bottom_left=32,
            bottom_right=32,
        )
        self.border = ft.border.all(
            width=2,
            color=ft.Colors("grey900"),
        )
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors("black45"),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )

        self.content = ft.Row(
            controls=[
                ft.Container(
                    margin=ft.margin.only(left=8, top=0, right=0, bottom=0),
                    content=ft.Icon(self.icon_widget),
                ),
                ft.Container(
                    # width=140,
                    # expand = True,
                    content=ft.Text(
                        value=f"{self.type_widget}:\n",
                        text_align=ft.TextAlign.LEFT,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",  # "Consolas ,RobotoSlab
                        size=8,
                        spans=[
                            ft.TextSpan(
                                text=self.widget_selected,
                                style=ft.TextStyle(
                                    size=17,
                                    color=ft.Colors("cyan"),
                                    weight=ft.FontWeight.BOLD,
                                ),
                            ),
                        ],
                    ),
                ),
            ]
        )
        # self.page.session.set(f"selection_footer_{self.side}_text", self.content)


class selected_widget(ft.Row):

    def __init__(self, page: object = None) -> None:
        super().__init__()
        self.page = page
        self.alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.run_alignment = ft.CrossAxisAlignment.CENTER
        self.expand = True
        self.spacing = 8
        self.run_spacing = 8

        self.right_text = "None"

        self.left_container = footer_selected_widget(
            page=self.page,
            widget_selected="Container",
            type_widget="None",
            icon_widget="select_all_rounded",
            side="left",
        )

        self.right_container = footer_selected_widget(
            page=self.page,
            widget_selected="Container",
            type_widget=self.right_text,
            icon_widget="select_all_rounded",
            side="right",
        )

        self.controls = [self.left_container, self.right_container]
