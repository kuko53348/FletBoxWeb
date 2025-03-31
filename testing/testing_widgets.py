import flet as ft

medium_text = "Flet is a framework that allows building web, desktop and mobile applications in Python without prior experience in frontend development."
long_text = "Flet is a framework that allows building web, desktop and mobile applications in Python without prior experience in frontend development.\n\nYou can build a UI for your program with Flet controls which are based on Flutter by Google. Flet goes beyond merely wrapping Flutter widgets. It adds its own touch by combining smaller widgets, simplifying complexities, implementing UI best practices, and applying sensible defaults. This ensures that your applications look stylish and polished without requiring additional design efforts on your part."
few_medium_text = (
    "Flet is a framework that allows building web, desktop and mobile applications"
)


class get_attr_from_widget:
    filter_deprecated = [
        "event_handlers",
        "icon_size",
        "icon_enabled_color",
        "icon_disabled_color",
        "icon_content",
        "self",
        "args",
        "kwargs",
        "rtl",
        "image_src",
        "image_repeat",
        "image_opacity",
        "image_src_base64",
        "image_fit",
        "tooltip",
        "content",
        "controls",
        "tabs",
        "parent",
        "n",
        "selected_index",
        "on_hover",
        # "on_click",
        "on_change",
        "on_long_press",
        "on_will_accept",
        "on_accept",
        "on_leave",
        "page",
    ]

    def __init__(self, page: object = None, widget: object = None) -> list:
        self.page = page
        widget_object = widget
        self.get_attribute_from(target=widget_object)

    def get_attribute_from(self, target: object = None) -> list:
        widget = target

        for attr in dir(widget):
            if attr in self.filter_deprecated:
                continue

            if not attr.startswith("_") and not callable(getattr(widget, attr)):
                value = getattr(widget, attr)

                data_type = type(value)
                # print(attr, value)
                print(f"[+]>>> {attr}= {value}")


class bool_widget(ft.Row):

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


