import flet as ft
import requests
import json

request_session = requests.Session()
#
testing = False

# COMENT THIS 2 LINES IN TESTING
from ..external_library.async_requests import async_requests
from ..external_library.sqlite_db import sqlite_db
# testing = True

def on_developing(self, name_seccion: str = str(), body_string: str = str()):
    # NEED IMPLEMENT YET
    if body_string == "":
        self.data = f"""Hello, User!\n\n{name_seccion.upper()}\n{body_string}"""
    else:
        # self.data = body_string
        self.data = f"""Hello, User!\n\n{name_seccion.upper()}\n\n{body_string}"""

    self.dialog_alert = ft.AlertDialog(
        on_dismiss=lambda e: print("Dialog dismissed!"),
        title=ft.Text(
            value=self.data,
            size=15
        ),
    )
    if self.page.overlay:
        self.page.overlay.pop()

    self.page.overlay.insert(0, self.dialog_alert)
    self.page.overlay[0].open = True
    self.page.update()
    # print(self.page.overlay)

class code_editor(ft.Container):
    opacity_markdown: float= 0.9

    def __init__(
        self,
        paren_widget: object = None,
        md_code: str=str(),
        visible: bool=False,
        page: object=None,
        ):
        super().__init__()
        self.page=page
        self.visible = visible
        self.paren_widget = paren_widget
        self.margin = ft.margin.all(0)
        self.bgcolor = ft.Colors.with_opacity(0.05, ft.colors('brown'))
        self.blur = (12,12)
        self.md_code = md_code

    def build(self):
        self.theme_name = 'solarized-dark'
        self.bgcolor = ft.Colors.with_opacity(0.05, ft.colors('white'))

        self.Markdown=ft.Markdown(
            value=self.md_code,
            scale=0.998,
            opacity=self.opacity_markdown,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB, # COMMON_MARK ,GITHUB_FLAVORED ,GITHUB_WEB
            code_theme=ft.MarkdownCodeTheme.GRUVBOX_DARK,
            code_style_sheet=ft.MarkdownStyleSheet(code_text_style=ft.TextStyle(font_family='Roboto Mono'),),
            md_style_sheet=ft.MarkdownStyleSheet(code_text_style=ft.TextStyle(font_family='Roboto Mono'),),
        )
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.VerticalAlignment.START,
            controls=[
                ft.Container(
                    padding=ft.padding.only(left=16,right=0,top=0,bottom=0),
                    expand=True,
                    opacity=self.opacity_markdown,
                    bgcolor="#282828",
                    content=ft.Column(
                            scroll="ALWAYS",
                            controls=[
                                self.Markdown
                            ],
                        ),
                ),

                # MARK DOWN EDITOR
                ft.Container(
                    content=ft.Row(
                    alignment= ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            tooltip="Home",
                            padding=ft.padding.all(0),
                            margin=ft.margin.all(0),
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(
                                        bgcolor=ft.Colors.with_opacity(opacity=0.2,color='cyan'),
                                        icon="home",
                                        on_click=lambda widget: self.hide_main_widget(widget=self),
                                    ),
                                ]
                            ),
                        ),
                        ft.Container(
                            tooltip="Copy",
                            padding=ft.padding.all(8),
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(
                                        bgcolor=ft.Colors.with_opacity(opacity=0.2,color='yellow'),
                                        icon="copy",
                                        on_click=lambda widget: self.copy_widget_template(markdown_text=self.Markdown.value),
                                    ),
                                ]
                            ),
                        ),
                    ]
                ),

                ),

            ]
        )

    def copy_widget_template(self,markdown_text) -> None:
        markdown_text = markdown_text.strip('```python').strip('```')
        self.page.set_clipboard(value=markdown_text)

        self.alert_dialog = self.page.session.get('on_dev')
        self.alert_dialog(
            name_seccion='Code was saved',
            body_string='[+] Module was saved paste a in a new file and run your flet App\n[+] Run Code:\n[+]>>> flet module_name.py'
        )

    def hide_main_widget(self, widget: object=None) -> None:
        widget.visible = False
        self.page.update()

