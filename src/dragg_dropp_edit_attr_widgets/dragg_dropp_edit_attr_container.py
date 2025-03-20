import flet as ft

from .bool_widget import bool_widget
from .one_number_widget import get_one_string
from .two_number_widget import get_two_numers
from .four_number_widget import get_four_numers
from .one_number_widget_with_button import get_one_string_with_button
from .one_number_with_slider import get_one_string_with_slider
from .linear_gradient_widget import get_linear_gradient

from .aligment_widgets import (
    get_aligment,
    get_aligment_horizontal,
    get_aligment_container,
)


class main_edit_container(ft.Container):
    # Generic Container

    def __init__(self, page: object = None, controls: list = []) -> None:
        super().__init__()
        self.page = page
        self.border_radius = ft.border_radius.only(
            top_left=12, top_right=12, bottom_left=12, bottom_right=12
        )

        self.shadow = ft.BoxShadow(
            spread_radius=0.02,
            blur_radius=3,
            color=ft.colors("black"),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )
        self.padding = ft.padding.only(left=12, right=8, bottom=8, top=8)
        self.ink = True
        self.bgcolor = ft.Colors.with_opacity(opacity=0.05, color=ft.colors("white"))
        self.alignment = ft.alignment.center
        self.ink_color = ft.colors("yellow")

        self.content = ft.Column(spacing=4, run_spacing=4, controls=controls)


class banner_eddit_title_container(ft.Container):

    def __init__(
        self,
        page: object = None,
        content: object = None,
        title_container: str = "",
    ) -> None:
        super().__init__()
        self.page = page
        self.title_container = title_container
        self.padding = ft.padding.only(left=8, top=4, right=8, bottom=8)
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            # expand=True,
            spacing=8,
            run_spacing=12,
            controls=[
                ft.Text(
                    value=title_container,
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.BOLD,
                    font_family="Consolas",
                ),
                content,
            ],
        )


class box_with_title_container(ft.Container):

    def __init__(self, page: object = None, controls: list = list()) -> None:
        super().__init__()
        self.page = page
        self.expand = True
        self.ink = True
        self.bgcolor = ft.colors("black12")
        self.alignment = ft.alignment.center
        self.ink_color = ft.colors("yellow")

        self.content = ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            auto_scroll=True,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            run_alignment=ft.CrossAxisAlignment.START,
            expand=True,
            spacing=8,
            run_spacing=8,
            controls=controls,
        )


