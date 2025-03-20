import flet as ft

# categorie_navigations = widgets_by_categories.get("navigations")
# categorie_alerts = widgets_by_categories.get("alerts")
# categorie_text = widgets_by_categories.get("text")
# categorie_images = widgets_by_categories.get("images")
# categorie_selection = widgets_by_categories.get("selection")
# categorie_cupertino_selection = widgets_by_categories.get("cupertino selection")
# categorie_progress = widgets_by_categories.get("progress")
# categorie_charts = widgets_by_categories.get("charts")
# categorie_tables = widgets_by_categories.get("tables")
# categorie_tooltips = widgets_by_categories.get("tooltips")


# def layouts_witgets(get_widget: str = "", keys=True):

#     widget_dict = {}

#     if keys:
#         return widget_dict.get(get_widget)
#     else:
#         return widget_dict.keys()


def layouts_witgets(get_widget: str = "", keys=True):

    widget_dict = {
        "Divider": ft.Divider(
            height=1,
            color=ft.Colors.with_opacity(
                opacity=0.2,
                color=ft.Colors("white"),
            ),
            thickness=3,
        ),
        "VerticalDivider": ft.VerticalDivider(),
        # TABS
        "Tabs": ft.Tabs(height=450, tabs=[]),
        # NAVIGATIONS
        "NavigationRail": ft.Row(
            controls=[
                ft.NavigationRail(
                    height=800,
                    selected_index=0,
                    label_type=ft.NavigationRailLabelType.ALL,
                    extended=True,
                    min_width=50,
                    min_extended_width=100,
                    leading=ft.FloatingActionButton(icon=ft.Icons.CREATE, text="Add"),
                    group_alignment=-0.9,
                    destinations=[
                        ft.NavigationRailDestination(
                            label="First",
                            icon=ft.Icons.FAVORITE_BORDER,
                            selected_icon=ft.Icons.FAVORITE,
                        ),
                        ft.NavigationRailDestination(
                            label="Second",
                            icon=ft.Icon(ft.Icons.BOOKMARK_BORDER),
                            selected_icon=ft.Icon(ft.Icons.BOOKMARK),
                        ),
                        ft.NavigationRailDestination(
                            icon=ft.Icons.SETTINGS_OUTLINED,
                            selected_icon=ft.Icon(ft.Icons.SETTINGS),
                            label_content=ft.Text("Settings"),
                        ),
                    ],
                    # on_change=lambda e: print(
                    #     "Selected destination:", e.control.selected_index
                    # ),
                ),
            ]
        ),
        # LAYOUTS
        "Card": ft.Card(
            elevation=12,
            content=ft.Container(),
        ),
        "SafeArea": ft.SafeArea(content=ft.Text(value="Drop widget here is SafeArea")),
        "ResponsiveRow": ft.ResponsiveRow(),
        "Row": ft.Row(scroll=ft.ScrollMode.HIDDEN),
        "Column": ft.Column(scroll=ft.ScrollMode.HIDDEN),
        "Container": ft.Container(),
        "ListView": ft.ListView(),
        "GridView": ft.GridView(
            runs_count=2,
            run_spacing=4,
            padding=ft.padding.all(6),
        ),
        "Stack": ft.Stack(),
        "ExpansionPanelList": ft.ExpansionPanelList(),
        "ExpansionPanel": ft.ExpansionPanel(
            # has no header and content - placeholders will be used
            bgcolor=ft.Colors.BLUE_400,
            header=ft.ListTile(title=ft.Text(f"ExpansionPanel has controls")),
            expanded=True,
        ),
        "ExpansionTile": ft.ExpansionTile(
            title=ft.Text("ExpansionTile 1"),
            subtitle=ft.Text("Trailing expansion arrow icon"),
            affinity=ft.TileAffinity.PLATFORM,
            maintain_state=True,
            collapsed_text_color=ft.Colors.RED,
            text_color=ft.Colors.RED,
            controls=[],
        ),
        "ListTile": ft.ListTile(title=ft.Text("This is sub-tile number 3")),
    }

    if keys:
        return widget_dict.get(get_widget)
    else:
        return widget_dict.keys()


