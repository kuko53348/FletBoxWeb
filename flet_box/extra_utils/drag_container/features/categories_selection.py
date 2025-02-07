import flet as ft


# CONTENT
class AnimatedSwitcher(ft.AnimatedSwitcher):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__(content=None)
        self.page = page
        self.transition = ft.AnimatedSwitcherTransition.SCALE
        self.duration = 500
        self.reverse_duration = 100
        self.switch_in_curve = ft.AnimationCurve.BOUNCE_OUT
        self.switch_out_curve = ft.AnimationCurve.BOUNCE_IN

    def build(self):

        self.animation_container_1 = ft.Container(
            ft.Text(
                value="Hello!",
            ),
            alignment=ft.alignment.center,
            width=200,
            height=200,
            bgcolor=ft.Colors.GREEN,
            on_click=lambda _: self.animate(widget=_.control.parent),
        )
        self.animation_container_2 = ft.Container(
            ft.Text(
                value="Bye!",
            ),
            alignment=ft.alignment.center,
            width=200,
            height=200,
            bgcolor=ft.Colors.BLUE,
            on_click=lambda _: self.animate(widget=_.control.parent),
        )
        self.content = self.animation_container_1

    def animate(self, widget: object = None):
        self.content = (
            self.animation_container_2
            if self.content == self.animation_container_1
            else self.animation_container_1
        )
        self.update()


class Checkbox(ft.Checkbox):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.label = "Normal Checkbox"
        self.label_position = ft.LabelPosition.RIGHT
        self.value = False


class RadioGroup(ft.RadioGroup):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__(content=None)
        self.page = page
        self.label = "Select RadioGroup"
        self.label_position = ft.LabelPosition.RIGHT
        self.value = "RadioGroup"

    def build(self):
        self.content = ft.Column(
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
        )


class RangeSlider(ft.RangeSlider):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__(start_value=0, end_value=100)
        self.page = page
        self.label = "Range Slider"

        self.min = 0
        self.max = 50
        self.divisions = 10
        self.start_value = 10
        self.end_value = 20
        self.inactive_color = ft.Colors.BLACK12
        self.active_color = ft.Colors.BLUE
        self.overlay_color = ft.Colors.YELLOW


class Slider(ft.Slider):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__(min=0, max=100)
        self.page = page
        self.label = "Range Slider"

        self.min = 0
        self.max = 50
        self.divisions = 10
        self.start_value = 10
        self.end_value = 20
        self.inactive_color = ft.Colors.BLACK12
        self.active_color = ft.Colors.BLUE
        self.overlay_color = ft.Colors.YELLOW


class Switch(ft.Switch):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.label = "Switch"
        self.value = False


# CONTROLS
class Dropdown(ft.Dropdown):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.label = "Select Dropdown"
        self.label_position = ft.LabelPosition.RIGHT
        self.value = "Dropdown"

    def build(self):
        self.options = [
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ]


# CUPERTINO CONTENT
class CupertinoCheckbox(ft.CupertinoCheckbox):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.label = "Cupertino Checkbox"
        self.label_position = ft.LabelPosition.RIGHT
        self.value = False


class CupertinoSwitch(ft.CupertinoSwitch):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.label = "Cupertino Switch"
        self.value = False


class CupertinoSlider(ft.CupertinoSlider):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__(min=0, max=100)
        self.page = page
        self.label = "CupertinoSlider"

        self.min = 0
        self.max = 50
        self.divisions = 10
        self.start_value = 10
        self.end_value = 20
        self.inactive_color = ft.Colors.BLACK12
        self.active_color = ft.Colors.BLUE
        self.overlay_color = ft.Colors.YELLOW


# CUPERTINO CONTROLS