class tabs_menu(ft.Container):

    def __init__(self, page: object = None, content: object = None) -> None:
        super().__init__()
        self.page = page
        # self.tooltip = 'Container'
        self.padding = ft.padding.only(left=8, right=8, bottom=0, top=0)
        self.border_radius = ft.border_radius.only(
            top_left=32, top_right=32, bottom_left=0, bottom_right=0
        )
        self.expand = True
        self.ink = True
        self.bgcolor = ft.colors("grey900")
        self.alignment = ft.alignment.top_center
        self.ink_color = ft.colors("yellow")

        edit_container = self.page.session.get("selected_in_phone_widget")
        # edit_container = ft.Container() if check_selection == None else check_selection

        self.content = ft.Tabs(
            selected_index=1,
            indicator_border_radius=32,
            overlay_color=ft.Colors("transparent"),
            expand=1,
            tabs=[
                ft.Tab(
                    tab_content=ft.Icon(name="phone_android_rounded"),
                    height=30,
                    content=box_with_title_container(
                        page=self.page,
                        controls=[],
                    ),
                ),
                ft.Tab(
                    tab_content=ft.Icon(name="style_rounded"),
                    content=box_with_title_container(
                        page=self.page,
                        controls=[
                            # banner_eddit_title_container(
                            #     page=self.page,
                            #     title_container="edit bool container",
                            #     content=main_edit_container(
                            #         page=self.page,
                            #         controls=[
                            #             bool_widget(
                            #                 page=self.page,
                            #                 visible=True,
                            #                 tag_edit_widget="expand",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #             ft.Divider(height=2, thickness=1),
                            #             bool_widget(
                            #                 page=self.page,
                            #                 tag_edit_widget="ink",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #             # ft.Divider(height=2, thickness=1),
                            #         ],
                            #     ),
                            # ),
                            # banner_eddit_title_container(
                            #     page=self.page,
                            #     title_container="Edit one numbers range",
                            #     content=main_edit_container(
                            #         page=self.page,
                            #         controls=[
                            #             get_one_string_with_slider(
                            #                 page=self.page,
                            #                 tag_edit_widget="opacity",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #             ft.Divider(height=2, thickness=1),
                            #             get_one_string_with_slider(
                            #                 page=self.page,
                            #                 tag_edit_widget="width",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #         ],
                            #     ),
                            # ),
                            # banner_eddit_title_container(
                            #     page=self.page,
                            #     title_container="Edit one numbers",
                            #     content=main_edit_container(
                            #         page=self.page,
                            #         controls=[
                            #             get_one_string_with_button(
                            #                 page=self.page,
                            #                 tag_edit_widget="image",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #             ft.Divider(height=2, thickness=1),
                            #             get_one_string_with_button(
                            #                 page=self.page,
                            #                 tag_edit_widget="bgcolor",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #         ],
                            #     ),
                            # ),
                            # banner_eddit_title_container(
                            #     page=self.page,
                            #     title_container="Edit one numbers",
                            #     content=main_edit_container(
                            #         page=self.page,
                            #         controls=[
                            #             get_one_string(
                            #                 page=self.page,
                            #                 tag_edit_widget="tooltip",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #             ft.Divider(height=2, thickness=1),
                            #             get_one_string(
                            #                 page=self.page,
                            #                 tag_edit_widget="tooltip",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #         ],
                            #     ),
                            # ),
                            # banner_eddit_title_container(
                            #     page=self.page,
                            #     title_container="Edit two numbers",
                            #     content=main_edit_container(
                            #         page=self.page,
                            #         controls=[
                            #             get_two_numers(
                            #                 page=self.page,
                            #                 tag_edit_widget="offset",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #             ft.Divider(height=2, thickness=1),
                            #             get_two_numers(
                            #                 page=self.page,
                            #                 tag_edit_widget="offset",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #         ],
                            #     ),
                            # ),
                            # banner_eddit_title_container(
                            #     page=self.page,
                            #     title_container="Edit for numbers",
                            #     content=main_edit_container(
                            #         page=self.page,
                            #         controls=[
                            #             get_four_numers(
                            #                 page=self.page,
                            #                 tag_edit_widget="padding",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #             ft.Divider(height=2, thickness=1),
                            #             get_four_numers(
                            #                 page=self.page,
                            #                 tag_edit_widget="margin",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #         ],
                            #     ),
                            # ),
                            # banner_eddit_title_container(
                            #     page=self.page,
                            #     title_container="Edit for numbers",
                            #     content=main_edit_container(
                            #         page=self.page,
                            #         controls=[
                            #             get_aligment_container(
                            #                 page=self.page,
                            #                 tag_edit_widget="aligment",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #             ft.Divider(height=2, thickness=1),
                            #             get_aligment(
                            #                 page=self.page,
                            #                 widget_parent_name="row",
                            #                 tag_edit_widget="aligment",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #             ft.Divider(height=2, thickness=1),
                            #             get_aligment(
                            #                 page=self.page,
                            #                 widget_parent_name="column",
                            #                 tag_edit_widget="aligment",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #             ft.Divider(height=2, thickness=1),
                            #             get_aligment_horizontal(
                            #                 page=self.page,
                            #                 tag_edit_widget="vertical_aligmnet",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #             ft.Divider(height=2, thickness=1),
                            #             get_aligment_horizontal(
                            #                 page=self.page,
                            #                 tag_edit_widget="horizontal_aligmnet",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #         ],
                            #     ),
                            # ),
                            # banner_eddit_title_container(
                            #     page=self.page,
                            #     title_container="Edit one numbers range",
                            #     content=main_edit_container(
                            #         page=self.page,
                            #         controls=[
                            #             get_linear_gradient(
                            #                 page=self.page,
                            #                 tag_edit_widget="linear_gradient",
                            #                 widget_to_edit=edit_container,
                            #             ),
                            #         ],
                            #     ),
                            # ),
                        ],
                    ),
                ),
                ft.Tab(
                    tab_content=ft.Icon(name="edit_off_rounded"),
                    content=box_with_title_container(
                        page=self.page,
                        controls=[],
                    ),
                ),
            ],
        )
        self.page.session.set("tabs_containers", self)


class footer_menu(ft.Container):

    def __init__(
        self,
        page: object = None,
        dragg_width: object = None,
        left_menu: object = None,
    ) -> None:
        super().__init__()
        self.page = page
        self.dragg_width = dragg_width
        self.left_menu = left_menu

        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors("black"),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )
        self.bgcolor = ft.Colors.with_opacity(opacity=0.09, color=ft.Colors("white"))
        self.padding = ft.padding.only(left=4, top=0, right=2, bottom=0)
        self.margin = ft.margin.only(left=0, top=0, right=0, bottom=0)
        self.alignment = ft.alignment.center
        self.content = ft.Row(
            spacing=0,
            run_spacing=0,
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            controls=[
                ft.Slider(
                    width=100,
                    min=1,
                    max=4,
                    divisions=0.1,
                    # on_change=lambda slider_value: self.change_dragg_width(
                    #     payload=slider_value
                    # ),
                ),
                ft.Text(value="width", weight="bold"),
            ],
        )


class edit_attributes_container(ft.Container):

    def __init__(self, page: object = None, content: object = None) -> None:
        super().__init__()
        self.page = page
        self.ink = True
        # self.left_menu = left_menu
        self.bgcolor = ft.colors("white12")
        self.alignment = ft.alignment.center
        self.ink_color = ft.colors("yellow")
        self.width = 400
        self.padding = ft.padding.only(left=0, right=0, bottom=0, top=0)
        self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        self.border_radius = ft.border_radius.only(
            top_left=32, top_right=32, bottom_left=32, bottom_right=32
        )
        self.border = ft.border.all(width=2, color=ft.colors("grey900"))
        self.gradient = ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.colors("transparent"), ft.colors("black12")],
        )
        self.image = ft.DecorationImage(
            src="image136.jpeg",
            fit=ft.ImageFit.COVER,
            opacity=0.05,
        )
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors("black"),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )

        self.content = ft.Column(
            spacing=0,
            run_spacing=0,
            controls=[
                tabs_menu(page=self.page),
                footer_menu(page=self.page),
            ],
        )
