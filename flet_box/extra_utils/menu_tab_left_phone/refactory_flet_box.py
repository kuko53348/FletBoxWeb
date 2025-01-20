import json
import re
import requests
import flet as ft

from ..external_library.async_requests import async_requests
from .widget_templates import widget_templates
from ..external_library.sqlite_db import sqlite_db

request_session = requests.Session()

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

class refactory_flet_box:
    """
    - ## Will returned a clean code of recusion widget.

    ```python
    code_returned = refactory_flet_box(page=page)
    code_returned.get_widget_attributes(widget= widget_name, screen_name='main_screens')
    ```
    ### refactory code
    ```python
    clean_code = code_returned.refactory_code(string_widget=widget)
    ```

    ### name of class widget
    ```python
    widget_name = code_returned.get_widget_name(widget_name=widget)
    ```

    ### get list of controls
    ```python
    list_controls = code_returned.get_list_controls(widget_name=widget_name, widget=widget)
    ```

    ### id calss widget
    ```python
    widget_id = code_returned.get_widget_id(widget_id=widget)
    ```

    ### get style coded
    ```python
    widget_style = code_returned.get_style_function(widget_id=widget_id.get('id'))
    ```

    ### get funtion coded
    ```python
    widget_function = code_returned.get_function_in_app(widget_id=widget_id.get('id'),string_widget=widget)
    ```

    - ## Will return current format

    ```python

    [control_type]   >>> {'parent_controls': 'column'}
    [controls_child] >>> {'child_controls': []}
    [control_style]  >>> {'alignment': 'center', 'horizontal_alignment': 'center', 'scroll': 'auto'}
    [control_id]     >>> {'id': '_2'}
    [control_style]  >>> **self.dict_style('_2'),
    [control_event]  >>> # on_click= lambda tmp_widget: event_2(data='_2'),
    ```

    """

    def __init__(self, page: object = None):
        self.page = page
        # STRING THAT CONTENT ALL MAIN SCREEN
        self.refactory_string: str = str()
        self.app_refactory_string: str = str()

        # LIST WITH CONTRLS WIDGET
        self.controls_widget: list = []
        self.all_controls_in_widget: list = []

        self.app_all_controls_in_widget: list = []
        self.app_controls_widget: list = []

        # SCREEN STYLE AND SCREEN EVENT
        self.all_events_widget: list = []
        self.all_events_id: list = []
        self.screen_styles: dict = dict()
        self.all_widget_in_row: list = []

        self.app_all_events_widget: list = []
        self.app_all_events_id: list = []
        self.app_screen_styles: dict = dict()
        self.app_all_widget_in_row: list = []

        self.code_to_refactory: dict = {
            "aspectratio": "aspect_ratio",
            "backgroundimage_src": "background_image_src",
            "blurradius": "blur_radius",
            "bordercolor": "border_color",
            "borderradius": "border_radius",
            "borderwidth": "border_width",
            "childaspect_ratio": "child_aspect_ratio",
            "colspacing": "col_spacing",
            "contentpadding": "content_padding",
            "countertext": "counter_text",
            "cursorheight": "cursor_height",
            "focusedborder_color": "focused_border_color",
            "hinttext": "hint_text",
            "horizontalalignment": "horizontal_alignment",
            "imagefit": "image_fit",
            "imageopacity": "image_opacity",
            "imagesrc": "image_src",
            "inkcolor": "ink_color",
            "maxextent": "max_extent",
            "maxlines": "max_lines",
            "minlines": "min_lines",
            "onclick": "on_click",
            "runscount": "runs_count",
            "runspacing": "run_spacing",
            "semanticslabel": "semantics_label",
            "spaceAround": "space_around",
            "spaceBetween": "space_between",
            "spaceEvenly": "space_evenly",
            "spreadradius": "spread_radius",
            "srcbase64": "src_base64",
            "suffixtext": "suffix_text",
            "textalign": "text_align",
            "textsize": "text_size",
            "urltarget": "url_target",
            "verticalalignment": "vertical_alignment",
            "centerspaceradius": "center_space_radius",
            "sectionsspace": "sections_space",
            "extensionset": "extension_set",
            "autoscroll": "auto_scroll",
            "focusedbordercolor": "focused_border_color",
            "backgroundimagesrc": "background_image_src",
            "dismissdirection": "dismiss_direction",
            "dismissthresholds": "dismiss_thresholds",

            "crossaxisalignment": "cross_axis_alignment",
            "maintainstate": "maintain_state",
            "collapsedtextcolor": "collapsed_text_color",
            "textcolor": "text_color",
        }

        # SEPARATE BY TYPE CONTENT AND CONTROLS
        # WILL DELIMITATE TO ADD NEW WIDGET OR NOT
        self.content_attributes: dict = {
            "container": "content",
            "dragtarget": "content",
            "dismissible": "content",
            "radiogroup": "content",

            "piechart": "sections",

            "row": "controls",
            "column": "controls",
            "stack": "controls",
            "gridview": "controls",
            "responsiverow": "controls",
            "listview": "controls",
        }

        # ONLY THIS TYPE CONTENT WILL HAVE FUNCTION IN APP
        # on_click= lambda tmp_widget: event_3634(data='_3634'),
        self.function_attributes: dict = {
            # "container": True,
            "dragtarget": True,
        }

        self.del_attributes: list = [
            'n',
            'tooltip',
            'onclick',
            'style',
            'round'
        ]

        self.widget_reference: dict = {
            "container": "Container",
            "dragtarget": "DragTarget",
            "row": "Row",
            "column": "Column",
            "stack": "Stack",
            "gridview": "GridView",
            "responsiverow": "ResponsiveRow",
            'listview': 'ListView',

            'space': 'Space',
            'divider': 'Divider',
            'verticaldivider': 'VerticalDivider',
            'image': 'Image',
            'circleavatar': 'CircleAvatar',
            'icon': 'Icon',

            'text': 'Text',
            'textfield': 'TextField',

            'elevatedbutton': 'ElevatedButton',
            'textbutton': 'TextButton',
            'iconbutton': 'IconButton',
            'filledbutton': 'FilledButton',
            'filledtonalbutton': 'FilledTonalButton',
            'outlinedbutton': 'OutlinedButton',
            'chip': 'Chip',

            'checkbox': 'Checkbox',
            'cupertinocheckbox': 'CupertinoCheckbox',
            'cupertinoradio': 'CupertinoRadio',
            'radio': 'Radio',
            'cupertinoslider': 'CupertinoSlider',
            'switch': 'Switch',
            'badge': 'Badge',
            'radiogroup': 'RadioGroup',

            'datatable': 'DataTable',
            'dismissible': 'Dismissible',
            'expansionpanelist': 'ExpansionPanelList',
            'expansiontile': 'ExpansionTile',
            'placeholder': 'Placeholder',
            'webview': 'WebView',
            'progressring': 'ProgressRing',
            'progressbar': 'ProgressBar',
            'cupertinoactivityindicator': 'CupertinoActivityIndicator',
            'markdown': 'Markdown',
            'piechart': 'PieChart',
        }

        self.attributes: dict = dict()

    def refactory_code(self, string_widget: object = object()) -> str:
        """
        - TAKE OBJECT EXAMPLE CONTAINER AND TAKE IT ATTRIBUTES AND REFACTORY
        TO CLEAN CODE:

        ```python
        >>> FROM: 'borderradius':  '{"bl":30,"br":30,"tl":30,"tr":30}'
        >>> TO:   'border_radius': '{"bl":30,"br":30,"tl":30,"tr":30}'
        ```
        """
        self.attributes= {}
        string_widget.copy_attrs(dest=self.attributes)

        # DELETING ATTRIBUTES EXEMPLE 'n','tooltip'
        for _ in self.del_attributes:
            if self.attributes.get(_, False):
                del self.attributes[_]

        for _ in self.code_to_refactory:
            if self.attributes.get(_):
                self.attributes[self.code_to_refactory[_]] = self.attributes.pop(_)

        # WILL RETURNED CLEAN CODE
        return self.attributes

    def get_widget_name(self, widget_name: object = object()) -> dict:
        """
        - Gets the widget name.

        ```python
        widget_name = code_returned.get_widget_name(widget_name=widget)

        :returns:   {'controls': 'column'}
        ```
        """
        value: str = ""
        self.widget_name: str = widget_name._get_control_name()
        self.check_data = self.content_attributes.get(self.widget_name, "No content | No controls")

        if self.check_data == "No content | No controls":
            value = self.widget_name

        elif self.check_data == "controls":
            value = self.widget_name

        elif self.check_data == "content":
            # print(self.check_data,"<<<<<")
            value = self.widget_name

        return value

    def get_list_controls(self, widget_name: dict = dict(), widget: object = object()) -> dict:
        """
        - Gets the list controls.

        ```python
        list_controls = code_returned.get_list_controls(widget_name=widget_name, widget=widget)

        :returns:   The list controls.
        ```
        """
        is_content = self.content_attributes.get(str(widget_name), None)
        print('[+]',is_content, widget_name)

        if is_content == 'content':
            return {'content': widget.uid}

        elif is_content == 'controls':
            return {'controls': [_.uid for _ in widget.controls]}

        else:
            # if not have content will return other content
            return {'content': widget.uid}

        # print(is_content)

    def get_widget_id(self, widget_id: object = object()) -> str:
        """
        - Gets the widget identifier ID

        ```python
        widget_id = code_returned.get_widget_id(widget_id=widget)

        :returns:   The widget identifier {'id': '_2'}
        ```
        """

        return widget_id.__dict__['_Control__uid']

    def get_style_function(self, widget_id: str = str()) -> str:
        """
        - Will return the style function ID.

        ```python
        widget_style = code_returned.get_style_function(widget_id=widget_id.get('id'))

        :returns:   >>> **self.dict_style('_125'),
        ```
        """
        return f"**self.dict_style('{widget_id}'),"

    def get_function_in_app(self, widget_id: str = str(), string_widget: object = object()) -> str:
        """
        - Gets the function in application.

        ```python
        widget_function = code_returned.get_function_in_app(widget_id=widget_id.get('id'),string_widget=widget)

        :returns:   >>> on_click= lambda tmp_widget: event_3634(data='_3634'),
        ```
        """
        # print(string_widget._get_control_name())

        # IF _GET_CONTROL_NAME IN function_attributes DICT WILL HAVE ON_CLICK
        self.check_data = self.function_attributes.get(
            string_widget._get_control_name(), False)

        # if is container will have on_click
        if self.check_data:
            # return f"on_click= lambda dragg_item: self.dragg_event(selected_widget=dragg_item),"
            return widget_templates.get('event_dragg_target')

        else:
            return f"# on_click= lambda btn_event: event{widget_id}(data=\'{widget_id}\'),"

    def get_draggable_app(self, widget_name: dict = dict())-> dict:
        """
        Gets the draggable application.

        :param      widget_name:  The widget name
        :returns:   The draggable application.
        :rtype:     dict
        """
        is_container = widget_name.get('parent_content', False)

        if is_container:
            return {"dragg_editor": widget_templates.get('frame_content')}

        return {"dragg_editor": None}

    def create_framework(self,
                         tab: str = '\t',
                         widget_id: dict = dict(),
                         clean_code: dict = dict(),
                         widget_name: dict = dict(),
                         dragg_controls: dict = dict(),
                         )-> dict:

        self.tab = tab
        self.dragg_id = widget_id.get('dragg_id')
        self.container_id = widget_id.get('container_id')
        self.content_id = widget_id.get('content_id')

        self.check_controls = self.content_attributes.get(widget_name.get('content_name'))
        self.change_content = self.widget_reference.get(widget_name.get('content_name'))

        if self.change_content == None:
            """
            if widget not in dict return
            """
            self.open_dialog = self.page.session.get('on_dev')
            self.open_dialog(name_seccion='dev most add widget:',body_string=f"Sorry is not aviable yet it's neccesary be added in [ {widget_name.get('content_name')} ]\n{widget_templates.get('widget_reference')}")
            return

        if self.check_controls == 'controls':
            # SKELETON WIDGET WILL RETURN
            # EVENT , STYLE AND CLASS

            self.controls_widget = dragg_controls.get('content_controls').get('controls')

            for _ in self.controls_widget:
                if not f"{_}" in self.all_controls_in_widget:
                    self.all_controls_in_widget.append(_)

            self.skeleton = widget_templates.get('dragg_controls')
            self.skeleton = self.skeleton.replace('NUMBER_DRAGG', self.dragg_id.strip('_'))
            self.skeleton = self.skeleton.replace('CONTAINER_ID', self.container_id)
            self.skeleton = self.skeleton.replace('CONTEN_ID', self.content_id)
            self.skeleton = self.skeleton.replace('CHANGE_CONTENT_WIDGET', self.change_content)
            self.skeleton = self.skeleton.replace('CHANGE_CONTROLS', str(self.controls_widget))
            self.skeleton = self.skeleton.replace('[+]', self.tab)

            self.app_skeleton = widget_templates.get('app_controls')
            self.app_skeleton = self.app_skeleton.replace('NUMBER_DRAGG', self.dragg_id.strip('_'))
            self.app_skeleton = self.app_skeleton.replace('CONTAINER_ID', self.container_id)
            self.app_skeleton = self.app_skeleton.replace('CONTEN_ID', self.content_id)
            self.app_skeleton = self.app_skeleton.replace('CHANGE_CONTENT_WIDGET', self.change_content)
            self.app_skeleton = self.app_skeleton.replace('CHANGE_CONTROLS', str(self.controls_widget))
            self.app_skeleton = self.app_skeleton.replace('[+]', self.tab)

            self.refactory_string = self.skeleton
            self.app_refactory_string = self.app_skeleton

            self.screen_styles[f"Container{self.container_id}"] = clean_code.get('clean_container')
            self.screen_styles[f"{self.change_content}{self.content_id}"] = clean_code.get('clean_content')

            self.event_btn = widget_templates.get("screen_event")
            self.event_btn = self.event_btn.replace('CONTEN_ID', f"event{self.content_id}")

            self.all_events_widget.append(self.event_btn)
            self.all_events_id.append(self.content_id)
            # RUN IN PRODUCTION
            # print(self.event_btn)

        else:
            # SKELETON WIDGET WILL RETURN
            # EVENT , STYLE AND CLASS
            #
            self.skeleton = widget_templates.get('dragg_content')
            self.skeleton = self.skeleton.replace('NUMBER_DRAGG', self.dragg_id.strip('_'))
            self.skeleton = self.skeleton.replace('CONTAINER_ID', self.container_id)
            self.skeleton = self.skeleton.replace('CONTEN_ID', self.content_id)
            self.skeleton = self.skeleton.replace('CHANGE_CONTENT_WIDGET', self.change_content)
            self.skeleton = self.skeleton.replace('[+]', self.tab)

            self.app_skeleton = widget_templates.get('app_content')
            self.app_skeleton = self.app_skeleton.replace('NUMBER_DRAGG', self.dragg_id.strip('_'))
            self.app_skeleton = self.app_skeleton.replace('CONTAINER_ID', self.container_id)
            self.app_skeleton = self.app_skeleton.replace('CONTEN_ID', self.content_id)
            self.app_skeleton = self.app_skeleton.replace('CHANGE_CONTENT_WIDGET', self.change_content)
            self.app_skeleton = self.app_skeleton.replace('[+]', self.tab)

            self.refactory_string = self.skeleton
            self.app_refactory_string = self.app_skeleton

            self.screen_styles[f"Container{self.container_id}"] = clean_code.get('clean_container')
            self.screen_styles[f"{self.change_content}{self.content_id}"] = clean_code.get('clean_content')

            self.event_btn = widget_templates.get("screen_event")
            self.event_btn = self.event_btn.replace('CONTEN_ID', f"event{self.content_id}")

            self.all_events_widget.append(self.event_btn)
            self.all_events_id.append(self.content_id)

            # RUN IN PRODUCTION
            # print(self.event_btn)

        return {
                'dragg_widget':self.refactory_string,
                'dragg_app_widget':self.app_refactory_string,
            }

    def return_code(self, widget: object = None, tab: int = 3) -> dict:
        """
        - Return clean code refactorized

        ```python
        self.refactorized = self.return_code(widget=widget, tab=tab)
        ```
        """

        dragg = widget
        container = dragg.content
        container_content = container.content

        # # WIDGET ID
        dragg_id = self.get_widget_id(widget_id=dragg)
        container_id = self.get_widget_id(widget_id=container)
        content_id = self.get_widget_id(widget_id=container_content)

        # # CLEAN CODE
        clean_dragg = self.refactory_code(string_widget=dragg)
        clean_conta = self.refactory_code(string_widget=container)
        clean_content = self.refactory_code(string_widget=container_content)

        # #  WIDGET NAME
        dragg_name = self.get_widget_name(widget_name=dragg)
        container_name = self.get_widget_name(widget_name=container)
        content_name = self.get_widget_name(widget_name=container_content)

        content_controls = self.get_list_controls(widget_name=content_name, widget=container_content)

        widget_data: dict = {

            dragg_id: {
                "widget_id": {"dragg_id": dragg_id, "container_id": container_id, "content_id": content_id},
                "clean_code": {"clean_dragg": clean_dragg, "clean_container": clean_conta, "clean_content": clean_content},
                "widget_name": {"dragg_name": dragg_name, "container_name": container_name, "content_name": content_name},
                "dragg_controls": {"content_controls": content_controls},
            }}

        self.tab = '    ' * tab

        # DONT TOUCH
        self.refactorized = self.create_framework(
            tab=self.tab,
            widget_id=widget_data.get(dragg_id).get('widget_id'),
            clean_code=widget_data.get(dragg_id).get('clean_code'),
            widget_name=widget_data.get(dragg_id).get('widget_name'),
            dragg_controls=widget_data.get(dragg_id).get('dragg_controls'),
        )

        # print(clean_conta)
        # print(widget_data.get(dragg_id).get('widget_id'))
        # print(widget_data.get(dragg_id).get('clean_code'))
        # print(widget_data.get(dragg_id).get('widget_name'))
        # print(widget_data.get(dragg_id).get('dragg_controls'))
        # print(self.page._index['_2245'])

        return self.refactorized

    def recursive_nested(self, tab: int = int()):
        """
        - Recursion neste function

        ```python
        self.recursive_nested(tab=tab)
        ```
        :return: Remplace all widgets_id by ft.Container(content=Widget_name)
        """
        # most be str
        # dragg_app_widget dragg_widget

        for _ in self.controls_widget:
            self.tmp = self.return_code(widget=self.page._index[_], tab=tab).get('dragg_widget')
            if _ in self.edit_data:
                # self.edit_data= self.edit_data.replace(_, 'self.tmp')
                self.edit_data = self.edit_data.replace(_, self.tmp)

        # IF SCAPE WIDGETS IN MIDDLE CALL AGAIN IN LIST
        for _ in self.all_controls_in_widget:
            self.tmp = self.return_code(widget=self.page._index[_], tab=tab+2).get('dragg_widget')
            if _ in self.edit_data:
                # print(self.tmp,'==========================')
                self.edit_data = self.edit_data.replace(_, self.tmp)


        # APP CONTENT
        for _tmp in self.controls_widget:
            self.app_tmp = self.return_code(widget=self.page._index[_tmp], tab=tab).get('dragg_app_widget')
            if _tmp in self.app_edit_data:
                # self.app_edit_data= self.app_edit_data.replace(_, 'self.app_tmp')
                self.app_edit_data = self.app_edit_data.replace(_tmp, self.app_tmp)

        # IF SCAPE WIDGETS IN MIDDLE CALL AGAIN IN LIST
        for _tmp in self.all_controls_in_widget:
            self.app_tmp = self.return_code(widget=self.page._index[_tmp], tab=tab+2).get('dragg_app_widget')
            if _tmp in self.app_edit_data:
                # print(self.app_tmp,'==========================')
                self.app_edit_data = self.app_edit_data.replace(_tmp, self.app_tmp)
        # print(self.all_controls_in_widget)

    def get_widget_attributes(self, widget: object = ""):
        """
        - Gets the widget attributes.

        ```python
        code_returned = refactory_flet_box(page=page)
        code_returned.get_widget_attributes(widget=widget1,screen_name='main_screens')
        ```

        """
        tab = 3

        # WILLRETURN A LIST WITH ALL WIDGET TO MAKE A NESTED RECURSION
        self.refactorized = self.return_code(widget=widget, tab=tab).get('dragg_widget')
        self.edit_data = self.refactorized

        self.app_refactorized = self.return_code(widget=widget, tab=tab).get('dragg_app_widget')
        self.app_edit_data = self.app_refactorized

        while "'_" in self.edit_data:
            tab += 3
            self.recursive_nested(tab=tab)
            # await asyncio.sleep(0.02)

        # while "'_" in self.app_edit_data:
        #     tab += 3
            # self.recursive_nested(tab=tab)


        self.edit_data = self.edit_data.replace("'],", ']').replace("['", "[").replace("', '", '')
        self.app_edit_data = self.app_edit_data.replace("'],", ']').replace("['", "[").replace("', '", '')

        self.all_widget_in_row.append(self.edit_data)
        self.app_all_widget_in_row.append(self.app_edit_data)


    def get_template_widget(self,name_app: str=str(), screen_name: str=str(), widgets_class: str=str()) -> str:
        """
        - Get Template from widget_templates

        ```python

        self.get_template_widget(name_app='screen_class',screen_name=screen_name, widgets_class=widgets_class)

        :return: ONLY TEMPLATE
        ```
        """
        tmp_template = widget_templates.get(name_app)
        tmp_template = tmp_template.replace('SCREEN_NAME', screen_name)
        tmp_template = tmp_template.replace('REPLACE_WIDGET', widgets_class)
        return tmp_template

    def write_files_in_project(self,
                               screen_name: str = str(),
                               data_to_write: str = str(),
                               ):

        with open(f"flet_box/extra_utils/phone_container/app_manager/views/{screen_name}.py", 'w') as f:
            f.write(data_to_write)

    def refactory_wring_attributes(self,
                            dict_string: dict=dict()
                            ) -> str:

        widgets_styles = json.dumps(dict_string, indent=4, skipkeys=True )
        widgets_styles = widgets_styles.replace('"{', '{').replace('}"', '}').replace('\\', '').replace(":", ": ").replace('"["', '["').replace('"]"', '"]')
        widgets_styles = widgets_styles.replace('},"', '},\n\t\t\t\t\t"').replace('}},', '}\n\t\t\t\t\t},').replace(',"', ', "')
        widgets_styles = widgets_styles.replace('"on_click"', '# "on_click"').replace('\t', '    ')
        widgets_styles = widgets_styles.replace('"[', '[').replace(']"', ']')
        widgets_styles = widgets_styles.replace('"true"', 'True').replace('true', 'True').replace('"false"', 'False').replace('false', 'False')
        widgets_styles = widgets_styles.replace('null', 'None')
        #
        return widgets_styles

    def save_all_data(  self,
                        save_project_module: bool=False,

                        column_tab_db: str = str(),
                        name_project_db: str = str(),
                        time_created_db: str = str(),

                        screen_name: str = str(),
                        one_file: bool = False,

                        container_attributes: dict = dict(),
                      ) -> None:
        """
        - Save all App data in file and send by request metod to FletBox Web API

        """

        widgets_events: str = str()
        widgets_class:  str = str()
        widgets_styles: str = str()

        app_widgets_events: str = str()
        app_widgets_class:  str = str()
        app_widgets_styles: str = str()

        # ALL WIDGETS DRAGGIN CLASS
        for widgets in self.all_widget_in_row:
            widgets_class+=widgets

        for tmp_widgets in self.app_all_widget_in_row:
            app_widgets_class+=tmp_widgets

        # ALL WIDGETS STYLES
        widgets_styles = self.refactory_wring_attributes(dict_string=self.screen_styles)

        # ONLY GET NUMBERS
        for _ in re.findall('"[0-9(.)]+"', widgets_styles):
            widgets_styles = widgets_styles.replace(_, _.strip('"'))


        # ALL WIDGETS EVENTS
        tmp_list = set(self.all_events_widget)

        for events in tmp_list:
            widgets_events += events

        self.dragg_template = self.get_template_widget(name_app='screen_class',screen_name=screen_name, widgets_class=widgets_class)
        self.app_dragg_template = self.get_template_widget(name_app='app_screen_class',screen_name=screen_name, widgets_class=app_widgets_class)

        # ========================================
        # print(self.dragg_template)
        # print(self.app_dragg_template)

        # print(widgets_styles)
        # print(widgets_events)
        # ========================================
        # print(">>>>>> END <<<<<<")

        # IF ONE FILE WILL BE SAVED IN DATABASE
        if one_file:
            self.container_attributes = self.refactory_code(string_widget=container_attributes.get('container'))
            self.effect_container_attributes = self.refactory_code(string_widget=container_attributes.get('effect_container'))
            self.column_attributes = self.refactory_code(string_widget=container_attributes.get('column_attributes'))

            self.container_widget = {
                    'main_container': {
                                    'image':self.container_attributes.get('image'),
                                    'gradient':self.container_attributes.get('gradient'),
                        },
                    'second_container': {
                                    'padding':self.effect_container_attributes.get('padding'),
                                    'blur':self.effect_container_attributes.get('blur'),
                                    'bgcolor':self.effect_container_attributes.get('bgcolor'),

                    },
                    'column_attributes': {
                                    'scroll':self.column_attributes.get('scroll'),
                                    'spacing':self.column_attributes.get('spacing'),
                                    'tight':self.column_attributes.get('tight'),
                                    'wrap':self.column_attributes.get('wrap'),
                                    'alignment':self.column_attributes.get('alignment'),
                                    'horizontal_alignment':self.column_attributes.get('horizontal_alignment'),
                    },

            }

            # DRAGG TEMPLATE
            # self.clean_code_container = self.refactory_wring_attributes(dict_string=self.container_widget)
            # self.dragg_template = self.dragg_template.replace('CONTAINER_STYLE',self.clean_code_container)

            # # print('================== onefile ====================')
            # self.dragg_template = self.dragg_template.replace("from .main_screen_styles", "# from .main_screen_styles")
            # self.dragg_template = self.dragg_template.replace("from .main_screen_events", "# from .main_screen_events")

            # self.dragg_template = self.dragg_template.replace('# styles','styles').replace('CHANGE_STYLE',widgets_styles)
            # self.dragg_template = self.dragg_template.replace('CONTAINER_STYLE',self.clean_code_container)

            self.dragg_template = self.clean_template_to_production(
                                        widget_to_modify=self.dragg_template,
                                        container_widget=self.container_widget,
                                        widgets_styles=widgets_styles,
                                    )

            self.app_dragg_template = self.clean_template_to_production(
                                        widget_to_modify=self.app_dragg_template,
                                        container_widget=self.container_widget,
                                        widgets_styles=widgets_styles,
                                    )
            # APP TEMPLATE
            # ========================================
            # print(self.dragg_template)
            # print(self.app_dragg_template)

            # print(widgets_styles)
            # print(widgets_events)
            # ========================================
            # WRITE IN DATABASE
            self.user_name  = self.page.session.get('user_name').get('user_name') if self.page.session.get('user_name') else 'user_demo'
            # print( self.user_name,"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


            if self.page.session.get('flet_box_api'):
                """
                Will save data in database
                """
                self.dragg_template = self.dragg_template.replace("'",'"')
                self.app_dragg_template = self.app_dragg_template.replace("'",'"')

                try:
                    data_returned = request_session.put(f'{self.page.session.get("api_server")}update_widgets',
                                                        data=json.dumps({
                                                            'user_name': self.user_name,
                                                            'dragg_widget' : self.dragg_template,
                                                            'app_widget' : self.app_dragg_template,

                                                        }))
                except Exception as e:
                    # kuko53348@gmail.com
                    on_developing(
                            self=self,
                            name_seccion='Connection Error',
                            body_string="Connection error between render.com and endpoint pythoneverywhere.com\nTry agan in flew seconds "
                        )

                    save_project_module = False
                    return False

                if save_project_module:
                    # print('testing save project')
                    try:
                        data_request: dict={
                            'user_name':self.user_name,
                            'project_tab':column_tab_db,
                            'name_project':name_project_db,
                            'ranking_app':'0',
                            'dragg_screen':self.dragg_template,
                            'app_screen':self.app_dragg_template,
                            'time_created':time_created_db
                        }

                        data_module_returned = request_session.post(f'{self.page.session.get("api_server")}save_module_widgets',
                                        data=json.dumps(data_request))
                    except Exception as e:
                        # kuko53348@gmail.com
                        on_developing(
                                self=self,
                                name_seccion='Connection Error',
                                body_string="Connection error between render.com and endpoint pythoneverywhere.com\nTry agan in flew seconds "
                            )

                        save_project_module = False
                        return False
            else:
                # WRITE DATA TO LOCAL DB BUT NOT WRITE IN PROJECT
                sqlite_obj = sqlite_db()
                data_returned = sqlite_obj.update_data(
                                        table_name='user_screen',
                                        change_data=('user_name', self.user_name),
                                        by_data=('main_screen', self.dragg_template)
                                )

                data_returned = sqlite_obj.update_data(
                                        table_name='user_screen',
                                        change_data=('user_name', self.user_name),
                                        by_data=('screen_one', self.app_dragg_template)
                                )
                # print(f'>>>> {self.user_name} {data_returned}')

                if save_project_module:
                    # UPDATE DATA REGISTER TABLE LOCAL AND MAKE MODULE PROJECT
                    sqlite_obj = sqlite_db()
                    user_name_have_same_project = sqlite_obj.find_name(
                                    table_name=column_tab_db,
                                    column='user_name',
                                    name=self.user_name,
                                    match=['name_project', name_project_db]
                    )

                    if not user_name_have_same_project == False:
                        # UPDATE IF EXIT PROJECT LOCAL MAKE MODULE PROJECT
                        self.save_in_database(
                                            column_name='dragg_screen',
                                            column_tab_db=column_tab_db,
                                            name_project_db=name_project_db,
                                            template_app=self.dragg_template
                            )
                        self.save_in_database(
                                            column_name='app_screen',
                                            column_tab_db=column_tab_db,
                                            name_project_db=name_project_db,
                                            template_app=self.app_dragg_template
                            )
                    else:
                        # WITE NEW PROJECT IF NOT EXIT IN DATABASE
                        sqlite_obj = sqlite_db(path_db=PATH_DB)
                        sqlite_obj.write_data(
                            table_name=column_tab_db,
                            column=(
                                self.user_name,
                                column_tab_db,
                                name_project_db,
                                '0',
                                'None',
                                'None',
                                time_created_db
                            )
                        )

                        # sqlite_obj = sqlite_db(path_db=PATH_DB)
                        # sqlite_obj.update_data(
                        #     table_name=column_tab_db,
                        #     change_data=('dragg_screen', 'None'),
                        #     by_data=('dragg_screen', self.dragg_template)
                        # )
                        self.save_in_database(
                                            path_db=PATH_DB,
                                            column_name='dragg_screen',
                                            column_tab_db=column_tab_db,
                                            name_project_db=name_project_db,
                                            template_app=self.dragg_template
                            )
                        self.save_in_database(
                                            path_db=PATH_DB,
                                            column_name='app_screen',
                                            column_tab_db=column_tab_db,
                                            name_project_db=name_project_db,
                                            template_app=self.app_dragg_template
                            )

            # SAVE DATA TO CONTROL ERRORS
            self.write_files_in_project(
                                    screen_name=f"{screen_name}",
                                    data_to_write=self.dragg_template,
            )
            self.write_files_in_project(
                                    screen_name=f"app_{screen_name}",
                                    data_to_write=self.app_dragg_template,
            )

        else:

            self.container_attributes = self.refactory_code(string_widget=container_attributes.get('container'))
            self.effect_container_attributes = self.refactory_code(string_widget=container_attributes.get('effect_container'))
            self.column_attributes = self.refactory_code(string_widget=container_attributes.get('column_attributes'))

            self.container_widget = {
                    'main_container':{
                                    'image':self.container_attributes.get('image'),
                                    'gradient':self.container_attributes.get('gradient'),
                        },
                    'second_container':{
                                    'padding':self.effect_container_attributes.get('padding'),
                                    'blur':self.effect_container_attributes.get('blur'),
                                    'bgcolor':self.effect_container_attributes.get('bgcolor'),

                    },
                    'column_attributes':{
                                    'scroll':self.column_attributes.get('scroll'),
                                    'spacing':self.column_attributes.get('spacing'),
                                    'tight':self.column_attributes.get('tight'),
                                    'wrap':self.column_attributes.get('wrap'),
                                    'alignment':self.column_attributes.get('alignment'),
                                    'horizontal_alignment':self.column_attributes.get('horizontal_alignment'),
                    },

            }
            self.clean_code_container = self.refactory_wring_attributes(dict_string=self.container_widget)
            self.dragg_template = self.dragg_template.replace('CONTAINER_STYLE',self.clean_code_container)

            # WRITE CLASS WIDGET
            self.write_files_in_project(
                                    screen_name=f"{screen_name}",
                                    data_to_write=self.dragg_template,
                )
            # WRITE STYLE WIDGET
            self.write_files_in_project(
                                    screen_name=f"{screen_name}_styles",
                                    data_to_write=f"styles = {widgets_styles}\n",
                )
            # WRITE EVENT WIDGET
            self.write_files_in_project(
                                    screen_name=f"{screen_name}_events",
                                    data_to_write=f"{widgets_events}\n",
                )

    def clean_template_to_production(self,
                            widget_to_modify: str=object(),
                            container_widget: str=str(),
                            widgets_styles: str=str(),
        ) -> str:
        """
        Make a clean template to save all in database

        Args:
            widgets_styles (_type_): _description_
        """
        clean_code_container = self.refactory_wring_attributes(dict_string=container_widget)

        clean_template = widget_to_modify
        clean_template = clean_template.replace('CONTAINER_STYLE',clean_code_container)

        clean_template = clean_template.replace("from .main_screen_styles", "# from .main_screen_styles")
        clean_template = clean_template.replace("from .main_screen_events", "# from .main_screen_events")

        clean_template = clean_template.replace('# styles','styles').replace('CHANGE_STYLE',widgets_styles)
        clean_template = clean_template.replace('CONTAINER_STYLE',clean_code_container)

        return clean_template

    def save_in_database(self, path_db=False, column_tab_db: str=str(), name_project_db: str=str(),column_name: str=str(),template_app: str=str()):
        if path_db:
            sqlite_obj = sqlite_db(path_db=path_db)
        else:
            sqlite_obj = sqlite_db()

        sqlite_obj.update_data(
                            table_name=column_tab_db,
                            change_data=('name_project', name_project_db),
                            by_data=(column_name, template_app)
                        )