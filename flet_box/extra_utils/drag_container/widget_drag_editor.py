import flet as ft

from .dragg_widget import DraggWidget
from .categories import widgets_by_categories


class categories(ft.Container):
    drag_container_color = ft.colors("black12")
    drag_container_border_color = ft.colors("background")
    drag_container_shadow_color = ft.colors("black54")
    drag_text_container_color = ft.colors("black26")
    drag_text_color = ft.colors("white")

    def __init__(
        self,
        page: object = None,
        title: str = str,
        controls_view: list = list(),
    ):
        super().__init__()
        self.drag_box = self
        self.page = page
        self.title = title

        self.ink = False
        self.controls_view = controls_view
        self.expand = True

    def build(self):
        self.content = ft.Column(
            controls=[
                ft.Container(
                    ink=False,
                    padding=ft.padding.all(2),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(12),
                    content=ft.Text(
                        value=self.title,
                        text_align=ft.TextAlign.LEFT,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",  # "Consolas ,RobotoSlab
                        color=self.drag_text_color,
                    ),
                ),
                ft.Container(  # : TEXT WIDGET
                    ink=False,
                    bgcolor=self.drag_text_container_color,
                    padding=ft.padding.all(2),
                    margin=ft.margin.all(2),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(12),
                    border=ft.border.all(0.2, self.drag_container_border_color),
                    content=ft.GridView(
                        runs_count=3,
                        run_spacing=8,
                        padding=4,
                        spacing=8,
                        expand=1,
                        controls=self.controls_view,
                    ),
                ),
            ]
        )
        self.controls = self.controls_view


