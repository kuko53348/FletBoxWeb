import flet as ft


class save_menu_container(ft.Container):

    def __init__(self, page: object = None):
        super().__init__()
        self.page = page
        # self.expand = True
        self.ink = False
        self.bgcolor = ft.colors('black12')
        self.padding = ft.padding.all(8)
        self.margin = ft.margin.all(8)
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(30)
        self.border = ft.border.all(0.5, ft.colors('white12'))
        self.width = 480
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors('black45'),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )
    def build(self,):
        self.content= ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            expand=True,
                            padding=ft.padding.only(left=62),
                            alignment=ft.alignment.center,
                            content=ft.Text(
                                size=26,
                                text_align=ft.TextAlign.CENTER,
                                weight=ft.FontWeight.W_900,
                                font_family="Consolas",
                                value="Save Projects",
                            )
                        ),
                        ft.Container(
                            tooltip='Back Home Page',
                            padding=ft.padding.all(8),
                            margin=ft.margin.all(8),
                            border_radius=ft.border_radius.all(24),
                            bgcolor=ft.Colors.with_opacity(0.5,ft.colors('red')),
                            alignment=ft.alignment.center,
                            content=ft.Icon(
                                name=ft.icons('swipe_left'),
                            ),
                            on_click=lambda _: self.go_home_page(same_page=True)
                        ),
                    ]
                ),
                ft.Container(
                    # padding=ft.padding.all(8),
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",
                        color=ft.colors('blue200'),
                        value="If you want only save current project to continue working in future press current save button",
                    )
                ),
                ft.Container(
                    padding=ft.padding.all(8),
                    margin=ft.margin.all(16),
                    border_radius=ft.border_radius.all(18),
                    alignment=ft.alignment.center,
                    # expand=True,
                    ink=True,
                    height=48,
                    bgcolor=ft.Colors.with_opacity(0.04, ft.colors('blue200')),
                    content=ft.Text(
                        size=18,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.W_900,
                        font_family="Consolas",
                        color=ft.colors('blue200'),
                        value="Save",
                    ),
                    on_click=lambda _: self.save_project(),
                ),
                ft.Container(
                    padding=ft.padding.all(8),
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        size=26,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.W_900,
                        font_family="Consolas",
                        value="Create New Module",
                    )
                ),
                ft.Container(
                    padding=ft.padding.all(8),
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",
                        color=ft.colors('blue200'),
                        value="If you want create a module inside flet-box marketplace press create module buttom",
                    )
                ),
                ft.Container(
                    padding=ft.padding.all(16),
                    alignment=ft.alignment.center,
                    content= ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Container(
                                alignment=ft.alignment.center,
                                content=ft.Dropdown(
                                    border_radius=ft.border_radius.all(16),
                                    border_width=0,
                                    width=160,
                                    label='Project name',
                                    options=[
                                        ft.dropdown.Option(
                                            key=_,
                                            on_click=lambda tmp_widget: self.column_name(widget_name=tmp_widget.control)
                                        ) for _ in self.project_tab
                                    ],
                                ),
                            ),
                        ),
                        ft.Container(
                            expand=True,
                            ink=False,
                            padding=ft.padding.all(8),
                            margin=ft.margin.all(8),
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(30),
                            content=ft.TextField(
                                label="Set module name",
                                color=ft.Colors.with_opacity(0.8,ft.colors('yellow')),
                                border_color=ft.colors('black12'),
                                border_width=2,
                                bgcolor=ft.Colors.with_opacity(0.2, ft.colors( 'black')),
                                border=ft.InputBorder.OUTLINE,
                                border_radius=16,
                                #: EVENTS
                                on_change= lambda tmp_widget: self.project_name(widget_name= tmp_widget.control),
                            ),
                            #: EVENTS
                            # on_click= lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                        ),
                    ]
                ),
                ),

                self.button_save_project,
            ]
        )


    def go_home_page(self):
        self.page.views[1].controls[0].visible=True
        self.page.views[1].controls[1].visible=False
        self.page.views[1].controls[2].visible=False
        self.page.views[1].update()