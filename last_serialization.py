import flet as ft
from typing import Any, List, Dict, Set, Deque, Optional


def serialize_widget(widget, indent=0):
    """Serialize Flet widget tree into a human-readable format with all attributes."""
    spacing = "  " * indent

    class_name = widget.__class__.__name__

    result = f"{spacing}ft.{class_name}(\n"

    # Gather attributes
    attributes = []

    # print("============================")
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
        "actions",
    ]
    for attr in dir(widget):
        # try:
        if attr in filter_deprecated:
            continue

            # print(attr, "<<<<<<<<<<<<<<<<<<<<<,")
        if not attr.startswith("_") and not callable(getattr(widget, attr)):
            value = getattr(widget, attr)

            data_type = type(value)

            if (
                not value == False and not value == None
            ):  #  and not value == True  add if want remove True

                if (
                    not data_type == type(False)
                    and not data_type == type(str())
                    and not data_type == type(list())
                    and not data_type == type(tuple())
                    and not data_type == type(dict())
                    and not data_type == type(set())
                    and not data_type == type(float())
                    and not data_type == type(int())
                    and not data_type == type(None)
                ):
                    # print("--------------- here ------------------")

                    if isinstance(value, list):
                        value_str = f"[{', '.join(repr(v) for v in value)}]"
                    else:
                        value = _format_value(value)

                        if isinstance(value, ft.colors) or isinstance(value, ft.Colors):
                            value_str = f"Colors('{value.name.lower()}')"

                        elif isinstance(value, ft.MainAxisAlignment):
                            value_str = f"{value}"

                        elif isinstance(value, ft.CrossAxisAlignment):
                            value_str = f"{value}"

                        elif isinstance(value, ft.ScrollMode):
                            value_str = f"{value}"

                        elif isinstance(value, ft.CupertinoTimerPickerMode):
                            value_str = f"{value}"

                        elif isinstance(value, ft.Icons):
                            value_str = f"{value}"

                        elif isinstance(value, ft.FontWeight):
                            value_str = f"{value}"

                        else:
                            value_str = repr(value)

                    format_data = f"{spacing*2}{attr}=ft.{value_str}"
                    attributes.append(format_data)

                else:
                    if isinstance(value, list):
                        value_str = f"[{', '.join(repr(v) for v in value)}]"
                    else:
                        value_str = repr(value)

                    attributes.append(f"{spacing*2}{attr}={value_str}")
        # except Exception as e:
        #     print(f"[+] error: add [{e}] in filter_deprecated = [{e}]")

    # Add attributes to result
    if attributes:
        result += f"" + ",\n".join(attributes) + ",\n"

    # Serialize controls
    if hasattr(widget, "controls") and isinstance(widget.controls, list):
        result += f"{spacing}  controls=[\n"
        for child in widget.controls:
            result += serialize_widget(child, indent + 2)
        result += f"{spacing}  ],\n"

    # Special handling for TabControl and ListView
    if isinstance(widget, ft.Tabs):
        result += f"{spacing}  tabs=[\n"
        for tab in widget.tabs:
            result += f"{spacing}    Tab(text='{tab.text}', content=\n"
            result += serialize_widget(tab.content, indent + 3)
            result += f"{spacing}    ),\n"

        result += f"{spacing}  ],\n"

    elif isinstance(widget, ft.ListView):
        result += f"{spacing}  items=[\n"
        for item in widget.controls:
            result += f"{spacing}    ListTile(title={serialize_widget(item.title, indent + 3)}),\n"
        result += f"{spacing}  ],),\n"

    if isinstance(widget, ft.RadioGroup):
        print(widget.content.controls)
        result += f"{spacing}  content=ft.Column(\n"
        result += f"{spacing}  controls=[\n"
        for radio in widget.content.controls:
            result += f"{spacing*2}    ft.Radio(value='{radio.value}', content='{radio.label}'),\n"

        result += f"{spacing}    ],\n{spacing}  ),\n"

    # Additional handling for segments and actions
    if hasattr(widget, "segments"):
        segments = getattr(widget, "segments")
        if segments:
            result += f"{spacing}  segments=[\n"
            for segment in segments:
                result += f"{spacing}    {repr(segment)},\n"
            result += f"{spacing}  ],\n"

    if hasattr(widget, "actions"):
        actions = getattr(widget, "actions")
        if actions:
            result += f"{spacing}  actions=[\n"
            for action in actions:
                result += f"{spacing}    {repr(action)},\n"
            result += f"{spacing}  ],\n"

    if isinstance(widget, ft.Container):
        result += f"{spacing}  content={serialize_widget(widget.content, indent+1 )}"

    result += f"{spacing}),\n"
    return result


def write_to_file(data, filename):
    """Write serialized data to a Python file."""
    with open(filename, "w") as file:
        file.write(data)