def buttons_witgets(get_widget: str = "", keys=True):
    md1 = """# Markdown Example Markdown allows you to easily include formatted text, images, and even formatted Dart code in your app.\n## Titles"""
    long_text = "Flet is a framework that allows building web, desktop and mobile applications in Python without prior experience in frontend development.\n\nYou can build a UI for your program with Flet controls which are based on Flutter by Google. Flet goes beyond merely wrapping Flutter widgets. It adds its own touch by combining smaller widgets, simplifying complexities, implementing UI best practices, and applying sensible defaults. This ensures that your applications look stylish and polished without requiring additional design efforts on your part."
    image = "image97.jpeg"
    same_image = ft.Image(
        src="logo.png",
        width=200,
        height=200,
        fit=ft.ImageFit.NONE,
        repeat=ft.ImageRepeat.NO_REPEAT,
        border_radius=ft.border_radius.all(10),
    )
    widget_dict = {
        "DatePicker": ft.ElevatedButton(
            text="Pick date",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date=datetime.datetime(year=2023, month=10, day=1),
                    last_date=datetime.datetime(year=2024, month=10, day=1),
                    # on_change=handle_change,
                    # on_dismiss=handle_dismissal,
                )
            ),
        ),
        "TimePicker": ft.ElevatedButton(
            text="Pick time",
            icon=ft.Icons.ACCESS_TIME_FILLED_ROUNDED,
            on_click=lambda e: page.open(
                ft.TimePicker(
                    confirm_text="Confirm",
                    error_invalid_text="Time out of range",
                    help_text="Pick your time slot",
                    # on_change=handle_change,
                    # on_dismiss=handle_dismissal,
                    # on_entry_mode_change=handle_entry_mode_change,
                )
            ),
        ),
        "AlertDialog": ft.ElevatedButton(
            text="Alert Dialog",
            icon=ft.Icons.ADD_ALERT_ROUNDED,
            on_click=lambda e: page.open(alert_dialog),
        ),
        "Banner": ft.ElevatedButton(
            text="Alert Barner",
            icon=ft.Icons.ADD_ALERT_ROUNDED,
            on_click=lambda e: page.open(alert_barner),
        ),
        "Markdown": ft.Markdown(
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            value=md1,
        ),
        "Text": ft.Text(
            value="Hello dev this is a text exemple",
            size=15,
            color=ft.Colors("white"),
            weight=ft.FontWeight.NORMAL,
        ),
        "TextField": ft.TextField(
            bgcolor="white12",
            label="TextField with icon",
            icon=ft.Icons.ACCOUNT_CIRCLE_ROUNDED,
            hint_text="Fill correct data",
            border_radius=ft.border_radius.all(12),
        ),
        # IMAGE
        "Image": ft.Image(
            src="logo.png",
            width=200,
            height=200,
            fit=ft.ImageFit.NONE,
            repeat=ft.ImageRepeat.NO_REPEAT,
            border_radius=ft.border_radius.all(10),
        ),
        "Same Image": same_image,
        "CircleAvatar": ft.Stack(
            width=40,
            height=40,
            controls=[
                ft.CircleAvatar(foreground_image_src=".my_avatar.png"),
                ft.Container(
                    content=ft.CircleAvatar(bgcolor=ft.Colors.YELLOW, radius=5),
                    alignment=ft.alignment.bottom_left,
                ),
            ],
        ),
        # BUTTONS
        "Button": ft.Button(
            text="hello world dev",
        ),
        "ElevatedButton": ft.ElevatedButton(
            text="hello world dev",
        ),
        "FilledButton": ft.FilledButton(
            text="hello world dev",
        ),
        "FilledTonalButton": ft.FilledTonalButton(
            text="hello world dev",
        ),
        "FloatingActionButton": ft.FloatingActionButton(
            icon=ft.Icons.FAVORITE,
        ),
        "IconButton": ft.IconButton(
            icon=ft.Icons.FAVORITE,
        ),
        "Icon": ft.Icon(
            name=ft.Icons.FAVORITE,
        ),
        "OutlinedButton": ft.OutlinedButton(
            text="hello world dev",
        ),
        # CONTROLS
        "MenuItemButton": ft.MenuBar(
            controls=[
                ft.SubmenuButton(
                    content=ft.Text("BgColors"),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("Blue"),
                            leading=ft.Icon(ft.Icons.COLORIZE),
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.HOVERED: ft.Colors("blue")}
                            ),
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("Green"),
                            leading=ft.Icon(ft.Icons.COLORIZE),
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN}
                            ),
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("Red"),
                            leading=ft.Icon(ft.Icons.COLORIZE),
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.HOVERED: ft.Colors.RED}
                            ),
                        ),
                    ],
                ),
            ]
        ),
        # CONTENT
        "PopupMenuButton": ft.PopupMenuButton(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.HOURGLASS_TOP_OUTLINED),
                    ft.Text("Item with a custom content"),
                ]
            ),
        ),
        "SubmenuButton": ft.MenuBar(
            controls=[
                ft.SubmenuButton(
                    content=ft.Text("BgColors"),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("Blue"),
                            leading=ft.Icon(ft.Icons.COLORIZE),
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.HOVERED: ft.Colors("blue")}
                            ),
                            # on_click=lambda e: print("MenuItemButton clicked!"),
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("Green"),
                            leading=ft.Icon(ft.Icons.COLORIZE),
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN}
                            ),
                            # on_click=lambda e: print("MenuItemButton clicked!"),
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("Red"),
                            leading=ft.Icon(ft.Icons.COLORIZE),
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.HOVERED: ft.Colors.RED}
                            ),
                            # on_click=lambda e: print("MenuItemButton clicked!"),
                        ),
                    ],
                ),
            ]
        ),
        "SegmentedButton": ft.SegmentedButton(
            expand=True,
            on_change=lambda e: print("MenuItemButton clicked!"),
            selected_icon=ft.Icon(ft.Icons.ONETWOTHREE),
            selected={"1", "4"},
            allow_multiple_selection=True,
            segments=[
                ft.Segment(
                    value="1",
                    label=ft.Text("1"),
                    icon=ft.Icon(ft.Icons.LOOKS_ONE),
                ),
                ft.Segment(
                    value="2",
                    label=ft.Text("2"),
                    icon=ft.Icon(ft.Icons.LOOKS_TWO),
                ),
                ft.Segment(
                    value="3",
                    label=ft.Text("3"),
                    icon=ft.Icon(ft.Icons.LOOKS_3),
                ),
                ft.Segment(
                    value="4",
                    label=ft.Text("4"),
                    icon=ft.Icon(ft.Icons.LOOKS_4),
                ),
            ],
        ),
        "TextButton": ft.TextButton(
            text="hello world dev",
        ),
    }

    if keys:
        return widget_dict.get(get_widget)
    else:
        return widget_dict.keys()


