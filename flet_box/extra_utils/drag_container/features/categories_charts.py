import flet as ft


class BarChart(ft.BarChart):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.tooltip_bgcolor = ft.Colors.with_opacity(0.5, ft.Colors("grey")_300)
        self.max_y = 110
        self.interactive = True
        self.border = ft.border.all(1, ft.Colors("grey")_400)
        self.expand = True
        self.horizontal_grid_lines = ft.ChartGridLines(
            color=ft.Colors("grey")_300, width=1, dash_pattern=[3, 3]
        )

    def build(self):
        self.bar_groups = [
            ft.BarChartGroup(
                x=0,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=40,
                        width=40,
                        color=ft.Colors.AMBER,
                        tooltip="Apple",
                        border_radius=0,
                    ),
                ],
            ),
            ft.BarChartGroup(
                x=1,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=100,
                        width=40,
                        color=ft.Colors("blue"),
                        tooltip="Blueberry",
                        border_radius=0,
                    ),
                ],
            ),
            ft.BarChartGroup(
                x=2,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=30,
                        width=40,
                        color=ft.Colors.RED,
                        tooltip="Cherry",
                        border_radius=0,
                    ),
                ],
            ),
            ft.BarChartGroup(
                x=3,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=60,
                        width=40,
                        color=ft.Colors.ORANGE,
                        tooltip="Orange",
                        border_radius=0,
                    ),
                ],
            ),
        ]
        self.left_axis = ft.ChartAxis(
            labels_size=40, title=ft.Text("Fruit supply"), title_size=40
        )
        self.bottom_axis = ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=0, label=ft.Container(ft.Text("Apple"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=1, label=ft.Container(ft.Text("Blueberry"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=2, label=ft.Container(ft.Text("Cherry"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=3, label=ft.Container(ft.Text("Orange"), padding=10)
                ),
            ],
            labels_size=40,
        )


class LineChart(ft.LineChart):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.tooltip_bgcolor = ft.Colors.with_opacity(0.8, ft.Colors("blue")_GREY)
        self.min_y = 0
        self.max_y = 4
        self.min_x = 0
        self.max_x = 14
        self.expand = True

        self.border = ft.Border(
            bottom=ft.BorderSide(4, ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE))
        )

    def build(self):
        self.data_1 = [
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 1),
                    ft.LineChartDataPoint(3, 1.5),
                    ft.LineChartDataPoint(5, 1.4),
                    ft.LineChartDataPoint(7, 3.4),
                    ft.LineChartDataPoint(10, 2),
                    ft.LineChartDataPoint(12, 2.2),
                    ft.LineChartDataPoint(13, 1.8),
                ],
                stroke_width=8,
                color=ft.Colors.LIGHT_GREEN,
                curved=True,
                stroke_cap_round=True,
            ),
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 1),
                    ft.LineChartDataPoint(3, 2.8),
                    ft.LineChartDataPoint(7, 1.2),
                    ft.LineChartDataPoint(10, 2.8),
                    ft.LineChartDataPoint(12, 2.6),
                    ft.LineChartDataPoint(13, 3.9),
                ],
                color=ft.Colors.PINK,
                below_line_bgcolor=ft.Colors.with_opacity(0, ft.Colors.PINK),
                stroke_width=8,
                curved=True,
                stroke_cap_round=True,
            ),
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(1, 2.8),
                    ft.LineChartDataPoint(3, 1.9),
                    ft.LineChartDataPoint(6, 3),
                    ft.LineChartDataPoint(10, 1.3),
                    ft.LineChartDataPoint(13, 2.5),
                ],
                color=ft.Colors.CYAN,
                stroke_width=8,
                curved=True,
                stroke_cap_round=True,
            ),
        ]

        self.left_axis = ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=1,
                    label=ft.Text("1m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Text("2m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=3,
                    label=ft.Text("3m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=4,
                    label=ft.Text("4m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=5,
                    label=ft.Text("5m", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=6,
                    label=ft.Text("6m", size=14, weight=ft.FontWeight.BOLD),
                ),
            ],
            labels_size=40,
        )
        self.data_series = self.data_1

        self.bottom_axis = ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Container(
                        ft.Text(
                            "SEP",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=7,
                    label=ft.Container(
                        ft.Text(
                            "OCT",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=12,
                    label=ft.Container(
                        ft.Text(
                            "DEC",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
            ],
            labels_size=32,
        )


class LineChartData(ft.LineChartData):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page


class LineChartDataPoint(ft.LineChartDataPoint):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page


class PieChart(ft.PieChart):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
        self.sections_space = 1
        self.center_space_radius = 0
        self.expand = True
        self.normal_border = ft.BorderSide(
            0, ft.Colors.with_opacity(0, ft.Colors("white"))
        )
        # self.hovered_border = ft.BorderSide(6, ft.Colors("white"))
        # self.on_chart_event = lambda _: print(_)

    def build(self):

        self.sections = [
            ft.PieChartSection(
                25,
                color=ft.Colors("blue"),
                radius=80,
                border_side=self.normal_border,
            ),
            ft.PieChartSection(
                25,
                color=ft.Colors.YELLOW,
                radius=65,
                border_side=self.normal_border,
            ),
            ft.PieChartSection(
                25,
                color=ft.Colors.PINK,
                radius=60,
                border_side=self.normal_border,
            ),
            ft.PieChartSection(
                25,
                color=ft.Colors.GREEN,
                radius=70,
                border_side=self.normal_border,
            ),
        ]


class PieChartSection(ft.PieChartSection):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
