import flet as ft


class Card(ft.Card):
    def __init__(
        self,
        page: object = ft.Page,
    ):
        super().__init__()
        self.page = page


class Column(ft.Column):
    def __init__(
        self,
        page: object = ft.Page,
    ):
        super().__init__()
        self.page = page


class Container(ft.Container):
    def __init__(
        self,
        page: object = ft.Page,
    ):
        super().__init__()
        self.page = page


class GridView(ft.GridView):
    def __init__(
        self,
        page: object = ft.Page,
    ):
        super().__init__()
        self.page = page
        self.runs_count = 2
        self.run_spacing = 4
        padding = ft.padding.all(6)


class ListView(ft.ListView):
    def __init__(
        self,
        page: object = ft.Page,
    ):
        super().__init__()
        self.page = page


class ResponsiveRow(ft.ResponsiveRow):
    def __init__(
        self,
        page: object = ft.Page,
    ):
        super().__init__()
        self.page = page


class Row(ft.Row):
    def __init__(
        self,
        page: object = ft.Page,
    ):
        super().__init__()
        self.page = page


class Stack(ft.Stack):
    def __init__(
        self,
        page: object = ft.Page,
    ):
        super().__init__()
        self.page = page