def _format_value(value: Any, indent_level: int = 4) -> str:
    # """Comprehensive value formatting"""
    if isinstance(value, ft.Border):
        value.top.color = f"ft.{value.top.color}".split(".")[2].lower()
        return value

    if isinstance(value, ft.LinearGradient):
        value.tile_mode = f"{value.tile_mode}".split(" ")[0].split(".")[1].lower()
        value.colors = [_.split(" ")[0] for _ in value.colors]
        return value

    if isinstance(value, ft.BoxShadow):
        value.blur_style = f"{value.blur_style}".split(" ")[0].split(".")[1].lower()
        value.color = f"{value.color}".split(" ")[0].split(".")[1].lower()
        return value

    if isinstance(value, ft.DecorationImage):
        value.fit = f"{value}"

    if isinstance(value, ft.ButtonStyle):
        value.bgcolor = (
            f"{value.bgcolor}".split(" ")[0].split(".")[1].lower().strip(":")
        )
        value.padding = (
            f"{value.padding}".split(" ")[0].split(".")[1].lower().strip(":")
        )
        value.side = f"{value.side}".split(" ")[0].split(".")[1].lower().strip(":")
        value.shape = f"{value.shape}".split(" ")[0].split(".")[1].lower().strip(":")
        value.text_style = (
            f"{value.text_style}".split(" ")[0].split(".")[1].lower().strip(":")
        )
        return value

    return value
    # if isinstance(value, ft.Container):
    #     value.bgcolor = "red"
    #     return value

    # if isinstance(value, ft.Control):
    # return self.declared.get(self._get_widget_uid(value), "None")

    # if isinstance(value, ft.colors):
    #     return f"ft.colors('{value.name.lower()}')"

    # if isinstance(value, ft.Colors):
    #     return f"ft.Colors('{value.name.lower()}')"

    # if isinstance(value, ft.CupertinoColors):
    #     return f"ft.Colors('{value.name.lower()}')"

    # if isinstance(value, ft.Blur):
    #     value.tile_mode = f"{value.tile_mode}".split(" ")[0].split(".")[1].lower()
    #     return value

    # if isinstance(value, ft.ImageFit):
    #     return f"ft.ImageFit('{value.name.lower()}')"

    # if isinstance(value, ft.Icon):
    #     return f"ft.icons('{value.icons.lower()}')"

    # if isinstance(value, ft.Alignment):
    #     return f"ft.alignment.Alignment({value.x}, {value.y})"

    # # if isinstance(value, ft.GradientTileMode):
    # #     return f"ft.GradientTileMode('{value.lower()}')"

    # if isinstance(value, ft.LinearGradient):
    #     value.tile_mode = f"{value.tile_mode}".split(" ")[0].split(".")[1].lower()
    #     value.colors = [_.split(" ")[0] for _ in value.colors]
    #     return value

    # if isinstance(value, ft.Border):
    # return f"ft.border.all({value.width}, {self._format_value(value.color, 0)})"
    #     value.top.color = f"ft.{value.top.color}".split(".")[2].lower()
    #     # value.bottom.color = f"ft.{value.bottom.color}"
    #     # value.right.color = f"ft.{value.right.color}"
    #     # value.left.color = f"ft.{value.left.color}"
    #     return value

    # # if isinstance(value, ft.Padding):
    # #     return f"{value.padding}"

    # if isinstance(value, ft.TextStyle):
    #     value.weight = (
    #         f"ft.{value.weight}".split(".")[1].lower() if value.weight else None
    #     )
    #     value.shadow.color = (
    #         f"ft.{value.shadow.color}".split(".")[2].lower()
    #         if value.shadow.color
    #         else None
    #     )
    #     value.shadow.blur_style = (
    #         f"ft.{value.shadow.blur_style}".split(".")[2].lower()
    #         if value.shadow.blur_style
    #         else None
    #     )
    #     return f"ft.{value}"


if __name__ == "__main__":

    def main(page: ft.Page):
        # Serialize the widget structure and write it to a file
        # src="./flet_box/assets/splash.png",
        # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        # vertical_alignment=ft.CrossAxisAlignment.CENTER,
        # horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        widget_data = ft.Container(
            # height=80,
            padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
            border_radius=ft.border_radius.all(32),
            bgcolor=ft.Colors("black45"),
            content=ft.Column(
                controls=[
                    ft.Stack(
                        controls=[
                            column_swap,
                            ft.Container(
                                border_radius=ft.border_radius.all(12),
                                bgcolor="black54",
                                left=column_swap.width / 2.3,
                                right=column_swap.width / 2.3,
                                top=column_swap.height / 2.4,
                                bottom=column_swap.height / 2.4,
                                content=ft.Icon(name="swap_vertical_circle_rounded"),
                            ),
                        ],
                    ),
                    ft.Container(
                        # height=80,
                        width=420,
                        padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
                        border_radius=ft.border_radius.all(24),
                        expand=True,
                        bgcolor=ft.Colors("grey900"),
                        content=ft.Dropdown(
                            autofocus=True,
                            hint_text="1 USDT = ???? ",
                            icon_disabled_color=True,
                            border_width=0,
                            options=[
                                ft.dropdown.Option("1 UST == 0.00064 ETH"),
                                ft.dropdown.Option("1 UST == 0.000000064 BTC"),
                                ft.dropdown.Option("1 UST == 1.5 TRX"),
                                ft.dropdown.Option("1 UST == 2.2 POL"),
                            ],
                        ),
                    ),
                    ft.Container(
                        width=420,
                        expand=True,
                        padding=ft.padding.only(left=12, top=12, right=12, bottom=12),
                        border_radius=ft.border_radius.all(24),
                        bgcolor=ft.Colors("blue900"),
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    "Connect wallet",
                                    size=14,
                                    color=ft.Colors("grey"),
                                    weight="bold",
                                ),
                                ft.Icon(name="navigate_next_rounded"),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ),
                ]
            ),
        )

        page.window.width = 450
        page.window.height = 600
        # page.scroll = ft.ScrollMode.HIDDEN
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.add(widget_data)
        page.update()

        serialized_data = serialize_widget(widget_data)
        data = f"""import flet as ft\n{serialized_data}"""

        write_to_file(data, "widget_structure.py")

    ft.app(target=main)
