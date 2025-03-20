import flet as ft
import time


class alert_dialog(ft.Container):

    def __init__(self, page: object = None, content: object = None) -> None:
        super().__init__()
        self.page = page
        self.alignment = ft.alignment.center
        self.ink = True
        self.visible = False
        self.ink_color = ft.colors("yellow")
        self.border_radius = ft.border_radius.only(
            top_left=32, top_right=32, bottom_left=32, bottom_right=32
        )
        self.width = 200

        self.bgcolor = ft.colors("red")
        self.content = ft.Text(value="Sussefully copied", weight="bold", size=13)


class code_editor(ft.Container):
    opacity_markdown: float = 0.9

    def __init__(
        self,
        widget: object = None,
        md_code: str = str(),
        visible: bool = False,
        page: object = None,
    ):
        super().__init__()
        self.page = page
        self.widget = widget
        self.visible = visible
        self.margin = ft.margin.all(0)
        self.bgcolor = ft.Colors.with_opacity(0.05, ft.colors("brown"))
        self.blur = (12, 12)
        self.md_code = md_code
        self.theme_name = "solarized-dark"
        self.bgcolor = ft.Colors.with_opacity(0.05, ft.colors("white"))

        self.Markdown = ft.Markdown(
            value=self.md_code,
            scale=0.998,
            opacity=self.opacity_markdown,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,  # COMMON_MARK ,GITHUB_FLAVORED ,GITHUB_WEB
            code_theme=ft.MarkdownCodeTheme.GRUVBOX_DARK,
            code_style_sheet=ft.MarkdownStyleSheet(
                code_text_style=ft.TextStyle(font_family="Roboto Mono"),
            ),
            md_style_sheet=ft.MarkdownStyleSheet(
                code_text_style=ft.TextStyle(font_family="Roboto Mono"),
            ),
        )
        self.alert_visibility = alert_dialog(page=self.page)

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.VerticalAlignment.CENTER,
            spacing=0,
            run_spacing=0,
            controls=[
                #
                ft.Container(
                    opacity=self.opacity_markdown,
                    padding=ft.padding.only(left=16, right=12, top=12, bottom=0),
                    height=35,
                    bgcolor="#282828",
                    content=self.alert_visibility,
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    padding=ft.padding.only(left=16, right=0, top=0, bottom=0),
                    expand=True,
                    opacity=self.opacity_markdown,
                    bgcolor="#282828",
                    content=ft.Column(
                        scroll="ALWAYS",
                        controls=[
                            self.Markdown,
                        ],
                    ),
                ),
                # MARK DOWN EDITOR
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                tooltip="Home",
                                padding=ft.padding.all(0),
                                margin=ft.margin.all(0),
                                content=ft.Row(
                                    controls=[
                                        ft.IconButton(
                                            bgcolor=ft.Colors.with_opacity(
                                                opacity=0.2, color="cyan"
                                            ),
                                            icon="home",
                                            on_click=lambda widget: self.hide_overlay(),
                                        ),
                                    ]
                                ),
                            ),
                            ft.Container(
                                tooltip="Copy",
                                padding=ft.padding.all(8),
                                content=ft.Row(
                                    controls=[
                                        ft.IconButton(
                                            bgcolor=ft.Colors.with_opacity(
                                                opacity=0.2, color="yellow"
                                            ),
                                            icon="copy",
                                            on_click=lambda widget: self.copy_widget_template(
                                                markdown_text=self.Markdown.value
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                        ],
                    ),
                ),
            ],
        )

    def copy_widget_template(self, markdown_text) -> None:
        markdown_text = markdown_text.strip("```python").strip("```")
        self.page.set_clipboard(value=markdown_text)

        self.alert_visibility.visible = False if self.alert_visibility.visible else True
        self.alert_visibility.update()
        time.sleep(0.5)

        self.alert_visibility.visible = False if self.alert_visibility.visible else True
        self.alert_visibility.update()

    def hide_overlay(self):
        self.page.update()

        self.page.overlay.remove(self.widget)
        self.page.update()
