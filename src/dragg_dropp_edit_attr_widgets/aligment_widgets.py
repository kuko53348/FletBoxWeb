import flet as ft


class get_aligment(ft.Row):

    def __init__(
        self,
        page: object = None,
        widget_parent_name: str = "",
        tag_edit_widget: str = "",
        widget_to_edit: object = None,
    ) -> None:
        super().__init__()
        self.page = page
        self.widget_parent_name = widget_parent_name
        self.tag_edit_widget = tag_edit_widget
        self.widget_to_edit = widget_to_edit

        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.run_alignment = ft.CrossAxisAlignment.START
        self.spacing = 8
        self.run_spacing = 8

        if widget_parent_name == "Row":
            start = ["start", "vertical_align_top_rounded"]
            end = ["end", "vertical_align_center_rounded"]
            center = ["center", "vertical_align_bottom_rounded"]
            space_between = ["between", "vertical_distribute_rounded"]
            space_around = ["around", "format_line_spacing"]
            space_evenly = ["evenly", "format_align_center_rounded"]

        elif widget_parent_name == "Column":
            start = ["start", "align_horizontal_left_rounded"]
            end = ["end", "align_horizontal_center_rounded"]
            center = ["center", "align_horizontal_right_rounded"]
            space_between = ["between", "vertical_distribute_rounded"]
            space_around = ["around", "format_line_spacing"]
            space_evenly = ["evenly", "format_align_center_rounded"]

        self.controls = [
            ft.Text(
                expand=True,
                value=f"{self.tag_edit_widget}\n{widget_parent_name}",
                text_align=ft.TextAlign.START,
                weight=ft.FontWeight.BOLD,
                font_family="Consolas",
            ),
            ft.Container(
                ink=True,
                border_radius=ft.border_radius.all(8),
                padding=ft.padding.all(4),
                bgcolor=ft.Colors.with_opacity(opacity=0.05, color=ft.Colors("red")),
                content=ft.Column(
                    run_spacing=0,
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(start[1]),
                        ft.Text(
                            value=start[0],
                            size=8,
                        ),
                    ],
                ),
                on_click=lambda widget_name: self.set_attribute(payload=widget_name),
            ),
            ft.Container(
                ink=True,
                border_radius=ft.border_radius.all(8),
                padding=ft.padding.all(4),
                bgcolor=ft.Colors.with_opacity(opacity=0.05, color=ft.Colors("yellow")),
                content=ft.Column(
                    run_spacing=0,
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(end[1]),
                        ft.Text(
                            value=center[0],
                            size=8,
                        ),
                    ],
                ),
                on_click=lambda widget_name: self.set_attribute(payload=widget_name),
            ),
            ft.Container(
                ink=True,
                border_radius=ft.border_radius.all(8),
                padding=ft.padding.all(4),
                bgcolor=ft.Colors.with_opacity(opacity=0.05, color=ft.Colors("blue")),
                content=ft.Column(
                    run_spacing=0,
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(center[1]),
                        ft.Text(
                            value=end[0],
                            size=8,
                        ),
                    ],
                ),
                on_click=lambda widget_name: self.set_attribute(payload=widget_name),
            ),
            ft.Container(
                ink=True,
                border_radius=ft.border_radius.all(8),
                padding=ft.padding.all(4),
                bgcolor=ft.Colors.with_opacity(opacity=0.05, color=ft.Colors("green")),
                content=ft.Column(
                    run_spacing=0,
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(space_between[1]),
                        ft.Text(
                            value=space_between[0],
                            size=8,
                        ),
                    ],
                ),
                on_click=lambda widget_name: self.set_attribute(payload=widget_name),
            ),
            ft.Container(
                ink=True,
                border_radius=ft.border_radius.all(8),
                padding=ft.padding.all(4),
                bgcolor=ft.Colors.with_opacity(opacity=0.05, color=ft.Colors("orange")),
                content=ft.Column(
                    run_spacing=0,
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(space_around[1]),
                        ft.Text(
                            value=space_around[0],
                            size=8,
                        ),
                    ],
                ),
                on_click=lambda widget_name: self.set_attribute(payload=widget_name),
            ),
            ft.Container(
                ink=True,
                border_radius=ft.border_radius.all(8),
                padding=ft.padding.all(4),
                bgcolor=ft.Colors.with_opacity(opacity=0.05, color=ft.Colors("cyan")),
                content=ft.Column(
                    run_spacing=0,
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(space_evenly[1]),
                        ft.Text(
                            value=space_evenly[0],
                            size=8,
                        ),
                    ],
                ),
                on_click=lambda widget_name: self.set_attribute(payload=widget_name),
            ),
        ]

    def set_attribute(self, payload: object = None) -> None:
        aligment_widget = payload.control.content.controls[1].value

        if aligment_widget == "start":
            self.widget_to_edit.alignment = ft.MainAxisAlignment.START
        elif aligment_widget == "end":
            self.widget_to_edit.alignment = ft.MainAxisAlignment.END
        elif aligment_widget == "center":
            self.widget_to_edit.alignment = ft.MainAxisAlignment.CENTER
        elif aligment_widget == "between":
            self.widget_to_edit.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        elif aligment_widget == "around":
            self.widget_to_edit.alignment = ft.MainAxisAlignment.SPACE_AROUND
        elif aligment_widget == "evenly":
            self.widget_to_edit.alignment = ft.MainAxisAlignment.SPACE_EVENLY

        self.widget_to_edit.update()