def cupertino_witgets(get_widget: str = "", keys=True):

    widget_dict = {
        "CupertinoTimerPicker": ft.CupertinoTimerPicker(
            value=3600,
            second_interval=10,
            minute_interval=1,
            mode=ft.CupertinoTimerPickerMode.HOUR_MINUTE_SECONDS,
            # on_change=handle_timer_picker_change,
        ),
        # CUPERTINO CONTENT
        "CupertinoFilledButton": ft.CupertinoFilledButton(
            opacity_on_click=0.3,
            content=ft.Text("CupertinoFilled"),
            # on_click = event_manager
        ),
        # CUPERTINO CONTROLS
        "CupertinoButton": ft.CupertinoButton(
            text="hello world dev",
        ),
        "CupertinoSegmentedButton": ft.CupertinoSegmentedButton(
            expand=True,
            on_change=lambda e: print("MenuItemButton clicked!"),
            selected_color=ft.Colors.RED,
            selected_index=0,
            controls=[
                ft.Text("One"),
                ft.Container(
                    padding=ft.padding.symmetric(0, 30),
                    content=ft.Text("Two"),
                ),
                ft.Container(
                    padding=ft.padding.symmetric(0, 10),
                    content=ft.Text("Three"),
                ),
            ],
        ),
        "CupertinoSlidingSegmentedButton": ft.CupertinoSlidingSegmentedButton(
            expand=True,
            selected_index=0,
            thumb_color=ft.Colors("blue"),
            padding=ft.padding.symmetric(0, 10),
            controls=[
                ft.Text(value="One"),
                ft.Text(value="Two"),
                ft.Text(value="Three"),
            ],
        ),
        "CupertinoContextMenu": ft.CupertinoContextMenu(
            enable_haptic_feedback=True,
            # expand=True,
            content=ft.Image(
                src="splash.jpg",
                width=100,
                height=100,
            ),
            actions=[
                ft.CupertinoContextMenuAction(
                    text="Action 1",
                    is_default_action=True,
                    trailing_icon=ft.Icons.CHECK,
                    # on_click=lambda e: print("Action 1"),
                ),
                ft.CupertinoContextMenuAction(
                    text="Action 2",
                    trailing_icon=ft.Icons.MORE,
                    # on_click=lambda e: print("Action 2"),
                ),
                ft.CupertinoContextMenuAction(
                    text="Action 3",
                    is_destructive_action=True,
                    trailing_icon=ft.Icons.CANCEL,
                    # on_click=lambda e: print("Action 3"),
                ),
            ],
        ),
        "CupertinoActionSheet": ft.CupertinoActionSheet(
            title=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text("Title"),
                ],
            ),
            message=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text("Description"),
                ],
            ),
            cancel=ft.CupertinoActionSheetAction(
                content=ft.Text("Cancel"),
            ),
            actions=[
                ft.CupertinoActionSheetAction(
                    content=ft.Text("Default Action"),
                    is_default_action=True,
                    # on_click=lambda e: print("Action 3"),
                ),
                ft.CupertinoActionSheetAction(
                    content=ft.Text("Normal Action"),
                    # on_click=lambda e: print("Action 3"),
                ),
                ft.CupertinoActionSheetAction(
                    content=ft.Text("Destructive Action"),
                    is_destructive_action=True,
                    # on_click=lambda e: print("Action 3"),
                ),
            ],
        ),
        "CupertinoTextField": ft.CupertinoTextField(
            placeholder_text="Placeholder", bgcolor=ft.Colors("black12")
        ),
    }

    if keys:
        return widget_dict.get(get_widget)
    else:
        return widget_dict.keys()


