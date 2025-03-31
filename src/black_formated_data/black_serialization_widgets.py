import flet as ft
from typing import Any, List, Dict, Set, Deque, Optional


def serialize_widget(widget, indent=0):
    """
    ### Serialize Flet widget tree into a human-readable format with all attributes.

    ```python
    >>> from .black_serialization_widgets import serialize_widget
    >>> def main(page: ft.Page):
    >>>     widget_data = ft.Container(
                expand=True,
                padding=ft.padding.only(left=12, top=12, right=12, bottom=12),
                border_radius=ft.border_radius.all(12),
                width=340,
                bgcolor=ft.Colors("grey900"),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors("black"),
                    offset=ft.Offset(0, 5),
                ),
                image=ft.DecorationImage(src="amazon.jpg", fit="cover", opacity=0.18),
                content=ft.Text(),
            )

            page.window.width = 450
            page.window.height = 600
            # page.scroll = ft.ScrollMode.HIDDEN
            page.vertical_alignment = ft.MainAxisAlignment.CENTER
            page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.add(widget_data)
            page.update()

            serialized_data = serialize_widget(widget_data)
            # scape_filters
            data = data.replace("Offset", "ft.Offset")

            write_to_file(data, "widget_structure.py")

    >>> if __name__ == "__main__":
    >>>    ft.app(target=main)```

    """
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
        "select_icon",
        "self",
        "args",
        "kwargs",
        "rtl",
        "image_src",
        "image_repeat",
        "image_opacity",
        "image_src_base64",
        "image_fit",
        "track_color",
        "inactive_track_color",
        "active_color",
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
        "uid",
        "spans",
    ]

    for attr in dir(widget):
        # try:
        if attr in filter_deprecated:
            continue

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
                            print(value)
                            # ================================
                            # new_color = f"{value.name.lower()}"
                            # new_color = new_color.replace("_", "")
                            # value_str = f"Colors('{new_color}')"
                            # ================================

                            value_str = check_instance(
                                value=value.name, instance_widget=ft.colors
                            )

                        elif isinstance(value, ft.MainAxisAlignment):
                            value_str = f"{value}"

                        elif isinstance(value, ft.BorderSide):
                            value_str = f"{value}"

                        elif isinstance(value, ft.Border):
                            value_str = f"{value}"

                        elif isinstance(value, ft.NavigationRailLabelType):
                            value_str = f"{value}"

                        elif isinstance(value, ft.CrossAxisAlignment):
                            value_str = f"{value}"

                        elif isinstance(value, ft.TileAffinity):
                            value_str = f"{value}"

                        elif isinstance(value, ft.ScrollMode):
                            value_str = f"{value}"

                        elif isinstance(value, ft.CupertinoTimerPickerMode):
                            value_str = f"{value}"

                        elif isinstance(value, ft.GradientTileMode):
                            value_str = f"{value}"

                        elif isinstance(value, ft.LabelPosition):
                            value_str = f"{value}"

                        elif isinstance(value, ft.AnimationCurve):
                            value_str = f"{value}"

                        elif isinstance(value, ft.AnimatedSwitcherTransition):
                            value_str = f"{value}"

                        elif isinstance(value, ft.Icons):
                            value_str = f"{value}"

                        elif isinstance(value, ft.MarkdownExtensionSet):
                            value_str = f"{value}"

                        elif isinstance(value, ft.ImageRepeat):
                            value_str = f"{value}"

                        elif isinstance(value, ft.FontWeight):
                            value_str = f"{value}"

                        elif isinstance(value, ft.ImageFit):
                            value_str = f"{value}"

                        elif isinstance(value, ft.TextAlign):
                            value_str = f"{value}"

                        elif isinstance(value, ft.ControlState):
                            value_str = f"{value}"

                        elif isinstance(value, ft.Offset):
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
            result += f"{spacing}    Tab(text='{tab.text}',tab_content=ft.Icon(ft.Icons.SEARCH), content=\n"
            result += serialize_widget(tab.content, indent + 3)
            result += f"{spacing}    ),\n"

        result += f"{spacing}  ],\n"

    elif isinstance(widget, ft.ListView):
        result += f"{spacing}  items=[\n"
        for item in widget.controls:
            result += f"{spacing}    ListTile(title={serialize_widget(item.title, indent + 3)}),\n"
        result += f"{spacing}  ],),\n"

    if isinstance(widget, ft.RadioGroup):
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
    # del attributes
    # del value

    # result = result.replace("ft.ft.", "ft.").replace("],),", "],")
    return result


