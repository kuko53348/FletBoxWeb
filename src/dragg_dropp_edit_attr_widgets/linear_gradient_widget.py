import flet as ft
from itertools import takewhile
from .re_validation_input_textfield import input_filter_by

# for _ in dir(ft.Colors):
#     if _ == "__add__":
#         break
#     list_reference_color.append(_.lower())


list_reference_color = [
    _.lower() for _ in list(takewhile(lambda x: x != "__add__", dir(ft.Colors)))
]

one_color = "transparent"
second_color = "cyan"
three_color_check = ""
three_color = None
four_color = None


class get_four_numers(ft.Row):

    def __init__(
        self,
        page: object = None,
        widget_to_edit: object = None,
        l_value="",
        t_value="",
        r_value="",
        b_value="",
    ) -> None:
        super().__init__()
        self.page = page
        self.widget_to_edit = widget_to_edit

        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.run_alignment = ft.CrossAxisAlignment.START
        self.spacing = 8
        self.run_spacing = 8

        # attr
        self.l_value = l_value
        self.t_value = t_value
        self.r_value = r_value
        self.b_value = b_value

        self.controls = [
            ft.ElevatedButton(
                text="open color",
                icon="palette_rounded",
                bgcolor=ft.Colors(("green900")),
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
        global one_color, second_color, three_color, four_color, three_color_check

        if label == "l":
            one_color = payload.control.value.strip()

        elif label == "r":
            second_color = payload.control.value.strip()

        elif label == "u":
            three_color = payload.control.value.strip()
            three_color_check = three_color

            if not three_color in list_reference_color:
                three_color = None

        elif label == "d":
            four_color = payload.control.value.strip()

            if three_color == None:
                four_color = None

            else:
                if not four_color in list_reference_color:
                    four_color = None


class get_linear_gradient(ft.Column):
    # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
    # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
    selected_list: list = [
        ft.Colors(one_color),
        ft.Colors(second_color),
    ]
    left_selected: object = ft.alignment.top_center
    right_selected: object = ft.alignment.bottom_center

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

        self.controls = [
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                run_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    ft.Text(
                        expand=True,
                        value="linear\ngradient",
                        text_align=ft.TextAlign.START,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",
                    ),
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                expand=True,
                                value="gradient begin",
                                text_align=ft.TextAlign.CENTER,
                                weight=ft.FontWeight.BOLD,
                                font_family="Consolas",
                            ),
                            ft.RadioGroup(
                                on_change=lambda widget_name: self.change_aliment(
                                    payload=widget_name
                                ),
                                content=ft.Column(
                                    spacing=5,
                                    run_spacing=18,
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Radio(
                                                    value="left_top_left",
                                                    fill_color=ft.Colors.YELLOW_200,
                                                    active_color=ft.Colors.RED,
                                                ),
                                                ft.Radio(
                                                    value="CENTER_TOP_left",
                                                    fill_color=ft.Colors.BLUE_200,
                                                    active_color=ft.Colors.BLACK,
                                                ),
                                                ft.Radio(
                                                    value="right_top_left",
                                                    fill_color=ft.Colors.GREEN_200,
                                                    active_color=ft.Colors.CYAN,
                                                ),
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Radio(
                                                    value="left_CENTER_LEFT",
                                                    fill_color=ft.Colors.YELLOW_500,
                                                    active_color=ft.Colors.RED,
                                                ),
                                                ft.Radio(
                                                    value="CENTER_LEFT",
                                                    fill_color=ft.Colors.BLUE_500,
                                                    active_color=ft.Colors.BLACK,
                                                ),
                                                ft.Radio(
                                                    value="right_CENTER_LEFT",
                                                    fill_color=ft.Colors.GREEN_500,
                                                    active_color=ft.Colors.CYAN,
                                                ),
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Radio(
                                                    value="left_bottom_left",
                                                    fill_color=ft.Colors.YELLOW_800,
                                                    active_color=ft.Colors.RED,
                                                ),
                                                ft.Radio(
                                                    value="CENTER_BOTTOM_left",
                                                    fill_color=ft.Colors.BLUE_800,
                                                    active_color=ft.Colors.BLACK,
                                                ),
                                                ft.Radio(
                                                    value="right_bottom_left",
                                                    fill_color=ft.Colors.GREEN_800,
                                                    active_color=ft.Colors.CYAN,
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    ft.VerticalDivider(),
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                expand=True,
                                value="gradient end",
                                text_align=ft.TextAlign.CENTER,
                                weight=ft.FontWeight.BOLD,
                                font_family="Consolas",
                            ),
                            ft.RadioGroup(
                                on_change=lambda widget_name: self.change_aliment(
                                    payload=widget_name
                                ),
                                content=ft.Column(
                                    spacing=5,
                                    run_spacing=18,
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Radio(
                                                    value="left_top_right",
                                                    fill_color=ft.Colors.YELLOW_200,
                                                    active_color=ft.Colors.RED,
                                                ),
                                                ft.Radio(
                                                    value="CENTER_TOP_right",
                                                    fill_color=ft.Colors.BLUE_200,
                                                    active_color=ft.Colors.BLACK,
                                                ),
                                                ft.Radio(
                                                    value="right_top_right",
                                                    fill_color=ft.Colors.GREEN_200,
                                                    active_color=ft.Colors.CYAN,
                                                ),
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Radio(
                                                    value="left_CENTER_RIGHT",
                                                    fill_color=ft.Colors.YELLOW_500,
                                                    active_color=ft.Colors.RED,
                                                ),
                                                ft.Radio(
                                                    value="CENTER_RIGHT",
                                                    fill_color=ft.Colors.BLUE_500,
                                                    active_color=ft.Colors.BLACK,
                                                ),
                                                ft.Radio(
                                                    value="right_CENTER_RIGHT",
                                                    fill_color=ft.Colors.GREEN_500,
                                                    active_color=ft.Colors.CYAN,
                                                ),
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Radio(
                                                    value="left_bottom_right",
                                                    fill_color=ft.Colors.YELLOW_800,
                                                    active_color=ft.Colors.RED,
                                                ),
                                                ft.Radio(
                                                    value="CENTER_BOTTOM_right",
                                                    fill_color=ft.Colors.BLUE_800,
                                                    active_color=ft.Colors.BLACK,
                                                ),
                                                ft.Radio(
                                                    value="right_bottom_right",
                                                    fill_color=ft.Colors.GREEN_800,
                                                    active_color=ft.Colors.CYAN,
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ],
            ),
            get_four_numers(
                page=page,
                widget_to_edit=widget_to_edit,
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=8,
                run_spacing=8,
                controls=[
                    ft.ElevatedButton(
                        icon="save",
                        text="Apply",
                        bgcolor="green900",
                        on_click=lambda _: self.apply_gradient(),
                    ),
                    ft.ElevatedButton(
                        icon="cancel",
                        text="Cancel",
                        bgcolor="red900",
                        on_click=lambda _: self.cancel_gradient(),
                    ),
                ],
            ),
        ]

    def change_aliment(self, payload: object = None):
        selection_radio = payload.control.value

        # LEFT SELECTION
        if selection_radio == "left_top_left":
            self.left_selected = ft.alignment.top_left
        elif selection_radio == "CENTER_TOP_left":
            self.left_selected = ft.alignment.top_center
        elif selection_radio == "right_top_left":
            self.left_selected = ft.alignment.top_right
        elif selection_radio == "left_CENTER_LEFT":
            self.left_selected = ft.alignment.center_left
        elif selection_radio == "CENTER_LEFT":
            self.left_selected = ft.alignment.center
        elif selection_radio == "right_CENTER_LEFT":
            self.left_selected = ft.alignment.center_right
        elif selection_radio == "left_bottom_left":
            self.left_selected = ft.alignment.bottom_left
        elif selection_radio == "CENTER_BOTTOM_left":
            self.left_selected = ft.alignment.bottom_right
        elif selection_radio == "right_bottom_left":
            self.left_selected = ft.alignment.bottom_center

        # RIGHT SELECTION
        if selection_radio == "left_top_right":
            self.right_selected = ft.alignment.top_left
        elif selection_radio == "CENTER_TOP_right":
            self.right_selected = ft.alignment.top_center
        elif selection_radio == "right_top_right":
            self.right_selected = ft.alignment.top_right
        elif selection_radio == "right_CENTER_RIGHT":
            self.right_selected = ft.alignment.center_left
        elif selection_radio == "CENTER_RIGHT":
            self.right_selected = ft.alignment.center
        elif selection_radio == "right_CENTER_RIGHT":
            self.right_selected = ft.alignment.center_right
        elif selection_radio == "right_bottom_right":
            self.right_selected = ft.alignment.bottom_left
        elif selection_radio == "CENTER_BOTTOM_right":
            self.right_selected = ft.alignment.bottom_right
        elif selection_radio == "right_bottom_right":
            self.right_selected = ft.alignment.bottom_center

        self.widget_to_edit.update()

    def apply_gradient(self):
        global one_color, second_color, three_color, four_color
        class_name = self.widget_to_edit.__class__.__name__
        self.selected_list.clear()

        self.selected_list.append(ft.Colors(one_color if one_color else "transparent"))
        self.selected_list.append(ft.Colors(second_color if second_color else "cyan"))

        if not three_color == None:
            self.selected_list.append(
                ft.Colors(three_color if three_color else "transparent")
            )

        if not four_color == None:

            self.selected_list.append(
                ft.Colors(three_color if three_color else "transparent")
            )

        self.widget_to_edit.gradient = ft.LinearGradient(
            begin=self.left_selected,
            end=self.right_selected,
            colors=self.selected_list,
        )

        self.widget_to_edit.update()

    def cancel_gradient(self):
        self.widget_to_edit.gradient = None
        self.widget_to_edit.update()