class get_aligment(ft.Row):
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

        start = ["start", "vertical_align_top_rounded"]
        end = ["end", "vertical_align_center_rounded"]
        center = ["center", "vertical_align_bottom_rounded"]
        space_between = ["between", "vertical_distribute_rounded"]
        space_around = ["around", "format_line_spacing"]
        space_evenly = ["evenly", "menu_rounded"]

        self.controls = [
            ft.Text(
                value=self.tag_edit_widget,
                text_align=ft.TextAlign.CENTER,
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
                        ft.Icon(name=start[1]),
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
                        ft.Icon(name=end[1]),
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
                        ft.Icon(name=center[1]),
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
                        ft.Icon(name=space_between[1]),
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
                        ft.Icon(name=space_around[1]),
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
                        ft.Icon(name=space_evenly[1]),
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
        # setattr(self.widget_to_edit, self.tag_edit_widget, payload.control.value)
        self.widget_to_edit.update()


class get_linear_gradient(ft.Column):
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

        # self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        # self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        # self.run_alignment = ft.CrossAxisAlignment.START
        # self.spacing = 8
        # self.run_spacing = 8

        start = ["start", "circle"]
        end = ["end", "circle"]
        center = ["center", "circle"]
        space_between = ["between", "circle"]
        space_around = ["around", "circle"]
        space_evenly = ["evenly", "circle"]

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
                                content=ft.Column(
                                    spacing=5,
                                    run_spacing=18,
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Radio(
                                                    value="left_top",
                                                    fill_color=ft.Colors.YELLOW_200,
                                                    active_color=ft.Colors.RED,
                                                ),
                                                ft.Radio(
                                                    value="center_top",
                                                    fill_color=ft.Colors.BLUE_200,
                                                    active_color=ft.Colors.BLACK,
                                                ),
                                                ft.Radio(
                                                    value="right_top",
                                                    fill_color=ft.Colors.GREEN_200,
                                                    active_color=ft.Colors.CYAN,
                                                ),
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Radio(
                                                    value="left_center",
                                                    fill_color=ft.Colors.YELLOW_500,
                                                    active_color=ft.Colors.RED,
                                                ),
                                                ft.Radio(
                                                    value="center",
                                                    fill_color=ft.Colors.BLUE_500,
                                                    active_color=ft.Colors.BLACK,
                                                ),
                                                ft.Radio(
                                                    value="right_center",
                                                    fill_color=ft.Colors.GREEN_500,
                                                    active_color=ft.Colors.CYAN,
                                                ),
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Radio(
                                                    value="left_bottom",
                                                    fill_color=ft.Colors.YELLOW_800,
                                                    active_color=ft.Colors.RED,
                                                ),
                                                ft.Radio(
                                                    value="center_bottom",
                                                    fill_color=ft.Colors.BLUE_800,
                                                    active_color=ft.Colors.BLACK,
                                                ),
                                                ft.Radio(
                                                    value="right_bottom",
                                                    fill_color=ft.Colors.GREEN_800,
                                                    active_color=ft.Colors.CYAN,
                                                ),
                                            ]
                                        ),
                                    ],
                                )
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
                                content=ft.Column(
                                    spacing=5,
                                    run_spacing=18,
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Radio(
                                                    value="left_top",
                                                    fill_color=ft.Colors.YELLOW_200,
                                                    active_color=ft.Colors.RED,
                                                ),
                                                ft.Radio(
                                                    value="center_top",
                                                    fill_color=ft.Colors.BLUE_200,
                                                    active_color=ft.Colors.BLACK,
                                                ),
                                                ft.Radio(
                                                    value="right_top",
                                                    fill_color=ft.Colors.GREEN_200,
                                                    active_color=ft.Colors.CYAN,
                                                ),
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Radio(
                                                    value="left_center",
                                                    fill_color=ft.Colors.YELLOW_500,
                                                    active_color=ft.Colors.RED,
                                                ),
                                                ft.Radio(
                                                    value="center",
                                                    fill_color=ft.Colors.BLUE_500,
                                                    active_color=ft.Colors.BLACK,
                                                ),
                                                ft.Radio(
                                                    value="right_center",
                                                    fill_color=ft.Colors.GREEN_500,
                                                    active_color=ft.Colors.CYAN,
                                                ),
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Radio(
                                                    value="left_bottom",
                                                    fill_color=ft.Colors.YELLOW_800,
                                                    active_color=ft.Colors.RED,
                                                ),
                                                ft.Radio(
                                                    value="center_bottom",
                                                    fill_color=ft.Colors.BLUE_800,
                                                    active_color=ft.Colors.BLACK,
                                                ),
                                                ft.Radio(
                                                    value="right_bottom",
                                                    fill_color=ft.Colors.GREEN_800,
                                                    active_color=ft.Colors.CYAN,
                                                ),
                                            ]
                                        ),
                                    ],
                                )
                            ),
                        ],
                    ),
                ],
            ),
            get_four_numers(
                page=page,
                tag_edit_widget="colors gradient",
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
                    ft.ElevatedButton(icon="save", text="Apply", bgcolor="green900"),
                    ft.ElevatedButton(icon="cancel", text="Cancel", bgcolor="red900"),
                ],
            ),
        ]


