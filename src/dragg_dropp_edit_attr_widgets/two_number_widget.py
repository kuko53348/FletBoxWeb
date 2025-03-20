import flet as ft
from .re_validation_input_textfield import input_filter_by


class get_two_numers(ft.Row):

    def __init__(
        self,
        page: object = None,
        tag_edit_widget: str = "",
        widget_to_edit: object = None,
        l_value=0,
        r_value=0,
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
        self.r_value = r_value

        check_if_is_not_none_value = getattr(
            self.widget_to_edit, tag_edit_widget, tag_edit_widget
        )
        if check_if_is_not_none_value:
            if tag_edit_widget == "offset":
                self.l_value = getattr(
                    getattr(self.widget_to_edit, tag_edit_widget), "x"
                )
                self.r_value = getattr(
                    getattr(self.widget_to_edit, tag_edit_widget), "y"
                )

        else:
            if self.tag_edit_widget == "offset":
                setattr(
                    self.widget_to_edit,
                    "offset",
                    ft.Offset(
                        x=self.l_value,
                        y=self.r_value,
                    ),
                )

        self.controls = [
            ft.Text(
                value=self.tag_edit_widget,
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
                        width=50,
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
                    ft.TextField(
                        width=50,
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.05, color=ft.Colors("yellow")
                        ),
                        value=self.r_value,
                        # label="R",
                        border_width=0,
                        border_radius=ft.border_radius.all(18),
                        on_change=lambda current_widget: self.set_attribute(
                            label="r", payload=current_widget
                        ),
                    ),
                ],
            ),
        ]

    def set_attribute(self, payload: object = None, label: str = "") -> None:
        if label == "l":
            self.l_value = payload.control.value
            self.l_value = input_filter_by(
                filter_type="float_int",
                payload=str(self.l_value),
            )
            self.l_value = float(self.l_value)

        elif label == "r":
            self.r_value = payload.control.value
            self.r_value = input_filter_by(
                filter_type="float_int",
                payload=str(self.r_value),
            )
            self.r_value = float(self.r_value)

        if self.tag_edit_widget == "offset":
            setattr(
                getattr(self.widget_to_edit, self.tag_edit_widget),
                "x",
                self.l_value,
            )
            setattr(
                getattr(self.widget_to_edit, self.tag_edit_widget),
                "y",
                self.r_value,
            )

        self.widget_to_edit.update()
