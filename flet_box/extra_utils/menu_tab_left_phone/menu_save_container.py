import flet as ft

from .refactory_flet_box import refactory_flet_box

class menu_save_container(ft.Container):
    """
    This class describes a container save.
    """
    project_tab = [
        'Splash',
        'Introduction',
        'Login',
        'Register',
        'Lock',
        'MixViews',
        'GridView',
        'ListView',
        'DashBoard',
        'Payment',
        'Shopping',
        'Music',
        'SettingsView',
        'Verification',
        'About'
    ]

    def __init__(self, page: object = None, visible: bool=True):
        super().__init__()
        self.page = page
        self.visible = visible
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

    def build(self):
        self.save_column = ft.Column(
            controls=[
                ft.Container(
                    padding=ft.padding.all(8),
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
                    bgcolor=ft.Colors.with_opacity(0.2, ft.colors('teal')),
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
                                            key=_
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
                                color=ft.colors('black12'),
                                border_color=ft.colors('black12'),
                                border_width=2,
                                bgcolor=ft.Colors.with_opacity(0.2, ft.colors( 'black')),
                                border=ft.InputBorder.OUTLINE,
                                border_radius=16,
                                #: EVENTS
                                # on_change= lambda x:print('Pressed [< Write inside > ]'),
                                # on_submit= lambda x:print('Pressed [< Enter > ]'),
                                # on_focus = lambda x:print('Pressed [< Click inside > ]'),
                                # on_blur  = lambda x:print('Pressed [< click click and outside > ]'),
                            ),
                            #: EVENTS
                            # on_click= lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                        ),
                    ]
                ),
                ),

                ft.Container(
                    padding=ft.padding.all(8),
                    margin=ft.margin.all(16),
                    border_radius=ft.border_radius.all(18),
                    alignment=ft.alignment.center,
                    # expand=True,
                    height=48,
                    bgcolor=ft.Colors.with_opacity(0.2, ft.colors('teal')),
                    content=ft.Text(
                        size=18,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.W_900,
                        font_family="Consolas",
                        color=ft.colors('blue200'),
                        value="Create module",
                    )
                ),
            ]
        )
        self.congratulation_container = ft.Container(
            visible=False,
            content=ft.Column(
                controls=[
                    ft.Container(
                        padding=ft.padding.all(16),
                        alignment=ft.alignment.center,
                        content=ft.Text(
                            size=30,
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.W_900,
                            font_family="Consolas",
                            value="Congratulation !!.",
                        )
                    ),
                    ft.Container(
                        padding=ft.padding.all(16),
                        alignment=ft.alignment.center,
                        content=ft.Text(
                            size=18,
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.BOLD,
                            # font_family="Consolas",
                            color=ft.colors('yellow'),
                            value="🌟 A Heartfelt Thank You to the Flet Development Team! 🌟"
                            
                        )
                    ),
                    ft.Container(
                        padding=ft.padding.all(16),
                        alignment=ft.alignment.center,
                        content=ft.Text(
                            size=18,
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.BOLD,
                            # font_family="Consolas",
                            color=ft.colors('cyan'),
                            value="Dear @feodorf, @the_ethical_boy, and the entire Flet development team, Thank you for your hard work, passion, and vision. We are excited to see how Flet will evolve and inspire even more innovation in the future. Keep shining bright!",
                        )
                    ),
                    ft.Container(
                        padding=ft.padding.all(16),
                        alignment=ft.alignment.center,
                        content=ft.Text(
                            size=30,
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.W_900,
                            font_family="Consolas",
                            value="Project succesfully saved !!.",
                        )
                    ),
                ft.Container(
                    padding=ft.padding.all(8),
                    margin=ft.margin.all(16),
                    border_radius=ft.border_radius.all(18),
                    alignment=ft.alignment.center,
                    # expand=True,
                    ink=True,
                    height=60,
                    bgcolor=ft.Colors.with_opacity(0.2, ft.colors('black')),
                    # shadow = ft.BoxShadow(
                    #     spread_radius=1,
                    #     blur_radius=12,
                    #     color=ft.colors('black12'),
                    #     offset=ft.Offset(0, 0),
                    #     blur_style=ft.ShadowBlurStyle.OUTER,
                    # ),
                    content=ft.Text(
                        size=18,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.W_900,
                        font_family="Consolas",
                        color=ft.colors('yellow'),
                        value="Go to Market Place",
                    ),
                    on_click=lambda _:self.go_home_page(),
                ),
                ]
            )
        )
        self.content = ft.Column(
            controls = [
                self.save_column,
                self.congratulation_container,
            ]
        )
    
    def go_home_page(self):
        self.page.go('/home')

    def save_project(self,):

        # MAIN SCREEN PHONE
        self.screen_phone = self.page.session.get("SELECTED_SCREEN")

        # PHONE CONTENT CONTENT
        self.screen_widget = self.screen_phone.content.content

        # ATTRIBUTES COLUMN PHONE
        # self.column_atributes = self.screen_widget.content.content
        self.column_atributes = self.screen_widget.content.content.content.content.content

        # COLUMN CONTROLS OF PHONR
        # controls_widgets = self.screen_widget.content.content.controls
        controls_widgets = self.screen_widget.content.content.content.content.content.controls

        self.dict_attributes = {
            "container": self.screen_phone,
            "effect_container": self.screen_widget.content,
            "column_attributes":self.column_atributes
        }

        # SAVING DATA
        code_returned = refactory_flet_box(page=self.page)

        for widgets_recursion in controls_widgets:
            code_returned.get_widget_attributes(widget=widgets_recursion)

        # WRITE DATA IN FILES
        # code_returned.save_all_data(
        #             screen_name='main_screen',
        #             container_attributes=self.dict_attributes,
        #             one_file=True,
        #     )
        # WRITE DATA IN FILES
        code_returned.save_all_data(
                    screen_name='main_screen',
                    container_attributes=self.dict_attributes,
                    one_file=True,
            )

        self.save_column.visible=False
        self.congratulation_container.visible=True
        self.update()

if __name__ == '__main__':
    def main(page: ft.Page):
        page.scroll = "HIDDEN"  # AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        page.theme_mode = ft.ThemeMode.DARK  # ft.ThemeMode.LIGHT DARK
        page.theme = ft.Theme(color_scheme_seed=ft.Colors.TEAL)
        page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)

        page.window.left = 8
        page.window.top = 8
        page.window.height = 550
        page.window.width = 420
        page.padding = 8
        page.spacing = 8
        page.expand = True

        #:
        screen_1 = menu_save_container()

        page.add(screen_1)
        page.update()
    ft.app(
        # assets_dir = "assets",
        target=main,
        # port         = 8080,
        # view         = ft.AppView.WEB_BROWSER, #view=ft.WEB_BROWSER,
        # web_renderer = ft.WebRenderer.HTML
    )