class screen_phone(ft.Container):
    def __init__(self,page: object=None):
        super().__init__()
        self.page = page
        self.expand = True
        self.border_radius = ft.border_radius.all(16)
        self.padding = ft.padding.all(8)
        self.alignment = ft.alignment.center

    def build(self):
        self.content = ft.Container(
            padding=ft.padding.all(0),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            expand = True,
            width=320,
            border_radius=ft.border_radius.all(2),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors('black'),
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
        )


class lite_screen_manager(ft.Container):
    selected_text: str = 0
    old_payload = 0
    obtion_list = list()

    def __init__(self, page: object = None, tmp_screen_phone: object=None):
        super().__init__()
        self.page = page
        self.tmp_screen_phone = tmp_screen_phone
        self.ink = False
        self.alignment = ft.alignment.center

        # COMENT IF WILL DEV IN NORMAL MODE
        if testing:
            self.list_user_screen()

    def build(self):
        self.drop_down = ft.Dropdown(
            border_radius=ft.border_radius.all(16),
            border_width=0,
            width=160,
            label='Select screen',
            options=[
                ft.dropdown.Option(
                    key=f"Screen number: {_}"
                ) for _ in self.obtion_list
            ],
            on_change=lambda _: self.change_selected_input(
                payload=_.data)
        )

        self.content = ft.Container(
            width=320,
            # width=320,
            padding=ft.padding.all(4),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(30),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors('black'),
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),

            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[

                    # ADD ITEMS
                    ft.IconButton(
                        icon="add",
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.4,
                            color=ft.colors('purple')
                        ),
                        on_click=lambda _: self.add_drop_items()
                    ),

                    # DROP DOWN SELECTION ITEMS
                    self.drop_down,

                    # UPDATE ITEMS
                    ft.IconButton(
                        icon="update",
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.4,
                            color=ft.colors('green')
                        ),
                        on_click=lambda _: self.update_drop_items()
                    ),

                    # REMOVE ITEMS
                    ft.IconButton(
                        icon='delete',
                        bgcolor=ft.Colors.with_opacity(
                            opacity=0.4,
                            color=ft.colors('red')
                        ),
                        on_click=lambda _: self.delete_drop_items()
                    ),
                ],),
        )

    def update_drop_items(self):
        self.list_user_screen()
        if not self.obtion_list:
            return

        self.drop_down.options = [
            ft.dropdown.Option(key=f"Screen number: {self.obtion_list[0]}"),
        ]
        self.drop_down.update()

    def list_user_screen(self):
        """
        Loader screens in marketplace is by defauld load all screens
        """
        if self.page.session.get('flet_box_api'):
            self.obtion_list.clear()
            self.session_user_name = self.page.session.get('user_name').get('user_name')

            # kuko53348@gmail.com
            payload={'user_name': self.session_user_name}
            data_returned = async_requests(
                type='get',
                path='get_widgets',
                url=self.page.session.get("api_server"),
                payload=payload,
            )

            if not data_returned:
                on_developing(
                        self=self,
                        name_seccion='Connection Error',
                        body_string="Connection error between render.com and endpoint pythoneverywhere.com\nTry agan in flew seconds "
                    )

                return

            for index, _ in enumerate(data_returned):
                if not _ == "None" and index > 0:
                    print(f'index {index} Container')
                    self.obtion_list.append(index) # self.obtion_list.append(index)
                    # print(self.obtion_list)
        else:
            self.obtion_list.clear()
            #  CHECK THI PART
            return

            sqlite_obj = sqlite_db()
            data_returned = sqlite_obj.find_name(
                table_name='user_screen',
                column='user_name',
                # name='kuko53348',
                # name='user_demo',
                name=self.page.session.get('user_name').get('user_name')
            )

            for index, _ in enumerate(data_returned[0]):
                if not _ == "None" and index > 0:
                    # print(f'index {index} Container')
                    self.obtion_list.append(index)
                else:
                    # print(f'index {index} None')
                    self.obtion_list.append(_)

    def change_selected_input(self, payload):
        """
        Change content of screen phone in screen manager
        """

        self.old_payload = payload
        self.tmp_session_user_name = self.page.session.get('user_name').get('user_name')

        if self.page.session.get('flet_box_api'):
            # data_returned = request_session.get(f'{self.page.session.get("api_server")}get_widgets', params={'user_name': self.tmp_session_user_name})

            # kuko53348@gmail.com
            payload={'user_name': self.tmp_session_user_name}
            data_returned = async_requests(
                type='get',
                path='get_widgets',
                url=self.page.session.get("api_server"),
                payload=payload,
            )

            # if not data_returned:
            #     on_developing = self.page.session.get('on_dev')
            #     on_developing(
            #             self=self.page,
            #             name_seccion='Connection Error',
            #             body_string="Connection error between render.com and endpoint pythoneverywhere.com\nTry agan in flew seconds "
            #         )
            #     return

            self.data_selected = data_returned[1]
            self.app_data_selected = data_returned[2]

        else:
            sqlite_obj = sqlite_db()
            data_returned = sqlite_obj.find_name(
                table_name='user_screen',
                column='user_name',
                # name='kuko53348',
                # name='user_demo',
                name=self.tmp_session_user_name

            )

            # NECESSARY TAKE SELECTED SCREEN
            self.data_selected = data_returned[0][1]
            self.app_data_selected = data_returned[0][2]



        self.selected_screen = self.tmp_screen_phone

        # CHANGE CONTENT OF PHONE IN SCREEN MANAGER
        # self.selected_screen.content.content = ft.Container(bgcolor="red",height=120,width=120)
        self.selected_screen.content.content = self.load_module_from_string(
            page=self.page,
            string_code=self.data_selected
        )

        # WRITE IN  PHONE EDITOR
        self.Build_Phone_Editor = self.page.session.get('user_name_phone')
        self.Build_Phone_Editor.content = self.load_module_from_string(
            page=self.page,
            string_code=self.data_selected
        )

        # SET CODE IN CODE MARKDOWN
        self.page.session.set('MARK_DOWN_CODE', self.app_data_selected)

        self.Build_Phone_Editor.update()
        self.drop_down.options.clear()
        self.updating_phone(phone_attrib=self.Build_Phone_Editor.content.content)
        self.page.update()


    def updating_phone(self,phone_attrib: object=None):
        phone_attrib = phone_attrib

        # main_container in export data
        self.Build_Phone_Editor.parent.image=self.Build_Phone_Editor.content.content.image
        self.Build_Phone_Editor.parent.gradient=self.Build_Phone_Editor.content.content.gradient

        # second_container
        self.Build_Phone_Editor.content.content.bgcolor=self.Build_Phone_Editor.content.content.content.bgcolor
        self.Build_Phone_Editor.content.content.blur=self.Build_Phone_Editor.content.content.content.blur

    def add_drop_items(self):
        return

        print(self.drop_down.options)

    def load_module_from_string(self, page, string_code: str = str()) -> object:
        import importlib.util
        # import sys

        spec = importlib.util.spec_from_loader('dynamic_module', loader=None)
        module = importlib.util.module_from_spec(spec)
        exec(string_code, module.__dict__)
        # sys.modules['dynamic_module'] = module
        globals()['dynamic_module'] = module
        tmp_module = dynamic_module.load_module_str() # type: ignore
        return tmp_module

