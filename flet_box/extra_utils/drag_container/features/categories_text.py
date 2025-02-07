import flet as ft

md1 = """

## Code blocks

Formatted Dart code looks really pretty too:

```
void main() {
    runApp(MaterialApp(
        home: Scaffold(
        body: ft.Markdown(data: markdownData),
    ),
    ));
}
```
"""


class CupertinoTextField(ft.CupertinoTextField):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.placeholder_text = "Placeholder"


class Markdown(ft.Markdown):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.placeholder_text = "Placeholder"

        self.selectable = True
        self.extension_set = ft.MarkdownExtensionSet.GITHUB_WEB
        # self.on_tap_link=lambda e: page.launch_url(e.data)

    def build(self):
        self.value = md1


class Text(ft.Text):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page

        self.value = "Size 15, Normal"
        self.size = 15
        self.color = ft.Colors.WHITE
        self.bgcolor = ft.Colors.ORANGE_800
        self.weight = ft.FontWeight.NORMAL


class TextField(ft.TextField):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page

        self.label = "With an icon"
        self.icon = ft.Icons.EMOJI_EMOTIONS
