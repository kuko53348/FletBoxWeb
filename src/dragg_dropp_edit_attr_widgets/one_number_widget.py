import flet as ft

from .re_validation_input_textfield import input_filter_by


class get_one_string(ft.Row):

    def __init__(
        self,
        page: object = None,
        tag_edit_widget: str = "",
        widget_to_edit: object = None,
        l_value=None,
    ) -> None:
        super().__init__()
        self.page = page
        self.tag_edit_widget = tag_edit_widget
        self.widget_to_edit = widget_to_edit

        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.run_alignment = ft.CrossAxisAlignment.START
        self.spacing = 8
        self.run_spacing = 8
        self.l_value = l_value

        # check_if_is_not_none_value = getattr(
        #     self.widget_to_edit, tag_edit_widget, tag_edit_widget
        # )

        # if check_if_is_not_none_value:
        #     if tag_edit_widget == "tooltip":
        #         self.l_value = None

        # else:
        #     if self.tag_edit_widget == "tooltip":
        #         setattr(self.widget_to_edit, "tooltip", tag_edit_widget)

        self.controls = [
            ft.Text(
                value=self.tag_edit_widget.replace("_", " "),
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD,
                font_family="Consolas",
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=8,
                run_spacing=8,
                controls=[
                    ft.TextField(
                        # width=50,
                        expand=True,
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.05, color=ft.Colors("red")
                        ),
                        value=self.l_value,
                        # label="L",
                        border_width=0,
                        border_radius=ft.border_radius.all(18),
                        on_change=lambda current_widget: self.set_attribute(
                            label="l", payload=current_widget
                        ),
                    ),
                ],
            ),
        ]

    def set_attribute(self, payload: object = None, label: str = "") -> None:
        current_input = payload.control.value
        self.l_value = input_filter_by(filter_type="str", payload=current_input)

        if self.l_value:
            setattr(
                self.widget_to_edit,
                self.tag_edit_widget,
                self.l_value,
            )

        self.widget_to_edit.update()
