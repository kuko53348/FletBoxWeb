import flet as ft
from .re_validation_input_textfield import input_filter_by


class get_four_numers(ft.Row):

    def __init__(
        self,
        page: object = None,
        tag_edit_widget: str = "",
        widget_to_edit: object = None,
        l_value=0,
        t_value=0,
        r_value=0,
        b_value=0,
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
        self.t_value = t_value
        self.r_value = r_value
        self.b_value = b_value

        check_if_is_not_none_value = getattr(
            self.widget_to_edit, tag_edit_widget, tag_edit_widget
        )

        if check_if_is_not_none_value:
            if tag_edit_widget == "padding" or tag_edit_widget == "margin":
                self.l_value = getattr(
                    getattr(self.widget_to_edit, tag_edit_widget), "left"
                )
                self.t_value = getattr(
                    getattr(self.widget_to_edit, tag_edit_widget), "top"
                )
                self.r_value = getattr(
                    getattr(self.widget_to_edit, tag_edit_widget), "right"
                )
                self.b_value = getattr(
                    getattr(self.widget_to_edit, tag_edit_widget), "bottom"
                )

            elif tag_edit_widget == "border_radius":
                self.l_value = getattr(
                    getattr(self.widget_to_edit, tag_edit_widget), "top_left"
                )
                self.t_value = getattr(
                    getattr(self.widget_to_edit, tag_edit_widget), "top_right"
                )
                self.r_value = getattr(
                    getattr(self.widget_to_edit, tag_edit_widget), "bottom_left"
                )
                self.b_value = getattr(
                    getattr(self.widget_to_edit, tag_edit_widget), "bottom_right"
                )
        else:
            if self.tag_edit_widget == "padding":
                setattr(
                    self.widget_to_edit,
                    "padding",
                    ft.padding.only(
                        left=self.l_value,
                        top=self.t_value,
                        right=self.r_value,
                        bottom=self.b_value,
                    ),
                )
            elif self.tag_edit_widget == "margin":
                setattr(
                    self.widget_to_edit,
                    "margin",
                    ft.margin.only(
                        left=self.l_value,
                        top=self.t_value,
                        right=self.r_value,
                        bottom=self.b_value,
                    ),
                )
            elif self.tag_edit_widget == "border_radius":
                self.widget_to_edit.border_radius = ft.BorderRadius(
                    top_left=self.l_value,
                    top_right=self.t_value,
                    bottom_left=self.r_value,
                    bottom_right=self.b_value,
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
                        value=self.t_value,
                        # label="R",
                        border_width=0,
                        border_radius=ft.border_radius.all(18),
                        on_change=lambda current_widget: self.set_attribute(
                            label="r", payload=current_widget
                        ),
                    ),
                    ft.TextField(
                        width=50,
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.05, color=ft.Colors("blue")
                        ),
                        value=self.r_value,
                        # label="U",
                        border_width=0,
                        border_radius=ft.border_radius.all(18),
                        on_change=lambda current_widget: self.set_attribute(
                            label="u", payload=current_widget
                        ),
                    ),
                    ft.TextField(
                        width=50,
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.05, color=ft.Colors("green")
                        ),
                        value=self.b_value,
                        # label="D",
                        border_width=0,
                        border_radius=ft.border_radius.all(18),
                        on_change=lambda current_widget: self.set_attribute(
                            label="d", payload=current_widget
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
            self.l_value = int(self.l_value)

        elif label == "r":
            self.r_value = payload.control.value
            self.r_value = input_filter_by(
                filter_type="float_int",
                payload=str(self.r_value),
            )
            self.r_value = int(self.r_value)

        elif label == "u":
            self.t_value = payload.control.value
            self.t_value = input_filter_by(
                filter_type="float_int",
                payload=str(self.t_value),
            )
            self.t_value = int(self.t_value)

        elif label == "d":
            self.b_value = payload.control.value
            self.b_value = input_filter_by(
                filter_type="float_int",
                payload=str(self.b_value),
            )
            self.b_value = int(self.b_value)

        if self.tag_edit_widget == "padding" or self.tag_edit_widget == "margin":
            setattr(
                getattr(self.widget_to_edit, self.tag_edit_widget),
                "left",
                self.l_value,
            )
            setattr(
                getattr(self.widget_to_edit, self.tag_edit_widget),
                "top",
                self.t_value,
            )
            setattr(
                getattr(self.widget_to_edit, self.tag_edit_widget),
                "right",
                self.r_value,
            )
            setattr(
                getattr(self.widget_to_edit, self.tag_edit_widget),
                "bottom",
                self.b_value,
            )

        elif self.tag_edit_widget == "border_radius":
            setattr(
                getattr(self.widget_to_edit, self.tag_edit_widget),
                "top_left",
                self.l_value,
            )
            setattr(
                getattr(self.widget_to_edit, self.tag_edit_widget),
                "top_right",
                self.t_value,
            )
            setattr(
                getattr(self.widget_to_edit, self.tag_edit_widget),
                "bottom_left",
                self.r_value,
            )
            setattr(
                getattr(self.widget_to_edit, self.tag_edit_widget),
                "bottom_right",
                self.b_value,
            )

        self.widget_to_edit.update()