class Build_Drag_Editor(ft.Container):

    drag_container_color = ft.colors("black12")
    drag_container_border_color = ft.colors("background")
    drag_container_shadow_color = ft.colors("black54")
    drag_text_container_color = ft.colors("black26")
    drag_text_color = ft.colors("cyan")

    color_minimum: float = 0.02
    color_medium: float = 0.04
    color_hight: float = 0.06

    def __init__(
        self,
        page: object = None,
    ):
        super().__init__()
        self.drag_box = self
        self.page = page
        self.ink = False
        # self.bgcolor       = self.drag_container_color
        self.padding = ft.padding.all(0)
        self.margin = ft.margin.all(3)
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(16)
        self.width = 268

        self.bgcolor = ft.Colors.with_opacity(0.5, ft.colors("black"))
        self.border = ft.border.all(2, ft.Colors.with_opacity(0.6, ft.colors("black")))
        self.blur = (18, 18)
        self.border = ft.border.all(0.2, self.drag_container_border_color)

    def build(self):
        #: CONTROLS
        #: VIEW_COLUMN_ROUNDED
        #: TABLE_ROWS_ROUNDED
        #: WIDGETS_ROUNDED
        #: WEB_STORIES_ROUNDED
        #: icons.FORMAT_SIZE_ROUNDED <=== texto
        #: icons.FORMAT_COLOR_FILL_ROUNDED <== color

        #: CONTAINERS LAYOUTS

        # CATEGORIES
        # categories =  {'buttons', 'text', , 'images', 'selection', 'progress', 'charts', 'layout'
        # 'tables', 'tooltips', 'divider', 'other'}
        categorie_custom_text_widgets = widgets_by_categories.get("custom text widgets")
        categorie_custom_widgets = widgets_by_categories.get("custom widgets")
        categorie_navigations = widgets_by_categories.get("navigations")
        categorie_layout = widgets_by_categories.get("layout")
        categorie_buttons = widgets_by_categories.get("buttons")
        categorie_alerts = widgets_by_categories.get("alerts")
        categorie_cupertino_buttons = widgets_by_categories.get("cupertino buttons")
        categorie_text = widgets_by_categories.get("text")
        categorie_images = widgets_by_categories.get("images")
        categorie_selection = widgets_by_categories.get("selection")
        categorie_cupertino_selection = widgets_by_categories.get("cupertino selection")
        categorie_progress = widgets_by_categories.get("progress")
        categorie_charts = widgets_by_categories.get("charts")
        categorie_tables = widgets_by_categories.get("tables")
        categorie_tooltips = widgets_by_categories.get("tooltips")
        # categorie_other = widgets_by_categories.get("other")

        #: CHARTS LAYOUTS

        self.content = ft.Column(
            scroll="HIDDEN",
            controls=[
                categories(
                    page=self.page,
                    title="custom text widgets",
                    controls_view=[
                        DraggWidget(
                            page=self.page,
                            drag_box=self.drag_box,
                            widget=_,
                            color="CYAN",
                            icons=ft.icons(categorie_custom_text_widgets.get(_)),
                        )
                        for _ in categorie_custom_text_widgets
                    ],
                ),
                categories(
                    page=self.page,
                    title="custom widgets",
                    controls_view=[
                        DraggWidget(
                            page=self.page,
                            drag_box=self.drag_box,
                            widget=_,
                            color="CYAN",
                            icons=ft.icons(categorie_custom_widgets.get(_)),
                        )
                        for _ in categorie_custom_widgets
                    ],
                ),
                categories(
                    page=self.page,
                    title="Navigation",
                    controls_view=[
                        DraggWidget(
                            page=self.page,
                            drag_box=self.drag_box,
                            widget=_,
                            color="CYAN",
                            icons=ft.icons(categorie_navigations.get(_)),
                        )
                        for _ in categorie_navigations
                    ],
                ),
                categories(
                    page=self.page,
                    title="layout",
                    controls_view=[
                        DraggWidget(
                            page=self.page,
                            drag_box=self.drag_box,
                            widget=_,
                            color="CYAN",
                            icons=ft.icons(categorie_layout.get(_)),
                        )
                        for _ in categorie_layout
                    ],
                ),
                categories(
                    page=self.page,
                    title="buttons",
                    controls_view=[
                        DraggWidget(
                            page=self.page,
                            drag_box=self.drag_box,
                            widget=_,
                            color="CYAN",
                            icons=ft.icons(categorie_buttons.get(_)),
                        )
                        for _ in categorie_buttons
                    ],
                ),
                categories(
                    page=self.page,
                    title="Alerts",
                    controls_view=[
                        DraggWidget(
                            page=self.page,
                            drag_box=self.drag_box,
                            widget=_,
                            color="CYAN",
                            icons=ft.icons(categorie_alerts.get(_)),
                        )
                        for _ in categorie_alerts
                    ],
                ),
                categories(
                    page=self.page,
                    title="cupertino buttons",
                    controls_view=[
                        DraggWidget(
                            page=self.page,
                            drag_box=self.drag_box,
                            widget=_,
                            color="CYAN",
                            icons=ft.icons(categorie_cupertino_buttons.get(_)),
                        )
                        for _ in categorie_cupertino_buttons
                    ],
                ),
                categories(
                    page=self.page,
                    title="text",
                    controls_view=[
                        DraggWidget(
                            page=self.page,
                            drag_box=self.drag_box,
                            widget=_,
                            color="CYAN",
                            icons=ft.icons(categorie_text.get(_)),
                        )
                        for _ in categorie_text
                    ],
                ),
                categories(
                    page=self.page,
                    title="images",
                    controls_view=[
                        DraggWidget(
                            page=self.page,
                            drag_box=self.drag_box,
                            widget=_,
                            color="CYAN",
                            icons=ft.icons(categorie_images.get(_)),
                        )
                        for _ in categorie_images
                    ],
                ),
                categories(
                    page=self.page,
                    title="selection",
                    controls_view=[
                        DraggWidget(
                            page=self.page,
                            drag_box=self.drag_box,
                            widget=_,
                            color="CYAN",
                            icons=ft.icons(categorie_selection.get(_)),
                        )
                        for _ in categorie_selection
                    ],
                ),
                categories(
                    page=self.page,
                    title="cupertino selection",
                    controls_view=[
                        DraggWidget(
                            page=self.page,
                            drag_box=self.drag_box,
                            widget=_,
                            color="CYAN",
                            icons=ft.icons(categorie_cupertino_selection.get(_)),
                        )
                        for _ in categorie_cupertino_selection
                    ],
                ),
                categories(
                    page=self.page,
                    title="progress",
                    controls_view=[
                        DraggWidget(
                            page=self.page,
                            drag_box=self.drag_box,
                            widget=_,
                            color="CYAN",
                            icons=ft.icons(categorie_progress.get(_)),
                        )
                        for _ in categorie_progress
                    ],
                ),
                categories(
                    page=self.page,
                    title="charts",
                    controls_view=[
                        DraggWidget(
                            page=self.page,
                            drag_box=self.drag_box,
                            widget=_,
                            color="CYAN",
                            icons=ft.icons(categorie_charts.get(_)),
                        )
                        for _ in categorie_charts
                    ],
                ),
                categories(
                    page=self.page,
                    title="tables",
                    controls_view=[
                        DraggWidget(
                            page=self.page,
                            drag_box=self.drag_box,
                            widget=_,
                            color="CYAN",
                            icons=ft.icons(categorie_tables.get(_)),
                        )
                        for _ in categorie_tables
                    ],
                ),
                # categories(
                #     page=self.page,
                #     title="other",
                #     controls_view=[
                #         DraggWidget(
                #             page=self.page,
                #             drag_box=self.drag_box,
                #             widget=_,
                #             color="CYAN",
                #             icons=ft.icons(categorie_other.get(_)),
                #         )
                #         for _ in categorie_other
                #     ],
                # ),
            ],
        )