class go_home_screen(ft.Container):

    def __init__(self, page: object = None, main_screen: object = None):
        super().__init__()
        self.page = page
        self.alignment = ft.alignment.center
        self.main_screen = main_screen
    def build(self):
        self.content = ft.Container(
            width=160,
            # bgcolor=ft.colors('black12'),
            padding=ft.padding.all(8),
            margin=ft.margin.all(2),
            border_radius=ft.border_radius.all(32),

            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors('black'),
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            content=ft.ElevatedButton(
                text="Apply widgets",
                bgcolor=ft.Colors.with_opacity(
                    opacity=0.4,
                    color=ft.colors('purple')
                ),
                on_click=lambda _: self.go_main_screen(),

            ),
        )

    def go_main_screen(self):
        # RESET SELECTED WIDGET TO EVOIT ISSUES
        self.reset_border_select_widget()

        self.page.views[1].controls[1].visible = False
        self.page.views[1].controls[0].visible = True
        self.page.views[1].update()

    def reset_border_select_widget(self) -> None:
        """
        Note:
            remove clean all editro tab and selected widget before save data in database
        """
        self.widget_selected = self.page.session.get("SELECTED_CONTAINER")

        # REMOVE BORDER COLOR BEFORE SAVE
        if not self.widget_selected == None:
            self.widget_selected.border = ft.border.all(
                2, ft.colors('transparent'))

        self.config_tab_container = self.page.session.get(
            "CONFIG_TABS_CONTAINERS")
        self.config_tab_container_content = self.page.session.get(
            "CONFIG_TABS_CONTAINERS_CONTENT")

        # REMOVE VISIBLE TAB EDITOR BEFORE SAVE
        self.config_tab_container.visible=False
        self.config_tab_container_content.visible=False

        # RESET TO NONE TOUCH WIDGET
        self.page.session.set("SELECTED_CONTAINER", None)
        self.page.update()

