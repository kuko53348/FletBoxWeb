import flet as ft


BarChart = ft.BarChart(
    tooltip_bgcolor=ft.Colors.with_opacity(0.5, ft.Colors("grey300")),
    max_y=110,
    interactive=True,
    border=ft.border.all(1, ft.Colors("grey400")),
    expand=True,
    horizontal_grid_lines=ft.ChartGridLines(
        color=ft.Colors("grey300"), width=1, dash_pattern=[3, 3]
    ),
    bar_groups=[
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
                    color=ft.Colors("red"),
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
                    color=ft.Colors("orange"),
                    tooltip="Orange",
                    border_radius=0,
                ),
            ],
        ),
    ],
    left_axis=ft.ChartAxis(
        labels_size=40, title=ft.Text("Fruit supply"), title_size=40
    ),
    bottom_axis=ft.ChartAxis(
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
    ),
)
# LineChartData
data_1 = [
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
LineChart = ft.LineChart(
    tooltip_bgcolor=ft.Colors.with_opacity(0.8, ft.Colors("bluegrey")),
    min_y=0,
    max_y=4,
    min_x=0,
    max_x=14,
    expand=True,
    border=ft.Border(
        bottom=ft.BorderSide(4, ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE))
    ),
    left_axis=ft.ChartAxis(
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
    ),
    data_series=data_1,
    bottom_axis=ft.ChartAxis(
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
    ),
)

LineChartData = ft.LineChartData()


LineChartDataPoint = ft.LineChartDataPoint()


PieChart = ft.PieChart(
    sections_space=1,
    center_space_radius=0,
    expand=True,
    # hovered_border = ft.BorderSide(6, ft.Colors("white"))
    # on_chart_event = lambda _: print(_)
    sections=[
        ft.PieChartSection(
            25,
            color=ft.Colors("blue"),
            radius=80,
            border_side=ft.BorderSide(0, ft.Colors.with_opacity(0, ft.Colors("white"))),
        ),
        ft.PieChartSection(
            25,
            color=ft.Colors.YELLOW,
            radius=65,
            border_side=ft.BorderSide(0, ft.Colors.with_opacity(0, ft.Colors("white"))),
        ),
        ft.PieChartSection(
            25,
            color=ft.Colors.PINK,
            radius=60,
            border_side=ft.BorderSide(0, ft.Colors.with_opacity(0, ft.Colors("white"))),
        ),
        ft.PieChartSection(
            25,
            color=ft.Colors.GREEN,
            radius=70,
            border_side=ft.BorderSide(0, ft.Colors.with_opacity(0, ft.Colors("white"))),
        ),
    ],
)

PieChartSection = ft.PieChartSection()
