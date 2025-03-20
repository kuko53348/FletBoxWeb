import flet as ft
from .re_validation_input_textfield import input_filter_by


class get_one_string_with_slider(ft.Row):

    def __init__(
        self,
        page: object = None,
        tag_edit_widget: str = "",
        widget_to_edit: object = None,
        visible: bool = True,
        l_value=None,
    ) -> None:
        super().__init__()
        self.page = page

        self.spacing = 8
        self.run_spacing = 8

        self.l_value = l_value
        self.visible = visible
        self.tag_edit_widget = tag_edit_widget
        self.widget_to_edit = widget_to_edit

        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.run_alignment = ft.CrossAxisAlignment.START

        button_text = f"Open {tag_edit_widget}"
        self.only_cero_to_one = ["scale", "opacity", "aspect_ratio"]

        self.controls = [
            ft.Text(
                font_family="Consolas",
                width=80,
                value=self.tag_edit_widget.replace("_", " "),
                text_align=ft.TextAlign.START,
                weight=ft.FontWeight.BOLD,
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
                        keyboard_type=ft.KeyboardType.NUMBER,
                        width=60,
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
                    ft.Slider(
                        expand=True,
                        min=0,
                        max=(
                            1000
                            if not self.tag_edit_widget in self.only_cero_to_one
                            else 1
                        ),
                        on_change=lambda current_widget: self.set_attribute(
                            label="l", payload=current_widget
                        ),
                    ),
                ],
            ),
        ]

    def set_attribute(self, payload: object = None, label: str = "") -> None:
        self.l_value = payload.control.value
        self.l_value = input_filter_by(
            filter_type="float_int", payload=str(self.l_value)
        )

        if self.tag_edit_widget in self.only_cero_to_one:
            if float(self.l_value) >= 1.0:
                self.l_value = 1.0

        self.l_value = float(self.l_value)

        if self.tag_edit_widget == "padding":
            self.widget_to_edit.padding = ft.padding.all(value=int(self.l_value))

        elif self.tag_edit_widget == "margin":
            self.widget_to_edit.margin = ft.margin.all(value=int(self.l_value))

        elif self.tag_edit_widget == "border_radius":
            self.widget_to_edit.border_radius = ft.border_radius.all(
                value=int(self.l_value)
            )

        else:
            setattr(
                self.widget_to_edit,
                self.tag_edit_widget,
                self.l_value,
            )

        self.widget_to_edit.update()