class get_sources_code(ft.Container):

    def __init__(self, page: object = None, code_editor: object = None):
        super().__init__()
        self.page = page
        self.alignment = ft.alignment.center
        self.code_editor = code_editor
        self.expand = True

    def build(self):
        self.content = ft.Container(
            padding=ft.padding.all(8),
            margin=ft.margin.all(2),
            border_radius=ft.border_radius.all(32),

            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors('black'),
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            content=ft.ElevatedButton(
                text="Get Code",
                bgcolor=ft.Colors.with_opacity(
                    opacity=0.4,
                    color=ft.colors('blue'),
                ),
                on_click= lambda _: self.show_code_editor(),

            ),
        )

    def show_code_editor(self):
        mark_down_code = self.page.session.get('MARK_DOWN_CODE')    # <== MARKDOWN CODE IN PHONE SCREEN
        self.tmp_markdown = self.code_editor.controls[1]
        self.tmp_markdown.Markdown.value = f"""```python\n{mark_down_code}```"""
        self.tmp_markdown.visible = True

        self.page.update()

class delete_project(ft.Container):

    def __init__(self, page: object = None, code_editor: object = None):
        super().__init__()
        self.page = page
        self.alignment = ft.alignment.center
        self.code_editor = code_editor
        self.expand = True

    def build(self):
        self.content = ft.Container(
            padding=ft.padding.all(8),
            margin=ft.margin.all(2),
            border_radius=ft.border_radius.all(32),
            bgcolor = ft.Colors.with_opacity(0.6,ft.colors('red')),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors('black'),
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            content=ft.Icon(name='home'),
            on_click= lambda _: self.back_home(),

            )

    def back_home(self):
        # RESET SELECTED WIDGET TO EVOIT ISSUES
        self.page.views[1].controls[1].visible = False
        self.page.views[1].controls[0].visible = True
        self.page.views[1].update()

class screen_manager(ft.Container):
    # tmp_screen_phone = screen_phone()

    def __init__(self, page: object = None, visible: bool = True,  code_editor: object=None, tmp_screen_phone: object=None):
        super().__init__()
        self.page = page
        self.visible = visible
        self.code_editor = code_editor
        self.padding = ft.padding.all(8)
        self.margin = ft.margin.all(8)
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(32)

        self.tmp_screen_phone = tmp_screen_phone

        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors('black'),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )

    def build(self):
        # tmp_screen_phone = screen_phone()

        self.content = ft.Column(
            # alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END

            controls=[
                lite_screen_manager(
                    page=self.page,
                    tmp_screen_phone=self.tmp_screen_phone,
                ),
                self.tmp_screen_phone,
                ft.Container(
                    content=ft.Row(
                        controls=[
                            go_home_screen(
                                page=self.page,
                                main_screen=self
                            ),
                            get_sources_code(
                                page=self.page,
                                code_editor=self.code_editor
                            ),
                            delete_project(
                                page=self.page,
                                code_editor=self.code_editor
                            ),
                        ]
                    )
                )
            ],
        )

