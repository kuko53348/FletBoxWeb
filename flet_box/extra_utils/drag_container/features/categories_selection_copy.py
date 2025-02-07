import flet as ft

# ANIMATION CONTAINER
animation_container_1 = (
    ft.Container(
        ft.Text(
            value="Hello!",
        ),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.Colors.GREEN,
        on_click=lambda _: animate(widget=_.control.parent),
    ),
)
animation_container_2 = (
    ft.Container(
        ft.Text(
            value="Bye!",
        ),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.Colors.BLUE,
        on_click=lambda _: animate(widget=_.control.parent),
    ),
)
# CONTENT
AnimatedSwitcher = ft.AnimatedSwitcher(
    transition=ft.AnimatedSwitcherTransition.SCALE,
    duration=500,
    reverse_duration=100,
    switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
    switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    content=animation_container_1,
)


def animate(self, widget: object = None):
    content = (
        animation_container_2
        if content == animation_container_1
        else animation_container_1
    )
    update()


# END ANIMATION CONTAINER

Checkbox = ft.Checkbox(
    label="Normal Checkbox", label_position=ft.LabelPosition.RIGHT, value=False
)


RadioGroup = ft.RadioGroup(
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
)


RangeSlider = ft.RangeSlider(
    label="Range Slider",
    min=0,
    max=50,
    divisions=10,
    start_value=10,
    end_value=20,
    inactive_color=ft.Colors.BLACK12,
    active_color=ft.Colors.BLUE,
    overlay_color=ft.Colors.YELLOW,
)

Slider = ft.Slider(
    label="Range Slider",
    min=0,
    max=50,
    divisions=10,
    # start_value=10,
    # end_value=20,
    inactive_color=ft.Colors.BLACK12,
    active_color=ft.Colors.BLUE,
    overlay_color=ft.Colors.YELLOW,
)


Switch = ft.Switch(label="Switch", value=False)

# CONTROLS
Dropdown = ft.Dropdown(
    label="Select Dropdown",
    # label_position=ft.LabelPosition.RIGHT,
    value="Dropdown",
    options=[
        ft.dropdown.Option("Red"),
        ft.dropdown.Option("Green"),
        ft.dropdown.Option("Blue"),
    ],
)


# CUPERTINO CONTENT
CupertinoCheckbox = ft.CupertinoCheckbox(
    label="Cupertino Checkbox",
    label_position=ft.LabelPosition.RIGHT,
    value=False,
)


CupertinoSwitch = ft.CupertinoSwitch(
    label="Cupertino Switch",
    value=False,
    label_position=ft.LabelPosition.RIGHT,
)


CupertinoSlider = ft.CupertinoSlider(
    # label="CupertinoSlider",
    min=0,
    max=50,
    divisions=10,
    # start_value=10,
    # end_value=20,
    # inactive_color=ft.Colors.BLACK12,
    # active_color=ft.Colors.BLUE,
    # overlay_color=ft.Colors.YELLOW,
)


# CUPERTINO CONTROLS