def charts_witgets(get_widget: str = "", keys=True):
    data_1 = [
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(1, 1),
                ft.LineChartDataPoint(3, 1.5),
                ft.LineChartDataPoint(5, 1.4),
                ft.LineChartDataPoint(7, 3.4),
                ft.LineChartDataPoint(10, 2),
                ft.LineChartDataPoint(12, 2.2),
                ft.LineChartDataPoint(13, 1.8),
            ],
            stroke_width=8,
            color=ft.Colors.LIGHT_GREEN,
            curved=True,
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(1, 1),
                ft.LineChartDataPoint(3, 2.8),
                ft.LineChartDataPoint(7, 1.2),
                ft.LineChartDataPoint(10, 2.8),
                ft.LineChartDataPoint(12, 2.6),
                ft.LineChartDataPoint(13, 3.9),
            ],
            color=ft.Colors.PINK,
            below_line_bgcolor=ft.Colors.with_opacity(0, ft.Colors.PINK),
            stroke_width=8,
            curved=True,
            stroke_cap_round=True,
        ),
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(1, 2.8),
                ft.LineChartDataPoint(3, 1.9),
                ft.LineChartDataPoint(6, 3),
                ft.LineChartDataPoint(10, 1.3),
                ft.LineChartDataPoint(13, 2.5),
            ],
            color=ft.Colors.CYAN,
            stroke_width=8,
            curved=True,
            stroke_cap_round=True,
        ),
    ]
    widget_dict = {  # CHARTS
        "BarChart": ft.BarChart(
            tooltip_bgcolor=ft.Colors.with_opacity(0.5, ft.Colors("grey300")),
            max_y=110,
            interactive=True,
            border=ft.border.all(1, ft.Colors("grey400")),
            expand=True,
            horizontal_grid_lines=ft.ChartGridLines(
                color=ft.Colors("grey300"), width=1, dash_pattern=[3, 3]
            ),
            bar_groups=[
                ft.BarChartGroup(
                    x=0,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=40,
                            width=40,
                            color=ft.Colors("amber"),
                            tooltip="Apple",
                            border_radius=0,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=1,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=100,
                            width=40,
                            color=ft.Colors("blue"),
                            tooltip="Blueberry",
                            border_radius=0,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=2,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=30,
                            width=40,
                            color=ft.Colors.RED,
                            tooltip="Cherry",
                            border_radius=0,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=3,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=60,
                            width=40,
                            color=ft.Colors.ORANGE,
                            tooltip="Orange",
                            border_radius=0,
                        ),
                    ],
                ),
            ],
            left_axis=ft.ChartAxis(
                labels_size=40, title=ft.Text("Fruit supply"), title_size=40
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=0, label=ft.Container(ft.Text("Apple"), padding=10)
                    ),
                    ft.ChartAxisLabel(
                        value=1,
                        label=ft.Container(ft.Text("Blueberry"), padding=10),
                    ),
                    ft.ChartAxisLabel(
                        value=2, label=ft.Container(ft.Text("Cherry"), padding=10)
                    ),
                    ft.ChartAxisLabel(
                        value=3, label=ft.Container(ft.Text("Orange"), padding=10)
                    ),
                ],
                labels_size=40,
            ),
        ),
        "LineChart": ft.LineChart(
            tooltip_bgcolor=ft.Colors.with_opacity(0.8, ft.Colors("bluegrey")),
            min_y=0,
            max_y=4,
            min_x=0,
            max_x=14,
            expand=True,
            border=ft.Border(
                bottom=ft.BorderSide(
                    4, ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE)
                )
            ),
            left_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=1,
                        label=ft.Text("1m", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=2,
                        label=ft.Text("2m", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=3,
                        label=ft.Text("3m", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=4,
                        label=ft.Text("4m", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=5,
                        label=ft.Text("5m", size=14, weight=ft.FontWeight.BOLD),
                    ),
                    ft.ChartAxisLabel(
                        value=6,
                        label=ft.Text("6m", size=14, weight=ft.FontWeight.BOLD),
                    ),
                ],
                labels_size=40,
            ),
            data_series=data_1,
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=2,
                        label=ft.Container(
                            ft.Text(
                                "SEP",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=7,
                        label=ft.Container(
                            ft.Text(
                                "OCT",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                    ft.ChartAxisLabel(
                        value=12,
                        label=ft.Container(
                            ft.Text(
                                "DEC",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                            ),
                            margin=ft.margin.only(top=10),
                        ),
                    ),
                ],
                labels_size=32,
            ),
        ),
        "PieChart": ft.PieChart(
            sections_space=1,
            center_space_radius=0,
            expand=True,
            # hovered_border = ft.BorderSide(6, ft.Colors("white"))
            # on_chart_event = lambda _: print(_)
            sections=[
                ft.PieChartSection(
                    25,
                    color=ft.Colors("blue"),
                    radius=80,
                    border_side=ft.BorderSide(
                        0, ft.Colors.with_opacity(0, ft.Colors("white"))
                    ),
                ),
                ft.PieChartSection(
                    25,
                    color=ft.Colors.YELLOW,
                    radius=65,
                    border_side=ft.BorderSide(
                        0, ft.Colors.with_opacity(0, ft.Colors("white"))
                    ),
                ),
                ft.PieChartSection(
                    25,
                    color=ft.Colors.PINK,
                    radius=60,
                    border_side=ft.BorderSide(
                        0, ft.Colors.with_opacity(0, ft.Colors("white"))
                    ),
                ),
                ft.PieChartSection(
                    25,
                    color=ft.Colors.GREEN,
                    radius=70,
                    border_side=ft.BorderSide(
                        0, ft.Colors.with_opacity(0, ft.Colors("white"))
                    ),
                ),
            ],
        ),
        "DataTable": ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("First name")),
                ft.DataColumn(ft.Text("Last name")),
                ft.DataColumn(ft.Text("Age"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Jack")),
                        ft.DataCell(ft.Text("Brown")),
                        ft.DataCell(ft.Text("19")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Alice")),
                        ft.DataCell(ft.Text("Wong")),
                        ft.DataCell(ft.Text("25")),
                    ],
                ),
            ],
        ),
    }

    if keys:
        return widget_dict.get(get_widget)
    else:
        return widget_dict.keys()