class middle_container(ft.Container):
    def __init__(self,title: str = str(),procces_data: list=list(),tmp_screen_phone: object=None):
        super().__init__()
        self.title = title
        self.procces_data =procces_data
        self.padding=ft.padding.all(8)
        self.tmp_screen_phone = tmp_screen_phone

    def build(self):
        self.content = ft.Column(
            controls=[
                ft.Container(
                    padding=ft.padding.only(left=8,top=4,right=8,bottom=4),
                    content=ft.Text(
                        weight=ft.FontWeight.BOLD,
                        value=self.title
                    )
                ),
                ft.Container(
                    width=340,
                    expand=True,
                    ink=False,
                    border_radius=ft.border_radius.all(12),
                    alignment=ft.alignment.top_left,

                    content=ft.Row(
                        rtl=True,
                        scroll='auto',
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        alignment = ft.MainAxisAlignment.START,
                        spacing=4,
                        run_spacing=4,
                        wrap=True,
                        controls=[

                        ]
                    )
                ),
            ]
        )

        for tmp_list in self.procces_data:
            self.user_name = tmp_list[0]
            self.table_name = tmp_list[1]
            self.app_name = tmp_list[2]
            self.ranking_stars = tmp_list[3]
            self.dragg_widget = tmp_list[4]
            self.code_widget = tmp_list[5]
            self.time_created = tmp_list[6]

            self.content.controls[1].content.controls.append(
                            ft.Container(
                                width=100,
                                height=130,
                                ink=True,
                                ink_color=ft.colors('blue'),
                                padding=ft.padding.all(0),
                                margin=ft.margin.all(2),
                                border_radius=ft.border_radius.all(12),
                                border=ft.border.all(width=1,color=ft.colors('black12')),
                                bgcolor=ft.colors('black38'),
                                shadow=ft.BoxShadow(
                                    spread_radius=1,
                                    blur_radius=15,
                                    color=ft.colors('black45'),
                                    offset=ft.Offset(0, 0),
                                    blur_style=ft.ShadowBlurStyle.OUTER,
                                ),
                                content=projects_made(
                                                user_name = self.user_name,
                                                table_name = self.table_name,
                                                app_name = self.app_name,
                                                ranking_stars = self.ranking_stars,
                                                dragg_widget = self.dragg_widget,
                                                code_widget = self.code_widget,
                                                time_created = self.time_created.split(' ')[0],
                                                tmp_screen_phone = self.tmp_screen_phone
                                        ),

                            on_click= lambda widget_name: print(widget_name.control),

                            )
                )


class projects_made(ft.Container):
    def __init__(
        self,
        user_name: str = str(),
        table_name: str = str(),
        app_name: str = str(),
        ranking_stars: str = str(),
        dragg_widget: str = str(),
        code_widget: str = str(),
        time_created: str = str(),
        tmp_screen_phone: object = None,
    ):
        super().__init__()

        self.user_name = user_name
        self.table_name = table_name
        self.app_name = app_name
        self.ranking_stars = ranking_stars
        self.dragg_widget = dragg_widget
        self.code_widget = code_widget
        self.time_created = time_created

        self.tmp_screen_phone = tmp_screen_phone
        self.ink = True
        self.ink_color = ft.Colors.with_opacity(0.8, ft.colors('cyan'))
        self.expand=True
        self.image = ft.DecorationImage(
                src='backend.webp',
                fit=ft.ImageFit.COVER,
                opacity=0.02
            )

    def build(self):

        self.content = ft.Column(
            spacing=0,
            run_spacing=0,

            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # control number 0
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0,
                    run_spacing=0,

                    controls=[
                        ft.IconButton(
                            icon=ft.icons('star'),
                            selected_icon=ft.icons('star'),
                            selected=False,
                        ),

                        ft.Text(
                            text_align=ft.TextAlign.CENTER,
                            expand=True,
                            weight=ft.FontWeight.BOLD,
                            font_family="Consolas",  # "Consolas ,RobotoSlab
                            color=ft.Colors.with_opacity(
                                0.8, ft.colors('white')),
                            value=self.ranking_stars
                        ),
                    ]
                ),
                # control number 1
                ft.Container(
                    padding=ft.padding.all(4),
                    content=ft.Column(
                        spacing=0,
                        run_spacing=0,
                        controls=[
                            ft.Text(
                                weight=ft.FontWeight.BOLD,
                                font_family="Consolas",  # "Consolas ,RobotoSlab
                                color=ft.Colors.with_opacity(0.7, ft.colors('white')),
                                size=10,
                                value=self.user_name,
                            ),
                            # control number 2
                            ft.Text(
                                weight=ft.FontWeight.BOLD,
                                font_family="Consolas",  # "Consolas ,RobotoSlab
                                color=ft.Colors.with_opacity(0.7, ft.colors('white')),
                                size=13,
                                value=self.app_name,
                            ),
                            # control number 3
                            ft.Text(
                                weight=ft.FontWeight.BOLD,
                                font_family="Consolas",  # "Consolas ,RobotoSlab
                                color=ft.Colors.with_opacity(0.7, ft.colors('white')),
                                size=13,
                                value=self.time_created,
                            ),

                        ]
                    )
                )
            ]
        )

        self.on_click = lambda widget_parent: self.activate_screen()

    def activate_screen(self,) -> object():
        """Return widget screen to load

        Args:
            widget (object, optional): _description_. Defaults to None)->object()
        """
        tmp_screen_phone = self.tmp_screen_phone

        self.selected_screen = tmp_screen_phone

        # NECESSARY TAKE SELECTED SCREEN
        self.data_selected = self.dragg_widget

        self.selected_screen.content.content = self.load_module_from_string(
            page=self.page,
            string_code=self.data_selected
        )

        # WRITE IN  PHONE EDITOR
        self.Build_Phone_Editor = self.page.session.get('user_name_phone')
        self.Build_Phone_Editor.content = self.load_module_from_string(
            page=self.page,
            string_code=self.data_selected
        )

        # SET CODE IN CODE MARKDOWN
        self.page.session.set('MARK_DOWN_CODE', self.code_widget)
        self.Build_Phone_Editor.update()

        # self.page.update()
        self.selected_screen.update()

        # run only in production
        # print('='*20)
        # print(self.user_name)
        # print(self.table_name)
        # print(self.app_name)
        # print(self.ranking_stars)
        # print(self.dragg_widget)
        # print(self.code_widget)
        # print(self.time_created)


    def load_module_from_string(self, page, string_code: str = str()) -> object:
        import importlib.util
        spec = importlib.util.spec_from_loader('dynamic_module', loader=None)
        module = importlib.util.module_from_spec(spec)
        exec(string_code, module.__dict__)
        globals()['dynamic_module'] = module
        tmp_module = dynamic_module.load_module_str() # type: ignore
        return tmp_module

