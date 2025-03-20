import flet as ft

from dragg_widgets.parse_data import main_stream, stream_widget, parse_data
from markdown_code_editor.markdown_code_editor import code_editor
from black_formated_data.black_rope_refactory import CodeFormatter
from black_formated_data.black_serialization_widgets import (
    serialize_widget,
    write_to_file,
)


class left_menu_app_container(ft.Container):

    def __init__(self, page: object = None, content: object = None) -> None:
        super().__init__()
        self.page = page
        self.width = 60
        self.visible = True
        self.ink = True
        self.bgcolor = ft.colors("white12")
        self.alignment = ft.alignment.center
        self.ink_color = ft.colors("yellow")

        self.tooltip = "dragg_container_app"
        self.padding = ft.padding.only(left=0, right=0, bottom=0, top=16)
        self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        self.border_radius = ft.border_radius.only(
            top_left=32, top_right=32, bottom_left=32, bottom_right=32
        )
        self.border = ft.border.all(width=2, color=ft.colors("grey900"))
        self.gradient = ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[
                ft.colors("transparent"),
                ft.colors("black12"),
            ],
        )
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors("black"),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            run_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            spacing=8,
            run_spacing=8,
            controls=[
                ft.Container(
                    border_radius=ft.border_radius.only(
                        top_left=32, top_right=32, bottom_left=32, bottom_right=32
                    ),
                    border=ft.border.all(width=2, color=ft.colors("grey900")),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.colors("black"),
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    height=48,
                    width=48,
                    ink=True,
                    ink_color=ft.colors("yellow"),
                    bgcolor=ft.colors("red"),
                    alignment=ft.alignment.center,
                    content=ft.Icon(name="save"),
                    on_click=lambda _: self.save_data(),
                ),
            ],
        )

    def save_data(self):
        # get all widgets
        data_to_save = self.page.session.get("save_data")
        serialized_data = serialize_widget(data_to_save)

        # creating import str
        full_code_stream: str = "# widget class"
        # creating all_instances str
        stream_instances: str = "list = ["

        # all controls in list
        widgets_list = data_to_save.content.controls
        for index, _ in enumerate(widgets_list):
            serialized_data = serialize_widget(_)
            code_returned = serialized_data.replace("],),", "],")
            code_returned = code_returned.replace("NoneType", "Container").replace(
                "white12", "transparent"
            )

            modificated_code = (
                stream_widget.replace(
                    "remplace_data",
                    code_returned,
                )
                .replace(
                    "stream",
                    f"{index}",
                )
                .replace("),\n),", "),)")
            )

            modificated_instance = f"fletbox_ui_{index}(page=self.page,expand=False,),"
            # add all calss code in list
            full_code_stream += modificated_code
            # add instances of class list
            stream_instances += modificated_instance

        stream_instances += "]"

        formatter = CodeFormatter(code=full_code_stream, indent_level=0)
        all_class_objects = formatter.fix_code()

        data_returned = self.crate_all_string(
            class_main=main_stream,
            class_names=all_class_objects,
            all_instances=stream_instances,
        )

        self.write_to_file(data=data_returned, filename="./src/ui_refactoy_code.py")

        self.show_current_code(mark_down_code=data_returned)

    def write_to_file(self, data: str = "", filename: str = ""):
        """Write serialized data to a Python file."""

        with open(filename, "w") as file:
            file.write(data)

    def crate_all_string(
        self,
        class_main: str = "",
        class_names: str = "",
        all_instances: str = "",
    ):

        full_code: str = (
            "import flet as ft\nfrom flet import Offset, Tab, Alignment\n\n"
        )
        full_code += class_names
        full_code += class_main

        return full_code.replace("remplace_data", all_instances)

    def show_current_code(self, mark_down_code: str = "") -> None:
        md_code = f"```python\n{mark_down_code}\n```"

        wraper_widget_container = ft.Container(
            right=0,
            bottom=0,
            left=0,
            top=0,
        )

        self.page.overlay.append(wraper_widget_container)
        Markdown = code_editor(
            page=self.page,
            md_code=md_code,
            visible=True,
            widget=wraper_widget_container,
        )

        wraper_widget_container.content = ft.Container(
            margin=ft.margin.all(28),
            blur=ft.Blur(sigma_x=20, sigma_y=20),
            border_radius=ft.border_radius.only(
                top_left=32, top_right=32, bottom_left=32, bottom_right=32
            ),
            content=Markdown,
        )

        self.page.update()
