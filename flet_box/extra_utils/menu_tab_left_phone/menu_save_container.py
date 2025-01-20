import flet as ft
from datetime import datetime

from .congratulation_menu import congratulation_menu
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
    save_projects_name: dict = {
        'column_tab': None,
        'project_name': None,

    }
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
        self.button_save_project = ft.Container(
                    padding=ft.padding.all(8),
                    margin=ft.margin.all(16),
                    border_radius=ft.border_radius.all(18),
                    alignment=ft.alignment.center,
                    height=48,
                    bgcolor=ft.Colors.with_opacity(0.04, ft.colors('blue200')),
                    disabled=True,
                    content=ft.Text(
                        size=18,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.W_900,
                        font_family="Consolas",
                        color=ft.colors('blue200'),
                        value="Create module",
                    ),
                    on_click=lambda tmp_widget:self.validate_save_project(widget_name=tmp_widget)
                )

        self.save_column = ft.Column(
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
        self.save_column_congratulation = congratulation_menu(page=self.page,visible=False, hide_widget=self.save_column)
        self.content = ft.Column(
            controls = [
                self.save_column,
                self.save_column_congratulation,
            ]
        )

    def go_home_page(self, same_page: bool=False):
        self.page.views[1].controls[0].visible=True
        self.page.views[1].controls[1].visible=False
        self.page.views[1].controls[2].visible=False
        self.page.views[1].update()

        if not same_page:
            self.page.go('/congratulation')

    def activation_save_project_button(self, widget_name: object = None) -> None:
        if self.save_projects_name.get('project_name') and self.save_projects_name.get('column_tab'):
            widget_name.disabled = False
        else:
            widget_name.disabled = True

        widget_name.update()

    def project_name(self,widget_name: object=None) -> None:
        """
        Set value in dict self.save_projects_name ['project_name']
        """
        self.save_projects_name['project_name']=widget_name.value
        self.activation_save_project_button(widget_name=self.button_save_project)


    def column_name(self,widget_name: object=None) -> None:
        """
        Set value in dict self.save_projects_name ['column_tab']
        """
        self.save_projects_name['column_tab']=widget_name.key
        self.activation_save_project_button(widget_name=self.button_save_project)

    def validate_save_project(self,widget_name: object=None) -> None:
        column_tab = self.save_projects_name.get('column_tab')
        project_name = self.save_projects_name.get('project_name')

        print(column_tab, project_name)

        # save_project_module will set save as a module True

        data_returned = self.save_project(
                save_project_module=True,
                column_tab_db=column_tab,
                name_project_db=project_name,
                time_created_db=str(datetime.now())
        )
        if data_returned:
            self.page.go('/congratulation')

    def save_project(self,save_project_module: bool= False , column_tab_db: str=str(), name_project_db: str=str(), time_created_db: str=str()):

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
        # print(f'<<<<< {self.page.session}')
        # self.page.session.set('user_name', {'user_name': 'kuko53348'})
        # code_returned.get_widget_attributes(widget=controls_widgets[0])

        for widgets_recursion in controls_widgets:
            code_returned.get_widget_attributes(widget=widgets_recursion)

        # WRITE DATA IN FILES
        # code_returned.save_all_data(
        #             screen_name='main_screen',
        #             container_attributes=self.dict_attributes,
        #             one_file=True,
        #     )
        # WRITE DATA IN FILES
        if save_project_module:
            # save_project_module will save as a project module
            # one_file=True, will have all in one screen

            # ONLY APP WIDGET
            data_returned = code_returned.save_all_data(
                        save_project_module=save_project_module,
                        one_file=True,

                        column_tab_db = column_tab_db,
                        name_project_db = name_project_db,
                        time_created_db = time_created_db,

                        screen_name='main_screen',
                        container_attributes=self.dict_attributes,
                )

        else:

            data_returned = code_returned.save_all_data(
                        screen_name='main_screen',
                        container_attributes=self.dict_attributes,
                        one_file=True,
                )
        data = self.page.pubsub.send_all('/congratulation')

        # self.page.go('/congratulation')

        # self.congratulation_container.visible=True
        # congratulation_menu(page=self.page)

        print(self.save_column.visible)
        self.save_column.visible = False if self.save_column.visible else True
        self.save_column_congratulation.visible = True if not self.save_column.visible else False

        self.page.update()

        # self.save_column.visible=False
        # self.go_home_page(same_page=True)

        # congratulation_menu(page=self.page)

        # self.update()
        # if data_returned == None:
        #     # print('<<<<<<<<< here')
        #     # self.page.go('/congratulation')
        #     try:
        #         self.page.go('/congratulation')
        #     except Exception as e:
        #         return
        # else:
        #     return False

if __name__ == '__main__':
    def main(page: ft.Page):
        page.scroll = "HIDDEN"  # AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        page.theme_mode = ft.ThemeMode.DARK  # ft.ThemeMode.LIGHT DARK
        page.theme = ft.Theme(color_scheme_seed=ft.colors('white'))
        page.dark_theme = ft.Theme(color_scheme_seed=ft.colors('blue'))

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
