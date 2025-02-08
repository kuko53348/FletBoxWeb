import flet as ft

md1 = """## Code blocks

Formatted Dart code looks really pretty too:

```
void main() {
    runApp(MaterialApp(
        home: Scaffold(
        body: ft.Markdown(data: markdownData),
    ),
    ));
}
```"""


CupertinoTextField = ft.CupertinoTextField(
    placeholder_text="Placeholder",
)


Markdown = ft.Markdown(
    selectable=True,
    extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
    value=md1,
)


Text = ft.Text(
    value="Size 15, Normal",
    size=15,
    color=ft.Colors("white"),
    bgcolor=ft.Colors.ORANGE_800,
    weight=ft.FontWeight.NORMAL,
)


TextField = ft.TextField(
    label="With an icon",
    icon=ft.Icons.EMOJI_EMOTIONS,
)