class get_aligment_container(ft.Row):
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
                content=ft.Column(
                    spacing=5,
                    run_spacing=18,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Radio(
                                    value="left_top",
                                    fill_color=ft.Colors.YELLOW_200,
                                    active_color=ft.Colors.RED,
                                ),
                                ft.Radio(
                                    value="center_top",
                                    fill_color=ft.Colors.BLUE_200,
                                    active_color=ft.Colors.BLACK,
                                ),
                                ft.Radio(
                                    value="right_top",
                                    fill_color=ft.Colors.GREEN_200,
                                    active_color=ft.Colors.CYAN,
                                ),
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.Radio(
                                    value="left_center",
                                    fill_color=ft.Colors.YELLOW_500,
                                    active_color=ft.Colors.RED,
                                ),
                                ft.Radio(
                                    value="center",
                                    fill_color=ft.Colors.BLUE_500,
                                    active_color=ft.Colors.BLACK,
                                ),
                                ft.Radio(
                                    value="right_center",
                                    fill_color=ft.Colors.GREEN_500,
                                    active_color=ft.Colors.CYAN,
                                ),
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.Radio(
                                    value="left_bottom",
                                    fill_color=ft.Colors.YELLOW_800,
                                    active_color=ft.Colors.RED,
                                ),
                                ft.Radio(
                                    value="center_bottom",
                                    fill_color=ft.Colors.BLUE_800,
                                    active_color=ft.Colors.BLACK,
                                ),
                                ft.Radio(
                                    value="right_bottom",
                                    fill_color=ft.Colors.GREEN_800,
                                    active_color=ft.Colors.CYAN,
                                ),
                            ]
                        ),
                    ],
                )
            ),
        ]


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

        start = ["start", "vertical_align_top_rounded"]
        end = ["end", "vertical_align_center_rounded"]
        center = ["center", "vertical_align_bottom_rounded"]

        self.controls = [
            ft.Text(
                value=self.tag_edit_widget,
                text_align=ft.TextAlign.CENTER,
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
                        ft.Icon(name=start[1]),
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
                        ft.Icon(name=end[1]),
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
                        ft.Icon(name=center[1]),
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
        # setattr(self.widget_to_edit, self.tag_edit_widget, payload.control.value)
        self.widget_to_edit.update()


class get_one_string_with_slider(ft.Row):

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
                width=80,
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
                    ft.Slider(expand=True, min=0, max=100),
                ],
            ),
        ]

    def set_attribute(self, payload: object = None, label: str = "") -> None:
        self.l_value = payload.control.value

        if self.tag_edit_widget == "image":
            setattr(
                self.widget_to_edit,
                "image",
                self.l_value,
            )

        self.widget_to_edit.update()


class get_one_string_with_button(ft.Row):

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

        if self.tag_edit_widget == "image":
            setattr(
                self.widget_to_edit,
                "image",
                self.l_value,
            )

        self.widget_to_edit.update()


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

        check_if_is_not_none_value = getattr(
            self.widget_to_edit, tag_edit_widget, tag_edit_widget
        )

        if check_if_is_not_none_value:
            if tag_edit_widget == "tooltip":
                self.l_value = None

        else:
            if self.tag_edit_widget == "tooltip":
                setattr(self.widget_to_edit, "tooltip", tag_edit_widget)

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
        self.l_value = payload.control.value

        if self.tag_edit_widget == "tooltip":
            setattr(
                self.widget_to_edit,
                "tooltip",
                self.l_value,
            )

        self.widget_to_edit.update()


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

        elif label == "r":
            self.r_value = payload.control.value

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

        elif label == "r":
            self.r_value = payload.control.value

        elif label == "u":
            self.t_value = payload.control.value

        elif label == "d":
            self.b_value = payload.control.value

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


class main_edit_container(ft.Container):
    # Generic Container

    def __init__(self, page: object = None, content: object = None) -> None:
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
        self.padding = ft.padding.only(left=12, right=8, bottom=0, top=0)
        self.ink = True
        self.bgcolor = ft.Colors.with_opacity(opacity=0.05, color=ft.colors("white"))
        self.alignment = ft.alignment.center
        self.ink_color = ft.colors("yellow")

        self.content = content


