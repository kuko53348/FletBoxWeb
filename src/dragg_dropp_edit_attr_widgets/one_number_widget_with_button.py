import flet as ft
from .re_validation_input_textfield import input_filter_by


class get_one_string_with_button(ft.Row):

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
        self.tag_edit_widget = tag_edit_widget
        self.widget_to_edit = widget_to_edit
        self.visible = visible

        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.run_alignment = ft.CrossAxisAlignment.START
        self.spacing = 8
        self.run_spacing = 8
        self.l_value = l_value
        button_text = f"Open {tag_edit_widget}"
        check_if_is_not_none_value = getattr(
            self.widget_to_edit, tag_edit_widget, tag_edit_widget
        )

        if check_if_is_not_none_value:
            if tag_edit_widget == "image":
                self.l_value = ft.DecorationImage(
                    src="image136.jpeg",
                    fit=ft.ImageFit.COVER,
                    opacity=0.05,
                )

        else:
            # if self.tag_edit_widget == "image":
            #     setattr(self.widget_to_edit, "image", tag_edit_widget)
            self.image = ft.DecorationImage(
                src="image136.jpeg",
                fit=ft.ImageFit.COVER,
                opacity=1,
            )

        self.controls = [
            ft.Text(
                width=55,
                value=self.tag_edit_widget,
                text_align=ft.TextAlign.START,
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
                    ft.ElevatedButton(
                        text=button_text,
                        bgcolor=ft.Colors(("grey900")),
                    ),
                ],
            ),
        ]

    def set_attribute(self, payload: object = None, label: str = "") -> None:
        self.l_value = payload.control.value
        self.l_value = input_filter_by(
            filter_type="str",
            payload=str(self.l_value),
        )
        # if self.tag_edit_widget == "image":
        #     setattr(
        #         self.widget_to_edit,
        #         "image",
        #         self.l_value,
        #     )

        if self.widget_to_edit == "image":
            setattr(
                self.widget_to_edit,
                "src",
                self.l_value,
            )
        else:
            setattr(
                self.widget_to_edit,
                self.tag_edit_widget,
                self.l_value,
            )

        self.widget_to_edit.update()