class project_manager(ft.Stack):
    """
    project_tab = [
            'Splash',
            'Introduction',
            'Login',
            'LoginRegister',
            'Lock',
            'MixViews',
            'GridView',
            'ListView',
            'DashBoard',
            'Payment',
            'Shopping',
            'Music',
            'SettingView',
            'Verification',
            'About'
        ]
    """
    TABS_PROJECTS: list = {
        'Splash': ft.Icons('do_not_touch'),
        'Introduction': ft.Icons('start'),
        'Login': ft.Icons('login'),
        'LoginRegister': ft.Icons('how_to_reg'),
        'Lock': ft.Icons('block'),
        'MixViews': ft.Icons('dashboard'),
        'GridView': ft.Icons('grid_view_rounded'),
        'ListView': ft.Icons('grading'),
        'DashBoard': ft.Icons('dashboard'),
        'Payment': ft.Icons('account_balance_wallet'),
        'Shopping': ft.Icons('shopping_bag'),
        'Music': ft.Icons('speaker_group_rounded'),
        'SettingView': ft.Icons('settings'),
        'Verification': ft.Icons('verified'),
        'About': ft.Icons('account_box'),
    }


    def __init__(self, page: object = None, visible: bool = True):
        super().__init__()
        self.page = page
        self.expand = True
        self.visible = visible

    def build(self):
        self.tmp_screen_phone = screen_phone(page= self.page )

        self.nav_rail = ft.Container(
            width=80,
            content=ft.Column(
                scroll='hidden',
                controls=[
                    ft.Container(
                        ink=True,
                        width=80,
                        ink_color=ft.colors('blue'),
                        padding=ft.padding.all(10),
                        margin=ft.margin.all(0),
                        border_radius=ft.border_radius.all(12),
                        border=ft.border.all(width=1,color=ft.Colors.with_opacity(opacity=0.05, color=ft.colors('white'))),
                        bgcolor=ft.colors('black12'),
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.colors('black45'),
                            offset=ft.Offset(1, 0),
                            blur_style=ft.ShadowBlurStyle.OUTER,
                        ),
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            run_spacing=0,
                            spacing=0,
                            controls=[
                                ft.Icon(
                                    name=self.TABS_PROJECTS.get(tabs_name),
                                ),
                                ft.Text(
                                    value=tabs_name,
                                    weight=ft.FontWeight.BOLD,
                                    size=12,
                                )

                            ],
                        ),
                    on_click= lambda widget_name: print(widget_name.control.content.controls[1].value),
                    ) for tabs_name in self.TABS_PROJECTS
                ]
            )

        )

        self.parent_middle_grid_container = ft.Row(
            scroll='auto',
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment = ft.MainAxisAlignment.CENTER,
            expand=True,
            controls=[
                # middle_container(title=tabs_name) for tabs_name in self.TABS_PROJECTS
                ]
            )


        self.content = ft.Container(
            image = ft.DecorationImage(
                    src='backend.webp',
                    fit=ft.ImageFit.COVER,
                    opacity=0.015
                ),
            content=ft.Row(
                controls=[
                    # NAV RAIL
                    self.nav_rail,
                    # RIGHT WIDGETS
                    ft.Column(
                        expand=True,
                        controls=[
                            self.parent_middle_grid_container,

                            ft.Container(
                                ink=True,
                                ink_color=ft.colors('blue'),
                                padding=ft.padding.only(left=12,top=12,bottom=12,right=12),
                                margin=ft.margin.only(left=8,top=0,bottom=8,right=8),
                                bgcolor=ft.colors('black12'),
                                content=ft.Icon(name='discord'),
                                border_radius=ft.border_radius.all(18),
                                on_click= lambda _:print(_.control)
                            )
                            ]
                    ),
                    # screen_phone(),
                    screen_manager(
                        page=self.page,
                       code_editor=self,
                       tmp_screen_phone=self.tmp_screen_phone
                    )
                ],
            ),
        )
        self.controls = [
                self.content,
                code_editor(paren_widget=self, visible=False)
            ]

        self.loading_all_data()

    def list_projects_tabs(self, table_name: str=str()) -> list:
        """
        ### List all widgets in selected projects in database

        ```python

        >>> self.list_projects_tabs(table_name='Verification')
        ```
        Parameters:
        return ('kuko53348', 'Splash', 'exemple', '5', 'ft.DraggContainer()', 'ft.Container()', '14-15-15')

        """
        if self.page.session.get('flet_box_api'):

            try:
                data_returned = request_session.get(f'{self.page.session.get("api_server")}get_projects_widgets', params={'table_name': table_name})
                data_returned = data_returned.json()
                # print(data_returned)
            except Exception as error:
                import os
                os.system('clear')
                data_returned = False
                print('CONNECT FAST API\n\n[+] >>> source .venv/bin/activate\n[+] >>> uvicorn --app-dir "./flet_box_api_server/" main:app --host 0.0.0.0 --port 8080 --reload')

        else:
            sqlite_obj = sqlite_db()
            data_returned = sqlite_obj.find_all(table_name=table_name)

        # return
        # middle_container(title=tabs_name)

        if data_returned:
            self.parent_middle_grid_container.controls.append(
                middle_container(
                    title=table_name,
                    procces_data=data_returned,
                    tmp_screen_phone= self.tmp_screen_phone,
                    )
                )

    def loading_all_data(self, index_rail: int = int()):

        self.list_projects_tabs(table_name='Splash')
        self.list_projects_tabs(table_name='Introduction')
        self.list_projects_tabs(table_name='Login')
        self.list_projects_tabs(table_name='LoginRegister')
        self.list_projects_tabs(table_name='Lock')
        self.list_projects_tabs(table_name='MixViews')
        self.list_projects_tabs(table_name='GridView')
        self.list_projects_tabs(table_name='ListView')
        self.list_projects_tabs(table_name='DashBoard')
        self.list_projects_tabs(table_name='Payment')
        self.list_projects_tabs(table_name='Shopping')
        self.list_projects_tabs(table_name='Music')
        self.list_projects_tabs(table_name='SettingView')
        self.list_projects_tabs(table_name='Verification')
        self.list_projects_tabs(table_name='About')

if __name__ == '__main__':

    def main(page: ft.Page):
        # page.scroll='ALWAYS'
        page.theme_mode = ft.ThemeMode.DARK  # ft.ThemeMode.LIGHT DARK
        screen_1 = project_manager(page=page)
        page.add(screen_1)
        page.update()

    ft.app(
        target=main,
    )
