import flet as ft


class DataTable(ft.DataTable):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__(columns=[], rows=[])
        self.page = page

    def build(self):
        self.columns = [
            ft.DataColumn(ft.Text("First name")),
            ft.DataColumn(ft.Text("Last name")),
            ft.DataColumn(ft.Text("Age"), numeric=True),
        ]
        self.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("Smith")),
                    ft.DataCell(ft.Text("43")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Jack")),
                    ft.DataCell(ft.Text("Brown")),
                    ft.DataCell(ft.Text("19")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Alice")),
                    ft.DataCell(ft.Text("Wong")),
                    ft.DataCell(ft.Text("25")),
                ],
            ),
        ]


class DataRow(ft.DataRow):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page


class DataCell(ft.DataCell):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page


class DataColumn(ft.DataColumn):
    def __init__(
        self,
        page: object = ft.Page,
        event_manager: object = None,
    ):
        super().__init__()
        self.page = page
