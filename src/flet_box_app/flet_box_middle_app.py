import flet as ft

from dragg_widgets.dragg_container import dragg_container_app
from dropp_widgets.dropp_container import drop_phone_container
from dragg_dropp_edit_attr_widgets.dragg_dropp_edit_attr_container import (
    edit_attributes_container,
)
from dropp_widgets.footer_selected_widget import selected_widget
from left_lite_menu.left_menu_app import left_menu_app_container


class middle_fletbox_container(ft.Container):

    def __init__(self, page: object = None, content: object = None) -> None:
        super().__init__()
        self.page = page
        self.expand = True
        self.ink = True
        self.alignment = ft.alignment.center
        self.ink_color = ft.Colors("yellow")
        self.padding = ft.padding.all(8)
        # self.image = ft.DecorationImage(
        #     src="wallpaper.jpeg",
        #     fit=ft.ImageFit.COVER,
        #     opacity=0.12,
        # )
        lite_menu_left_app = left_menu_app_container(page=self.page)
        selection_widget = selected_widget(page=self.page)
        self.content = ft.Container(
            # blur=ft.Blur(sigma_x=24, sigma_y=24),
            # border_radius=ft.border_radius.only(
            #     top_left=24, top_right=24, bottom_left=24, bottom_right=24
            # ),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=8,
                run_spacing=8,
                controls=[
                    ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True,
                        spacing=8,
                        run_spacing=8,
                        controls=[
                            lite_menu_left_app,
                            dragg_container_app(
                                page=self.page,
                                left_menu=lite_menu_left_app,
                                text_selection_widget=selection_widget,
                            ),
                            drop_phone_container(
                                page=self.page,
                                text_selection_widget=selection_widget,
                            ),
                            edit_attributes_container(page=self.page),
                        ],
                    ),
                ],
            ),
        )