class get_aligment_container(ft.Row):

    def __init__(
        self,
        page: object = None,
        tag_edit_widget: str = "",
        widget_to_edit: object = None,
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

        start = ["start", "circle"]
        end = ["end", "circle"]
        center = ["center", "circle"]
        space_between = ["between", "circle"]
        space_around = ["around", "circle"]
        space_evenly = ["evenly", "circle"]

        self.controls = [
            ft.Text(
                expand=True,
                value=f"{self.tag_edit_widget}\nContainer",
                text_align=ft.TextAlign.START,
                weight=ft.FontWeight.BOLD,
                font_family="Consolas",
            ),
            ft.RadioGroup(
                on_change=lambda widget_name: self.change_aliment(payload=widget_name),
                content=ft.Column(
                    spacing=5,
                    run_spacing=18,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Radio(
                                    value="top_left",
                                    fill_color=ft.Colors.YELLOW_200,
                                    active_color=ft.Colors.RED,
                                ),
                                ft.Radio(
                                    value="top_center",
                                    fill_color=ft.Colors.BLUE_200,
                                    active_color=ft.Colors.BLACK,
                                ),
                                ft.Radio(
                                    value="top_right",
                                    fill_color=ft.Colors.GREEN_200,
                                    active_color=ft.Colors.CYAN,
                                ),
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.Radio(
                                    value="CENTER_LEFT",
                                    fill_color=ft.Colors.YELLOW_500,
                                    active_color=ft.Colors.RED,
                                ),
                                ft.Radio(
                                    value="center",
                                    fill_color=ft.Colors.BLUE_500,
                                    active_color=ft.Colors.BLACK,
                                ),
                                ft.Radio(
                                    value="CENTER_RIGHT",
                                    fill_color=ft.Colors.GREEN_500,
                                    active_color=ft.Colors.CYAN,
                                ),
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.Radio(
                                    value="bottom_left",
                                    fill_color=ft.Colors.YELLOW_800,
                                    active_color=ft.Colors.RED,
                                ),
                                ft.Radio(
                                    value="bottom_center",
                                    fill_color=ft.Colors.BLUE_800,
                                    active_color=ft.Colors.BLACK,
                                ),
                                ft.Radio(
                                    value="bottom_right",
                                    fill_color=ft.Colors.GREEN_800,
                                    active_color=ft.Colors.CYAN,
                                ),
                            ]
                        ),
                    ],
                ),
            ),
        ]

    def change_aliment(self, payload: object = None):
        aligment_widget = payload.control.value

        if aligment_widget == "top_left":
            self.widget_to_edit.alignment = ft.alignment.top_left
        elif aligment_widget == "top_center":
            self.widget_to_edit.alignment = ft.alignment.top_center
        elif aligment_widget == "top_right":
            self.widget_to_edit.alignment = ft.alignment.top_right
        elif aligment_widget == "CENTER_LEFT":
            self.widget_to_edit.alignment = ft.alignment.center_left
        elif aligment_widget == "center":
            self.widget_to_edit.alignment = ft.alignment.center
        elif aligment_widget == "CENTER_RIGHT":
            self.widget_to_edit.alignment = ft.alignment.center_right
        elif aligment_widget == "bottom_left":
            self.widget_to_edit.alignment = ft.alignment.bottom_left
        elif aligment_widget == "bottom_right":
            self.widget_to_edit.alignment = ft.alignment.bottom_right
        elif aligment_widget == "bottom_center":
            self.widget_to_edit.alignment = ft.alignment.bottom_center

        self.widget_to_edit.update()


