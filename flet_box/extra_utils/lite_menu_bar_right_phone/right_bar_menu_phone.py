# from ..tree_view.tree_view import TreeViewS
import flet as ft


class LiteMenuUpContainer(ft.Container):
    def __init__(
        self,
        page: object = None,
        phone_widget_container: object = None,
        menu_left_container: object = None,
        menu_right_container: object = None,
    ):
        super().__init__()
        self.page = page
        self.menu_left_container = menu_left_container
        self.phone_widget_container = phone_widget_container
        self.menu_right_container = menu_right_container
        self.ink = False
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(30)
        self.blur = (16, 16)

    def build(self):
        self.phone_edition = ft.Container(
            padding=ft.padding.all(2),
            bgcolor=ft.colors("black26"),
            ink=False,
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(30),
            border=ft.border.all(2, ft.colors("black12")),
            content=ft.Row(
                spacing=8,
                controls=[
                    ft.IconButton(
                        icon=ft.icons("smartphone"),
                        tooltip="SMARTPHONE",
                        on_click=lambda _: self.action_button(action="SMARTPHONE"),
                    ),
                    ft.IconButton(
                        icon=ft.icons("tablet_android"),
                        tooltip="TABLET",
                        on_click=lambda _: self.action_button(action="TABLET"),
                    ),
                    ft.IconButton(
                        icon=ft.icons("tv_outlined"),
                        tooltip="PC",
                        on_click=lambda _: self.action_button(action="PC"),
                    ),
                    ft.IconButton(
                        icon=ft.icons("screenshot_monitor"),
                        tooltip="FULL SCREEN",
                        on_click=lambda _: self.action_button(action="SHOW PC"),
                    ),
                    ft.IconButton(
                        icon=ft.icons("screen_rotation"),
                        tooltip="ROTATE",
                        on_click=lambda _: self.action_button(action="rotation"),
                    ),
                    # ft.IconButton(
                    #     icon=ft.icons.SCHEMA,
                    #     tooltip="TREE",
                    #     on_click=lambda _: self.action_button(
                    #         action="TREE"
                    #     ),
                    # ),
                ],
            ),
        )

        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=True,
            controls=[
                ft.Container(
                    ink=False,
                    blur=(16, 16),
                    bgcolor=ft.Colors.with_opacity(0.12, "white"),
                    padding=ft.padding.only(left=4, top=0, right=4, bottom=0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(30),
                    border=ft.border.all(2, ft.Colors.with_opacity(0.12, "white")),
                    content=ft.Row(
                        spacing=8,
                        controls=[
                            ft.IconButton(
                                icon=ft.icons("edit_square"),
                                tooltip="EDIT WIDGET",
                                on_click=lambda _: self.modify_widget_in_phone_container(),
                                bgcolor="Blue",
                                icon_color="White",
                            ),
                            ft.IconButton(
                                icon=ft.icons("touch_app"),
                                tooltip="UN SELECT\nBORDER WIDGET",
                                on_click=lambda _: self.action_button(
                                    action="UNSELECT"
                                ),
                                bgcolor=ft.colors("white24"),
                                icon_color="White",
                            ),
                            ft.IconButton(
                                icon=ft.icons("deblur"),
                                tooltip="LIGHT / DARK",
                                on_click=lambda _: self.action_button(
                                    action="LIGHT / DARK"
                                ),
                            ),
                            ft.IconButton(
                                icon=ft.icons("delete_sweep_outlined"),
                                tooltip="DELETE_",
                                on_click=lambda _: self.action_button(action="delete"),
                            ),
                            ft.IconButton(
                                icon=ft.icons("recycling"),
                                tooltip="CLEAR",
                                on_click=lambda _: self.action_button(action="clear"),
                                bgcolor=ft.colors("red900"),
                            ),
                            self.phone_edition,
                        ],
                    ),
                ),  # <=== NOTE COMA
                # self.phone_edition
            ],
        )

        self.check_size_page()

        # )  # <=== NOTE COMA
        # return self.Drop_LiteMenuUpContainer

    def check_size_page(self) -> bool:
        """
        :Return size of screen to addapt main screen to config container widget
        """
        page_width = self.page.width

        if page_width <= 690.0:
            self.phone_edition.visible = False

    def modify_widget_in_phone_container(self):
        """
        GLOBAL VARS:
            config_tab_container
            self.config_tab_container_content

        NOTE:
            IS NECESSARY ADD THIS 2 GLOVAL VAR TO CALL TAB MENU AND MAKE
            CHANGES IN STRAMING

        GLOBAL VARS:
            self.select_droped_widget
            self.select_droped_widget_CONTENT

        NOTE:
            EVERY TIME THAT IS SELECTED WIDGET INSIDE THE PHONE.
            THIS 2 VAR ARE CHANGE EVERY TIME THAT DETECT ONE CLICK
            AND AFTER PERES BUTTON EDIT WILL CALL THIS METOD TO
            CHANGE PROPERTY
        """
        self.select_droped_widget = self.page.session.get("SELECTED_CONTAINER")
        self.select_container_id = self.page.session.get("SELECTED_CONTAINER_ID")

        # TAB BOX EDITION OF CONTAINER WIDGET
        self.config_tab_container = self.page.session.get("CONFIG_TABS_CONTAINERS")

        # TAB BOX EDITION OF CONTAINER CONTENT WIDGET
        self.config_tab_container_content = self.page.session.get(
            "CONFIG_TABS_CONTAINERS_CONTENT"
        )

        is_selected = False

        if not self.select_droped_widget == None:
            is_selected = True
            self.select_droped_widget_CONTENT = self.select_droped_widget.content

            #: 'Position','Modification','Color','Image',
            self.control_tab_2 = self.config_tab_container.content.controls
            self.control_tab_3 = self.config_tab_container_content.content.controls

            print(
                f"[Selected] to edit: [{self.select_droped_widget.tooltip}] ID: right_bar_menu_phone.py"
            )

            self.menu_right_container.visible = True
            self.menu_right_container.update()
            self.page.update()

            #  'left', 'top', 'right', 'bottom', 'rotate', 'scale', 'offset'
            self.list_wdiget_content_attribute = []
            self.list_wdiget_content_attribute: list = (
                self.select_droped_widget_CONTENT.__dir__()
            )

            list_range: tuple = ("2_0", "2_1", "2_2", "2_3")

            list_range_tab_3: tuple = (
                "3_0",
                "3_1",
                "3_2",
                "3_3",
                "3_4",
                "3_5",
                "3_6",
                "3_7",
            )

        if is_selected:
            self.config_tab_container.visible = True
            self.config_tab_container.update()

            for index, tab_name in enumerate(list_range):
                """
                VERY IMPORTAN THIS LOOP WILL INSERT IN TABS CONFIG
                SELECTED WIDGET TO EDIT DEPENDING [ CONTAINER ]

                WILL SHOW VISIBLE IF IF IN ATTRIBUTES
                """

                self.insert_data_in_box_container(
                    column_tab=tab_name,
                    tab_control=self.control_tab_2[index],
                    widget_name=self.select_droped_widget,
                )

            # #: TAB 3 <== CALLING METHOD VISIBLE OR ONT VISIBLE
            self.config_tab_container_content.visible = True
            self.config_tab_container_content.update()

            for index, tab_name in enumerate(list_range_tab_3):
                """
                VERY IMPORTAN THIS LOOP WILL INSERT IN TABS CONFIG
                SELECTED WIDGET TO EDIT DEPENDING [ CONTENT ]

                WILL SHOW VISIBLE IF IF IN ATTRIBUTES
                """
                self.insert_data_in_box_container_content(
                    column_tab=tab_name,
                    tab_control=self.control_tab_3[index],
                    widget_name=self.select_droped_widget_CONTENT,
                )

        else:
            #: TAB 2
            self.config_tab_container.visible = False
            self.config_tab_container.update()

            #: TAB 3
            self.config_tab_container_content.visible = False
            self.config_tab_container_content.update()

    def action_button(self, action):
        # SETTING PHONE TO ROTATE AND EDIT
        # self.phone_widget_container  = self.page.session.get('SELECTED_SCREEN')
        self.select_droped_widget = self.page.session.get("SELECTED_CONTAINER")
        self.select_container_id = self.page.session.get("SELECTED_CONTAINER_ID")

        self.phone_widget_blur_cont = self.phone_widget_container.content

        if action == "delete":

            if not self.select_container_id == None:
                self.delete_widget()

        if action == "UNSELECT":
            if not self.select_droped_widget == None:
                self.select_droped_widget.border = ft.border.all(
                    2, ft.colors("transparent")
                )
                self.select_droped_widget.update()

        if action == "clear":
            """
            CLEAR ALL WIDGET FROM SCREEN PHONE
            """
            self.clear_all_phone_widgets()

        if action == "TREE":
            TreeView.visible_view()

        if action == "rotation":
            self.phone_widget_blur_cont.width, self.phone_widget_blur_cont.height = (
                self.phone_widget_blur_cont.height,
                self.phone_widget_blur_cont.width,
            )
            self.phone_widget_container.width, self.phone_widget_container.height = (
                self.phone_widget_container.height,
                self.phone_widget_container.width,
            )
            self.phone_widget_blur_cont.update()
            self.phone_widget_container.update()

            if self.phone_widget_container.width >= 600:
                self.menu_right_container.visible = (
                    False if self.menu_right_container.visible else True
                )
                self.menu_left_container.visible = (
                    False if self.menu_right_container.visible else True
                )
                self.menu_left_container.update()
                self.menu_right_container.update()

        if action == "LIGHT / DARK":
            self.light_color = ft.Colors.with_opacity(0.1, ft.colors.SURFACE_VARIANT)
            self.dark_color = ft.Colors.with_opacity(0.6, ft.colors("black"))
            self.phone_widget_container.dark_theme = ft.Theme(
                color_scheme_seed=ft.Colors.YELLOW
            )

            self.phone_widget_container.theme_mode = (
                ft.ThemeMode.DARK
                if self.phone_widget_container.theme_mode == ft.ThemeMode.LIGHT
                else ft.ThemeMode.LIGHT
            )
            self.phone_widget_container.bgcolor = (
                self.dark_color
                if self.phone_widget_container.bgcolor == self.light_color
                else self.light_color
            )
            self.phone_widget_container.update()

        if action == "SMARTPHONE":
            self.phone_widget_container.width = 320
            self.phone_widget_blur_cont.width = self.phone_widget_container.width
            self.phone_widget_container.height = 567
            self.phone_widget_blur_cont.height = self.phone_widget_container.height
            self.phone_widget_blur_cont.update()
            self.phone_widget_container.update()

            self.menu_left_container.visible = True
            self.menu_right_container.visible = True
            self.menu_left_container.update()
            self.menu_right_container.update()

        if action == "TABLET":
            #: Phone Container offset
            self.phone_widget_container.width = 480
            self.phone_widget_blur_cont.width = self.phone_widget_container.width
            self.phone_widget_container.height = 768
            self.phone_widget_blur_cont.height = self.phone_widget_container.height

            self.phone_widget_blur_cont.update()
            self.phone_widget_container.update()

            self.menu_left_container.visible = True
            self.menu_right_container.visible = True
            self.menu_left_container.update()
            self.menu_right_container.update()

        if action == "PC":
            self.phone_widget_container.width = 1240
            self.phone_widget_blur_cont.width = self.phone_widget_container.width
            self.phone_widget_container.height = 720
            self.phone_widget_blur_cont.height = self.phone_widget_container.height
            self.phone_widget_blur_cont.update()
            self.phone_widget_container.update()

            # self.menu_right_container.visible = (
            #     False if self.menu_right_container.visible else True
            # )
            # self.menu_left_container.visible = (
            #     False if self.menu_right_container.visible else True
            # )
            self.menu_left_container.update()
            self.menu_right_container.update()

        if action == "SHOW PC":
            self.width_ = 1024

            if self.menu_left_container.visible and self.menu_right_container.visible:
                self.menu_left_container.visible = False
                self.menu_right_container.visible = False

            elif (
                not self.menu_left_container.visible
                and not self.menu_right_container.visible
            ):
                if self.phone_widget_container.width >= 500:
                    self.phone_widget_container.width = 480
                    self.phone_widget_blur_cont.width = (
                        self.phone_widget_container.width
                    )

                    self.phone_widget_container.height = 768
                    self.phone_widget_blur_cont.height = (
                        self.phone_widget_container.height
                    )
                    self.phone_widget_blur_cont.update()
                    self.phone_widget_container.update()
                self.menu_left_container.visible = True
                self.menu_right_container.visible = True

            elif (
                not self.menu_left_container.visible
                and self.menu_right_container.visible
            ):
                self.menu_left_container.visible = False
                self.menu_right_container.visible = False

            elif (
                self.menu_left_container.visible
                and not self.menu_right_container.visible
            ):
                self.menu_left_container.visible = False
                self.menu_right_container.visible = False

            self.menu_left_container.update()
            self.menu_right_container.update()

    def check_number_column(self, tab_control: object = object()):
        """
        { extract data for column to edid widget select }

        :param      tab_control:  The tab control
        :type       tab_control:  object
        """
        column_controls = tab_control  #
        return column_controls.content.controls[1].content.controls

    def insert_data_in_box_container(
        self,
        column_tab: str = "",
        tab_control: list = list(),
        widget_name: object = object(),
    ):
        """
        - WALK ALL TABS TO INSERT THE VALUE THAT WE
        CHECK IF HAVE CURRENT SELECTED WIDGET HAVE OWN CORRECT VALUES

        EXEMPLE:
        ```python
        ft.Container()
        ```

        ATTRIBUTES:
        ```python
        bgcolor, width, height ....
        ```

        EXEMPLE content:
        ```python
        ft.Text()
        ```

        ATTRIBUTES:
        ```python
        color, size, value ....
        ```
        """
        #: TAB 2

        if column_tab == "2_0":
            tmp_value = self.check_number_column(tab_control=tab_control)

        if column_tab == "2_1":
            tmp_value = self.check_number_column(tab_control=tab_control)

        if column_tab == "2_2":
            tmp_value = self.check_number_column(tab_control=tab_control)

        if column_tab == "2_3":
            tmp_value = self.check_number_column(tab_control=tab_control)

        for _ in tmp_value:
            _.controls[0].visible = True
            _.widget = widget_name
            _.update()

    def insert_data_in_box_container_content(
        self,
        column_tab: str = "",
        tab_control: list = list(),
        widget_name: object = object(),
    ):
        """
        - WALK ALL TABS TO INSERT THE VALUE THAT WE
        CHECK IF HAVE CURRENT SELECTED WIDGET HAVE OWN CORRECT VALUES

        EXEMPLE:
        ```python
        ft.Container()
        ```

        ATTRIBUTES:
        ```python
        bgcolor, width, height ....
        ```

        EXEMPLE content:
        ```python
        ft.Text()
        ```

        ATTRIBUTES:
        ```python
        color, size, value ....
        """

        #: TAB 3

        if column_tab == "3_0":
            tmp_value = self.check_number_column(tab_control=tab_control)

        if column_tab == "3_1":
            tmp_value = self.check_number_column(tab_control=tab_control)

        if column_tab == "3_2":
            tmp_value = self.check_number_column(tab_control=tab_control)

        if column_tab == "3_3":
            tmp_value = self.check_number_column(tab_control=tab_control)

        if column_tab == "3_4":
            tmp_value = self.check_number_column(tab_control=tab_control)

        if column_tab == "3_5":
            tmp_value = self.check_number_column(tab_control=tab_control)

        if column_tab == "3_6":
            tmp_value = self.check_number_column(tab_control=tab_control)

        if column_tab == "3_7":
            tmp_value = self.check_number_column(tab_control=tab_control)

        for _ in tmp_value:

            if _.id_name_widget_dict in self.list_wdiget_content_attribute:
                _.visible = True
                _.widget = widget_name
                _.update()  # :<==== update exactly widget <<<

            else:
                _.visible = False
                _.widget = widget_name
                _.update()  # :<==== update exactly widget <<<

    def action_windows(self, action):
        self.phone_widget_container.width, self.phone_widget_container.height = (
            self.phone_widget_container.height,
            self.phone_widget_container.width,
        )
        self.phone_widget_container.update()

    def clear_all_phone_widgets(self):
        main_phone = self.page.session.get("SELECTED_SCREEN")
        # self.control_phone_page = main_phone.content.content.content.content.controls

        self.controls_column = (
            main_phone.content.content.content.content.content.content.content.controls
        )
        self.control_phone_page = self.controls_column

        for _ in self.control_phone_page:
            del self.page._index[_.uid]

        self.controls_column.clear()
        # APPLYE ALL CHANGES
        main_phone.update()

    def delete_widget(self):
        """
        DELETE SELECTED WIDGET

        1. remove from controls
        2. remove from index page
        3. set SELECTED_CONTAINER None by defould
        4. update to apply all
        """
        self.select_container = self.page.session.get("SELECTED_CONTAINER")

        if not self.select_container == None:
            # NECESSARY REMOVE PROM PREVIOUS PARAEN PARENT
            cover_widget = self.page.session.get("cover_widget")

            if cover_widget._get_control_name() == "dragtarget":
                # print(cover_widget.content.content.content)
                cover_widget = cover_widget.parent

                for _ in cover_widget.controls:
                    # print(_)
                    if _.uid == self.select_container.parent.parent.uid:
                        cover_widget.controls.remove(
                            self.select_container.parent.parent
                        )

            else:
                # print(cover_widget._get_control_name(),"<<<<< ======================")
                if cover_widget._get_control_name() == "container":
                    print(self.page.session.get_keys())
                    self.show_warning = self.page.session.get("on_dev")
                    self.show_warning("You may not erase main dragg column..")
                    return

                cover_widget.controls.remove(self.select_container.parent)

            # ERASE FROM INDEX PAGE
            del self.page._index[self.select_container.parent.uid]

            # SET SELECTED_CONTAINER IN NONE TO AVOID DOUBLE REMOVE AND NO RETURN ERROR
            self.page.session.set("SELECTED_CONTAINER", None)

            # UPDATE MAIN PAGE TO APPLY ALL
            self.page.update()


if __name__ == "__main__":

    def main(page: ft.Page):
        page.scroll = "HIDDEN"  # AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK  # ft.ThemeMode.LIGHT
        page.window_bgcolor = ft.colors.RED_100
        page.window_left = 20
        page.window_top = 20
        page.window_height = 400
        page.window_width = 600
        page.padding = 0
        page.spacing = 0
        page.expand = True
        Lite_MenuUpContainer = LiteMenuUpContainer()
        page.add(Lite_MenuUpContainer)
        page.update()

    ft.app(
        target=main,
    )
