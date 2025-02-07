import flet as ft


Button = ft.Button(
    text="hello world dev",
)


ElevatedButton = ft.ElevatedButton(
    text="hello world dev",
)


FilledButton = ft.FilledButton(
    text="hello world dev",
)


FilledTonalButton = ft.FilledTonalButton(
    text="hello world dev",
)


OutlinedButton = ft.OutlinedButton(
    text="hello world dev",
)


TextButton = ft.TextButton(text="hello world dev")


# =====================  CUPERTINO
CupertinoButton = ft.CupertinoButton(
    text="hello world dev",
)


# =====================  ICONS
FloatingActionButton = ft.FloatingActionButton(
    icon=ft.Icons.FAVORITE,
)


IconButton = ft.IconButton(
    icon=ft.Icons.FAVORITE,
)


Icon = ft.Icon(
    name=ft.Icons.FAVORITE,
)


# =====================  CONTROLS
MenuItemButton = ft.MenuBar(
    controls=[
        ft.SubmenuButton(
            content=ft.Text("BgColors"),
            controls=[
                ft.MenuItemButton(
                    content=ft.Text("Blue"),
                    leading=ft.Icon(ft.Icons.COLORIZE),
                    style=ft.ButtonStyle(
                        bgcolor={ft.ControlState.HOVERED: ft.Colors.BLUE}
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
)


SegmentedButton = ft.SegmentedButton(
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
)


CupertinoSegmentedButton = ft.CupertinoSegmentedButton(
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
)


CupertinoSlidingSegmentedButton = ft.CupertinoSlidingSegmentedButton(
    expand=True,
    selected_index=0,
    thumb_color=ft.Colors.BLUE,
    padding=ft.padding.symmetric(0, 10),
    controls=[
        ft.Text("One"),
        ft.Text("Two"),
        ft.Text("Three"),
    ],
)


CupertinoContextMenu = ft.CupertinoContextMenu(
    enable_haptic_feedback=True,
    # expand=True,
    content=ft.Image("splash.jpg"),
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
)


CupertinoActionSheet = ft.CupertinoActionSheet(
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
)


SubmenuButton = ft.SubmenuButton(
    content=ft.Text("BgColors"),
    controls=[
        ft.CupertinoActionSheetAction(
            ft.SubmenuButton(
                content=ft.Text("B"),
                leading=ft.Icon(ft.Icons.COLORIZE),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Blue"),
                        # style=ft.Button(bgcolor=ft.Colors.BLUE),
                    )
                ],
            ),
            ft.SubmenuButton(
                content=ft.Text("G"),
                leading=ft.Icon(ft.Icons.COLORIZE),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Green"),
                        # style=ft.Button(bgcolor=ft.Colors.GREEN),
                    )
                ],
            ),
            ft.SubmenuButton(
                content=ft.Text("R"),
                leading=ft.Icon(ft.Icons.COLORIZE),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Red"),
                        # style=ft.Button(bgcolor=ft.Colors.RED),
                    )
                ],
            ),
        ),
    ],
)


# CONTENT
PopupMenuButton = ft.PopupMenuButton(
    content=ft.Row(
        controls=[
            ft.Icon(ft.Icons.HOURGLASS_TOP_OUTLINED),
            ft.Text("Item with a custom content"),
        ]
    ),
)


CupertinoFilledButton = ft.CupertinoFilledButton(
    opacity_on_click=0.3,
    content=ft.Text("CupertinoFilled"),
    # on_click = event_manager
)