class get_aligment_horizontal(ft.Row):
    # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
    # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE

    def __init__(
        self,
        page: object = None,
        tag_edit_widget: str = "",
        widget_to_edit: object = None,
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

        if tag_edit_widget == "vertical_alignment":
            start = ["start", "align_vertical_top_rounded"]
            end = ["end", "align_vertical_center_rounded"]
            center = ["center", "align_vertical_bottom_rounded"]

        elif tag_edit_widget == "horizontal_alignment":
            start = ["start", "align_horizontal_left_rounded"]
            end = ["end", "align_horizontal_center_rounded"]
            center = ["center", "align_horizontal_right_rounded"]

        elif tag_edit_widget == "run_alignment":
            start = ["start", "align_horizontal_left_rounded"]
            end = ["end", "align_horizontal_center_rounded"]
            center = ["center", "align_horizontal_right_rounded"]

        self.controls = [
            ft.Text(
                expand=True,
                value=self.tag_edit_widget,
                text_align=ft.TextAlign.START,
                weight=ft.FontWeight.BOLD,
                font_family="Consolas",
            ),
            ft.Container(
                ink=True,
                border_radius=ft.border_radius.all(8),
                padding=ft.padding.all(4),
                bgcolor=ft.Colors.with_opacity(opacity=0.05, color=ft.Colors("red")),
                content=ft.Column(
                    run_spacing=0,
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(start[1]),
                        ft.Text(
                            value=start[0],
                            size=8,
                        ),
                    ],
                ),
                on_click=lambda widget_name: self.set_attribute(payload=widget_name),
            ),
            ft.Container(
                ink=True,
                border_radius=ft.border_radius.all(8),
                padding=ft.padding.all(4),
                bgcolor=ft.Colors.with_opacity(opacity=0.05, color=ft.Colors("yellow")),
                content=ft.Column(
                    run_spacing=0,
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(end[1]),
                        ft.Text(
                            value=center[0],
                            size=8,
                        ),
                    ],
                ),
                on_click=lambda widget_name: self.set_attribute(payload=widget_name),
            ),
            ft.Container(
                ink=True,
                border_radius=ft.border_radius.all(8),
                padding=ft.padding.all(4),
                bgcolor=ft.Colors.with_opacity(opacity=0.05, color=ft.Colors("blue")),
                content=ft.Column(
                    run_spacing=0,
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(center[1]),
                        ft.Text(
                            value=end[0],
                            size=8,
                        ),
                    ],
                ),
                on_click=lambda widget_name: self.set_attribute(payload=widget_name),
            ),
        ]

    def set_attribute(self, payload: object = None) -> None:
        alignment_selected = payload.control.content.controls[1].value

        if alignment_selected == "start":
            if self.tag_edit_widget == "horizontal_alignment":
                self.widget_to_edit.horizontal_alignment = ft.CrossAxisAlignment.START
            elif self.tag_edit_widget == "vertical_alignment":
                self.widget_to_edit.vertical_alignment = ft.CrossAxisAlignment.START
            elif self.tag_edit_widget == "run_alignment":
                self.widget_to_edit.run_alignment = ft.CrossAxisAlignment.START

        elif alignment_selected == "center":
            if self.tag_edit_widget == "horizontal_alignment":
                self.widget_to_edit.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            elif self.tag_edit_widget == "vertical_alignment":
                self.widget_to_edit.vertical_alignment = ft.CrossAxisAlignment.CENTER
            elif self.tag_edit_widget == "run_alignment":
                self.widget_to_edit.run_alignment = ft.CrossAxisAlignment.CENTER

        elif alignment_selected == "end":
            if self.tag_edit_widget == "horizontal_alignment":
                self.widget_to_edit.horizontal_alignment = ft.CrossAxisAlignment.END
            elif self.tag_edit_widget == "vertical_alignment":
                self.widget_to_edit.vertical_alignment = ft.CrossAxisAlignment.END
            elif self.tag_edit_widget == "run_alignment":
                self.widget_to_edit.run_alignment = ft.CrossAxisAlignment.END

        self.widget_to_edit.update()