def selection_witgets(get_widget: str = "", keys=True):

    def animate(widget: object = None):
        animated_switcher.content = (
            animation_container_2
            if animated_switcher.content == animation_container_1
            else animation_container_1
        )

        animated_switcher.update()

    animation_container_1 = ft.Container(
        content=ft.Text(value="Hello!"),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.Colors.GREEN,
        on_click=lambda _: animate(widget=_.control.parent),
    )
    animation_container_2 = ft.Container(
        content=ft.Text(value="Bye!"),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.Colors("blue"),
        on_click=lambda _: animate(widget=_.control.parent),
    )

    animated_switcher = ft.AnimatedSwitcher(
        visible=True,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
        content=animation_container_1,
    )

    widget_dict = {
        "AnimatedSwitcher": animated_switcher,
        "Checkbox": ft.Checkbox(
            label="Normal Checkbox",
            label_position=ft.LabelPosition.RIGHT,
            value=False,
        ),
        "Dropdown": ft.Dropdown(
            width=320,
            label="Select Dropdown",
            # label_position=ft.LabelPosition.RIGHT,
            value="Dropdown",
            options=[
                ft.dropdown.Option("Red"),
                ft.dropdown.Option("Green"),
                ft.dropdown.Option("Blue"),
            ],
        ),
        "RadioGroup": ft.RadioGroup(
            # label="Select RadioGroup",
            # label_position=ft.LabelPosition.RIGHT,
            value="RadioGroup",
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                spacing=8,
                run_spacing=8,
                controls=[
                    ft.Radio(value="red", label="Red"),
                    ft.Radio(value="green", label="Green"),
                    ft.Radio(value="blue", label="Blue"),
                ],
            ),
        ),
        "RangeSlider": ft.RangeSlider(
            label="Range Slider",
            min=0,
            max=50,
            divisions=10,
            start_value=10,
            end_value=20,
            inactive_color=ft.Colors("black12"),
            active_color=ft.Colors("blue"),
            overlay_color=ft.Colors.YELLOW,
        ),
        "Slider": ft.Slider(
            label="Range Slider",
            min=0,
            max=50,
            divisions=10,
            # start_value=10,
            # end_value=20,
            inactive_color=ft.Colors("black12"),
            active_color=ft.Colors("blue"),
            overlay_color=ft.Colors.YELLOW,
        ),
        "Switch": ft.Switch(label="Switch", value=False),
        # CUPERTINO SELECTION
        "CupertinoCheckbox": ft.CupertinoCheckbox(
            label="Cupertino Checkbox",
            label_position=ft.LabelPosition.RIGHT,
            value=False,
        ),
        "CupertinoSlider": ft.CupertinoSlider(
            min=0,
            max=50,
            divisions=10,
        ),
        "CupertinoSwitch": ft.CupertinoSwitch(
            label="Cupertino Switch",
            value=True,
        ),
        # PROGRESS
        "ProgressBar": ft.ProgressBar(
            width=400, color=ft.Colors("yellow"), bgcolor=ft.Colors("black12")
        ),
        "ProgressRing": ft.ProgressRing(
            width=16,
            height=16,
            stroke_width=2,
            color=ft.Colors("yellow"),
            bgcolor=ft.Colors("black12"),
        ),
    }

    if keys:
        return widget_dict.get(get_widget)
    else:
        return widget_dict.keys()