if __name__ == "__main__":
    bool_dict = [
        "disabled",
        "expand",
        "expand_loose",
        "ignore_interactions",
        "ink",
        "visible",
    ]
    one_buttom_dict = [
        "image",
    ]
    one_dict = [
        "offset",
    ]
    two_dict = [
        "offset",
    ]
    four_dict = [
        "padding",
        "margin",
        "border_radius",
    ]

    def main(page: ft.Page):

        widget_exemple = ft.Container(
            width=300,
            height=150,
            border_radius=ft.border_radius.all(32),
            padding=ft.padding.all(20),
            bgcolor=ft.Colors("white"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(
                src="apple.png",
                fit="cover",
                opacity=0.18,
            ),
            content=ft.Column(
                controls=[
                    # Business Name
                    ft.Text(
                        value="Tech Solutions Inc.",
                        size=26,
                        weight=ft.FontWeight.W_900,
                        color=ft.Colors("grey800"),
                    ),
                    # Contact Info
                    ft.Text(
                        value="Email: info@techsolutions.com",
                        size=16,
                        weight=ft.FontWeight.W_500,
                        color=ft.Colors("grey600"),
                    ),
                    ft.Text(
                        value="Phone: +1 234 567 890",
                        size=16,
                        color=ft.Colors("grey600"),
                        weight=ft.FontWeight.W_900,
                    ),
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )  # <

        widget_data = ft.Container(
            expand=True,
            padding=ft.padding.only(left=12, top=12, right=12, bottom=12),
            border_radius=ft.border_radius.all(12),
            bgcolor=ft.Colors("grey900"),
            image=ft.DecorationImage(src="amazon.jpg", fit="cover", opacity=0.18),
            content=ft.Column(
                controls=[
                    main_edit_container(
                        page=page,
                        content=get_linear_gradient(
                            page=page,
                            tag_edit_widget="linear_gradient",
                            widget_to_edit=widget_exemple,
                        ),
                    ),
                    # main_edit_container(
                    #     page=page,
                    #     content=bool_widget(
                    #         page=page,
                    #         tag_edit_widget="expand",
                    #         widget_to_edit=widget_exemple,
                    #     ),
                    # ),
                    # main_edit_container(
                    #     page=page,
                    #     content=get_one_string_with_slider(
                    #         page=page,
                    #         tag_edit_widget="aligment",
                    #         widget_to_edit=widget_exemple,
                    #     ),
                    # ),
                    # main_edit_container(
                    #     page=page,
                    #     content=get_aligment_container(
                    #         page=page,
                    #         tag_edit_widget="aligment",
                    #         widget_to_edit=widget_exemple,
                    #     ),
                    # ),
                    # main_edit_container(
                    #     page=page,
                    #     content=get_aligment(
                    #         page=page,
                    #         tag_edit_widget="aligment",
                    #         widget_to_edit=widget_exemple,
                    #     ),
                    # ),
                    # main_edit_container(
                    #     page=page,
                    #     content=get_one_string_with_button(
                    #         page=page,
                    #         tag_edit_widget="image",
                    #         widget_to_edit=widget_exemple,
                    #     ),
                    # ),
                    # main_edit_container(
                    #     page=page,
                    #     content=get_one_string(
                    #         page=page,
                    #         tag_edit_widget="tooltip",
                    #         widget_to_edit=widget_exemple,
                    #     ),
                    # ),
                    # main_edit_container(
                    #     page=page,
                    #     content=get_two_numers(
                    #         page=page,
                    #         tag_edit_widget="offset",
                    #         widget_to_edit=widget_exemple,
                    #     ),
                    # ),
                    # main_edit_container(
                    #     page=page,
                    #     content=get_four_numers(
                    #         page=page,
                    #         tag_edit_widget="padding",
                    #         widget_to_edit=widget_exemple,
                    #     ),
                    # ),
                    widget_exemple,
                ]
            ),
        )

        page.window.width = 410
        page.window.height = 600
        # page.scroll = ft.ScrollMode.HIDDEN
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.add(widget_exemple)  #
        # page.add(widget_data)  # dragger widgets
        page.update()

    ft.app(target=main)
