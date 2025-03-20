import flet as ft


class bool_widget(ft.Row):

    def __init__(
        self,
        page: object = None,
        tag_edit_widget: str = "",
        visible: bool = True,
        widget_to_edit: object = None,
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
        self.controls = [
            ft.Text(
                value=self.tag_edit_widget,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD,
                font_family="Consolas",
            ),
            ft.Switch(
                value=getattr(widget_to_edit, tag_edit_widget),
                on_change=lambda current_widget: self.set_attribute(
                    payload=current_widget
                ),
            ),
        ]

    def set_attribute(self, payload: object = None) -> None:
        setattr(self.widget_to_edit, self.tag_edit_widget, payload.control.value)

        self.widget_to_edit.update()
