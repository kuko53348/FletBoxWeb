import flet as ft


class Button(ft.Button):

    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.text = "hello world dev"


class ElevatedButton(ft.ElevatedButton):

    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.text = "hello world dev"
        # self.on_click = event_manager


class FilledButton(ft.FilledButton):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page

        self.text = "hello world dev"
        # self.on_click = event_manager


class FilledTonalButton(ft.FilledTonalButton):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page

        self.text = "hello world dev"
        # self.on_click = event_manager


class OutlinedButton(ft.OutlinedButton):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page

        self.text = "hello world dev"
        # self.on_click = event_manager


class TextButton(ft.TextButton):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page

        self.text = "hello world dev"
        # self.on_click = event_manager


# =====================  CUPERTINO
class CupertinoButton(ft.CupertinoButton):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page

        self.text = "hello world dev"
        # self.on_click = event_manager


# =====================  ICONS
class FloatingActionButton(ft.FloatingActionButton):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page

        self.icon = ft.Icons.FAVORITE
        # self.on_click = event_manager


class IconButton(ft.IconButton):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page

        self.icon = ft.Icons.FAVORITE
        # self.on_click = event_manager


class Icon(ft.Icon):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.name = ft.Icons.FAVORITE
        # self.on_click = event_manager


# =====================  CONTROLS
class MenuItemButton(ft.MenuBar):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__(controls=list())
        self.page = page
        self.expand = True

    def build(self):
        self.controls = [
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
        # self.on_click = event_manager


class SegmentedButton(ft.SegmentedButton):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__(segments=list())
        self.page = page
        self.expand = True
        self.on_change = lambda e: print("MenuItemButton clicked!")
        self.selected_icon = ft.Icon(ft.Icons.ONETWOTHREE)
        self.selected = {"1", "4"}
        self.allow_multiple_selection = True

    def build(self):
        self.segments = [
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
        ]
        # self.on_click = event_manager


class CupertinoSegmentedButton(ft.CupertinoSegmentedButton):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__(controls=list())
        self.page = page
        self.expand = True
        self.on_change = lambda e: print("MenuItemButton clicked!")
        self.selected_color = ft.Colors.RED

    def build(self):
        self.controls = [
            ft.Text("One"),
            ft.Container(
                padding=ft.padding.symmetric(0, 30),
                content=ft.Text("Two"),
            ),
            ft.Container(
                padding=ft.padding.symmetric(0, 10),
                content=ft.Text("Three"),
            ),
        ]
        self.selected_index = 0


class CupertinoSlidingSegmentedButton(ft.CupertinoSlidingSegmentedButton):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__(controls=list())
        self.page = page
        self.expand = True
        self.thumb_color = ft.Colors("blue")
        # self.on_change = lambda e: print(f"selected_index: {e.data}")
        self.padding = ft.padding.symmetric(0, 10)

    def build(self):
        self.controls = [
            ft.Text("One"),
            ft.Text("Two"),
            ft.Text("Three"),
        ]
        self.selected_index = 0


class CupertinoContextMenu(ft.CupertinoContextMenu):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__(actions=list(), content=None)
        self.page = page
        self.expand = True
        self.enable_haptic_feedback = True
        # self.on_change = lambda e: print(f"selected_index: {e.data}")

    def build(self):
        self.content = ft.Image("splash.jpg")
        self.actions = [
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
        ]


class CupertinoActionSheet(ft.CupertinoActionSheet):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__(actions=list())
        self.page = page
        self.expand = True
        # self.on_change = lambda e: print(f"selected_index: {e.data}")

    def build(self):
        self.title = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text("Title"),
            ],
        )
        self.message = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text("Description"),
            ],
        )
        self.cancel = ft.CupertinoActionSheetAction(
            content=ft.Text("Cancel"),
        )
        self.actions = [
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
        ]


class SubmenuButton(ft.SubmenuButton):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__(controls=list())
        self.page = page
        self.expand = True
        # self.on_change = lambda e: print(f"selected_index: {e.data}")

    def build(self):
        self.content = ft.Text("BgColors")
        self.controls = [
            ft.CupertinoActionSheetAction(
                ft.SubmenuButton(
                    content=ft.Text("B"),
                    leading=ft.Icon(ft.Icons.COLORIZE),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("Blue"),
                            # style=ft.Button(bgcolor=ft.Colors("blue")),
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
        ]


# CONTENT
class PopupMenuButton(ft.PopupMenuButton):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page

    def build(self):
        self.content = ft.Row(
            controls=[
                ft.Icon(ft.Icons.HOURGLASS_TOP_OUTLINED),
                ft.Text("Item with a custom content"),
            ]
        )
        # self.on_click = event_manager


class CupertinoFilledButton(ft.CupertinoFilledButton):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.opacity_on_click = 0.3

    def build(self):
        self.content = ft.Text("CupertinoFilled")
        # self.on_click = event_manager