def write_to_file(data: str = "", filename: str = ""):
    """Write serialized data to a Python file."""

    with open(filename, "w") as file:
        file.write(data)


def check_instance(value, instance_widget):
    value_str = value
    # print(value_str, "[+] <<<<<<<<<<< ", type(value_str))

    if isinstance(value, str):
        value_str = f"{value.lower()}"

    elif isinstance(value, dict):
        for _ in value.keys():
            value_str = check_instance(value=_, instance_widget=instance_widget)

            # value_str = f"{_}"
        # print(f"===== her ===={value_str}")

    else:
        new_color = f"{value.name.lower()}"
        value_str = new_color.replace("_", "")
    return value_str


def _format_value(value: Any, indent_level: int = 4) -> str:
    # """Comprehensive value formatting"""
    if isinstance(value, ft.Border):
        try:
            tmp_widget = check_instance(
                value=value.top.color,
                instance_widget=ft.Colors,
            )
            value.top.color = tmp_widget
        except:
            value = value

        return value

    if isinstance(value, ft.DecorationImage):
        tmp_widget = check_instance(value=value.fit, instance_widget=ft.ImageFit)
        value.fit = tmp_widget

        return value

    if isinstance(value, ft.LinearGradient):
        # if value.tile_mode:
        value.tile_mode = check_instance(
            value=value.tile_mode, instance_widget=ft.GradientTileMode
        )
        value.colors = [_.split(" ")[0] for _ in value.colors]

        return value

    if isinstance(value, ft.BoxShadow):
        color = check_instance(value=value.color, instance_widget=ft.Colors)
        ShadowBlurStyle = check_instance(
            value=value.blur_style, instance_widget=ft.ShadowBlurStyle
        )
        value.color = color
        value.blur_style = ShadowBlurStyle

        return value

    if isinstance(value, ft.ChartGridLines):
        tmp_widget = check_instance(value=value.color, instance_widget=ft.Colors)
        value.color = tmp_widget

    if isinstance(value, ft.ButtonStyle):
        tmp_widget = check_instance(value=value.bgcolor, instance_widget=ft.Colors)
        tmp_widget = check_instance(value=value.bgcolor, instance_widget=ft.padding)
        tmp_widget = check_instance(
            value=value.text_style,
            instance_widget=ft.TextStyle,
        )
        tmp_widget = check_instance(value=value.shape, instance_widget=ft.ControlState)
        tmp_widget = check_instance(value=value.side, instance_widget=ft.ControlState)
        value.bgcolor = tmp_widget
        value.padding = tmp_widget
        value.text_style = tmp_widget
        value.shape = tmp_widget
        value.side = tmp_widget

        return value

    return value


if __name__ == "__main__":

    def main(page: ft.Page):
        # Serialize the widget structure and write it to a file
        # src="./flet_box/assets/splash.png",
        # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        # vertical_alignment=ft.CrossAxisAlignment.CENTER,
        # horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        widget_data = ft.Container(
            expand=True,
            padding=ft.padding.only(left=12, top=12, right=12, bottom=12),
            border_radius=ft.border_radius.all(12),
            width=340,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                # offset=ft.Offset(0, 5),
            ),
            image=ft.DecorationImage(src="amazon.jpg", fit="cover", opacity=0.18),
            content=ft.Text(),
        )

        page.window.width = 450
        page.window.height = 600
        # page.scroll = ft.ScrollMode.HIDDEN
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.add(widget_data)
        page.update()

        serialized_data = serialize_widget(widget_data)
        rafactory_code = f"""import flet as ft\n{serialized_data}"""
        # scape_filters
        rafactory_code = rafactory_code.replace("ft.ft.", "ft.").replace("],),", "],")
        # rafactory_code = rafactory_code.replace("white12", "transparent")

        write_to_file(rafactory_code, "widget_structure.py")

    ft.app(target=main)
