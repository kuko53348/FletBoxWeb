
#: MAIN WIDGET SCREEN CLASS
import flet as ft

# from .main_screen_styles import styles
# from .main_screen_events import *

#: STYLE TO MAIN SCREEN WIDGET
phone_style_widget: dict = {
    "main_container":  {
        "image":  {"src": "image107.jpeg", "fit": "cover"},
        "gradient":  None
    },
    "second_container":  {
        "padding":  None,
        "blur":  {"sigma_x": 8, "sigma_y": 8, "tile_mode": "mirror"},
        "bgcolor":  "transparent"
    },
    "column_attributes":  {
        "scroll":  None,
        "spacing":  None,
        "tight":  None,
        "wrap":  None,
        "alignment":  "spaceBetween",
        "horizontal_alignment":  "center"
    }
}

#: STYLES IN SCREEN_STYLE
styles = {
    "Container_4008":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "ink_color":  "cyan"
    },
    "Row_4009":  {
        "alignment":  "spaceBetween"
    },
    "Container_4071":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "ink_color":  "red"
    },
    "Icon_4072":  {
        "name":  "arrow_drop_down_rounded"
    },
    "Container_4074":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "ink_color":  "red"
    },
    "Text_4075":  {
        "size":  22.0,
        "value":  "Play Now",
        "weight":  "bold"
    },
    "Container_4077":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "ink_color":  "red"
    },
    "Icon_4078":  {
        "name":  "more_vert_rounded"
    },
    "Container_4011":  {
        "alignment":  {"x": 0, "y": 1},
        "bgcolor":  "black54",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "height":  200,
        "image":  {"src": "image107.jpeg", "fit": "cover"},
        "ink":  True,
        "padding":  {"l": 18, "t": 18, "r": 18, "b": 18},
        "width":  200,
        "border_radius":  {"bl": 103.0, "br": 103.0, "tl": 103.0, "tr": 103.0},
        "ink_color":  "yellow"
    },
    "Column_4012":  {
        "alignment":  "end",
        "scroll":  "ALWAYS",
        "horizontal_alignment":  "end"
    },
    "Container_4017":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "ink_color":  "yellow"
    },
    "Column_4018":  {
        "scroll":  "ALWAYS",
        "horizontal_alignment":  "center"
    },
    "Container_4020":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "ink_color":  "red"
    },
    "Row_4085":  {
        "alignment":  "spaceBetween",
        "height":  "",
        "width":  210,
        "vertical_alignment":  "center"
    },
    "Container_4023":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "ink_color":  "red"
    },
    "Text_4024":  {
        "size":  16.0,
        "value":  "The Best Moment of the live",
        "weight":  "bold"
    },
    "Container_4093":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "ink_color":  "red"
    },
    "Text_4094":  {
        "size":  10,
        "value":  "Unknow Artist",
        "weight":  "bold"
    },
    "Container_4087":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "ink_color":  "red"
    },
    "Text_4088":  {
        "size":  10,
        "value":  0.0,
        "weight":  "bold"
    },
    "Container_4090":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "ink_color":  "red"
    },
    "Text_4091":  {
        "size":  10,
        "value":  3.20,
        "weight":  "bold"
    },
    "Container_4026":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "black54",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "height":  "",
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "width":  180,
        "border_radius":  {"bl": 103.0, "br": 103.0, "tl": 103.0, "tr": 103.0},
        "ink_color":  "cyan"
    },
    "Row_4027":  {
        "alignment":  "center"
    },
    "Container_4029":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "ink_color":  "red"
    },
    "Icon_4030":  {
        "name":  "add_rounded"
    },
    "Container_4032":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "ink_color":  "red"
    },
    "Icon_4033":  {
        "color":  "errorcontainer",
        "name":  "favorite"
    },
    "Container_4035":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "ink_color":  "red"
    },
    "Icon_4036":  {
        "name":  "playlist_add_circle_rounded"
    },
    "Container_4038":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "ink_color":  "cyan"
    },
    "Row_4039":  {
        "alignment":  "spaceBetween",
        "vertical_alignment":  "center"
    },
    "Container_4041":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "ink_color":  "red"
    },
    "Icon_4042":  {
        "name":  "repeat_rounded"
    },
    "Container_4044":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "ink_color":  "red"
    },
    "Icon_4045":  {
        "name":  "skip_previous_rounded"
    },
    "Container_4047":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "onerror",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "border_radius":  {"bl": 61.0, "br": 61.0, "tl": 61.0, "tr": 61.0},
        "ink_color":  "red"
    },
    "Icon_4048":  {
        "name":  "play_arrow_rounded"
    },
    "Container_4050":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "ink_color":  "red"
    },
    "Icon_4051":  {
        "name":  "skip_next_rounded"
    },
    "Container_4053":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "ink_color":  "red"
    },
    "Icon_4054":  {
        "name":  "shuffle_rounded"
    },
    "Container_4056":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "black54",
        "border":  {"l": {"w": 0, "c": "transparent", "sa": None},
                    "t": {"w": 0, "c": "transparent", "sa": None},
                    "r": {"w": 0, "c": "transparent", "sa": None},
                    "b": {"w": 0, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "border_radius":  {"bl": 156.0, "br": 156.0, "tl": 156.0, "tr": 156.0},
        "ink_color":  "cyan"
    },
    "Row_4057":  {},
    "Container_4062":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "ink_color":  "red"
    },
    "Icon_4063":  {
        "name":  "volume_down_rounded"
    },
    "Container_4065":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 0, "c": "transparent", "sa": None},
                    "t": {"w": 0, "c": "transparent", "sa": None},
                    "r": {"w": 0, "c": "transparent", "sa": None},
                    "b": {"w": 0, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "ink_color":  "red"
    },
    "CupertinoSlider_4103":  {
        "height":  28,
        "max":  100
    },
    "Container_4068":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "ink_color":  "red"
    },
    "Icon_4069":  {
        "name":  "volume_up_rounded"
    },
    "Container_4059":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 2, "c": "transparent", "sa": None},
                    "t": {"w": 2, "c": "transparent", "sa": None},
                    "r": {"w": 2, "c": "transparent", "sa": None},
                    "b": {"w": 2, "c": "transparent", "sa": None}
                    },
        "height":  "",
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "width":  120,
        "ink_color":  "red"
    },
    "Divider_4060":  {}
}


class main_screen(ft.DragTarget):
    #: NECCESARY HAVE INSTANCE OF ACTUALLY PAGE
    # main_page: dict = dict()
    def __init__(self, page: object = None, main_page: bool= False):
        super().__init__(content=None)
        self.group="GroupDragg"

        # HEIGHT MAIN SCREEN
        self.main_page = main_page

        # ERASE IN PRODUCTION
        self.drag_width = 320

        #: NECCESARY HAVE INSTANCE OF ACTUALLY PAGE
        self.page = page

        #: ERASE IN PRODUCTION OR COMMENT THIS 2 LINES
        self.expand = True
        self.border_radius=ft.border_radius.all(32)

    def build(self,):
        #: DRAGG_CONTROLS
        list_controls: list = [
            
            #: DRAG-BOX-CONTROLS [ID: 4007]
            self.draggin_framework(
                content=ft.Container(
                    **self.dict_style("Container_4008"),
                    on_click=lambda dragg_item: self.dragg_event(
                                     selected_widget=dragg_item ),

                    content=ft.Row(
                        **self.dict_style("Row_4009"),
                        controls=[
                        #: DRAG-BOX-CONTENT [ID: 4070]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4071"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.Icon(
                                    **self.dict_style("Icon_4072"),
                                    # on_click= lambda tmp_widget: event_4072(
                                    #        payload="Icon_4072",
                                    #        page= self.page ),
                                ),
                            ),),
                        #: DRAG-BOX-CONTENT [ID: 4073]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4074"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.Text(
                                    **self.dict_style("Text_4075"),
                                    # on_click= lambda tmp_widget: event_4075(
                                    #        payload="Text_4075",
                                    #        page= self.page ),
                                ),
                            ),),
                        #: DRAG-BOX-CONTENT [ID: 4076]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4077"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.Icon(
                                    **self.dict_style("Icon_4078"),
                                    # on_click= lambda tmp_widget: event_4078(
                                    #        payload="Icon_4078",
                                    #        page= self.page ),
                                ),
                            ),),]
                    ),
                ),),
            #: DRAG-BOX-CONTROLS [ID: 4010]
            self.draggin_framework(
                content=ft.Container(
                    **self.dict_style("Container_4011"),
                    on_click=lambda dragg_item: self.dragg_event(
                                     selected_widget=dragg_item ),

                    content=ft.Column(
                        **self.dict_style("Column_4012"),
                        controls=[],
                    ),
                ),),
            #: DRAG-BOX-CONTROLS [ID: 4016]
            self.draggin_framework(
                content=ft.Container(
                    **self.dict_style("Container_4017"),
                    on_click=lambda dragg_item: self.dragg_event(
                                     selected_widget=dragg_item ),

                    content=ft.Column(
                        **self.dict_style("Column_4018"),
                        controls=[
                        #: DRAG-BOX-CONTROLS [ID: 4019]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4020"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item ),

                                content=ft.Row(
                                    **self.dict_style("Row_4085"),
                                    controls=[
                                #: DRAG-BOX-CONTENT [ID: 4086]
                                self.draggin_framework(
                                    content=ft.Container(
                                        **self.dict_style("Container_4087"),
                                        on_click=lambda dragg_item: self.dragg_event(
                                                         selected_widget=dragg_item,),

                                        content=ft.Text(
                                            **self.dict_style("Text_4088"),
                                            # on_click= lambda tmp_widget: event_4088(
                                            #        payload="Text_4088",
                                            #        page= self.page ),
                                        ),
                                    ),),
                                #: DRAG-BOX-CONTENT [ID: 4089]
                                self.draggin_framework(
                                    content=ft.Container(
                                        **self.dict_style("Container_4090"),
                                        on_click=lambda dragg_item: self.dragg_event(
                                                         selected_widget=dragg_item,),

                                        content=ft.Text(
                                            **self.dict_style("Text_4091"),
                                            # on_click= lambda tmp_widget: event_4091(
                                            #        payload="Text_4091",
                                            #        page= self.page ),
                                        ),
                                    ),),]
                                ),
                            ),),
                        #: DRAG-BOX-CONTENT [ID: 4022]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4023"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.Text(
                                    **self.dict_style("Text_4024"),
                                    # on_click= lambda tmp_widget: event_4024(
                                    #        payload="Text_4024",
                                    #        page= self.page ),
                                ),
                            ),),
                        #: DRAG-BOX-CONTENT [ID: 4092]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4093"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.Text(
                                    **self.dict_style("Text_4094"),
                                    # on_click= lambda tmp_widget: event_4094(
                                    #        payload="Text_4094",
                                    #        page= self.page ),
                                ),
                            ),),]
                    ),
                ),),
            #: DRAG-BOX-CONTROLS [ID: 4025]
            self.draggin_framework(
                content=ft.Container(
                    **self.dict_style("Container_4026"),
                    on_click=lambda dragg_item: self.dragg_event(
                                     selected_widget=dragg_item ),

                    content=ft.Row(
                        **self.dict_style("Row_4027"),
                        controls=[
                        #: DRAG-BOX-CONTENT [ID: 4028]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4029"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.Icon(
                                    **self.dict_style("Icon_4030"),
                                    # on_click= lambda tmp_widget: event_4030(
                                    #        payload="Icon_4030",
                                    #        page= self.page ),
                                ),
                            ),),
                        #: DRAG-BOX-CONTENT [ID: 4031]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4032"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.Icon(
                                    **self.dict_style("Icon_4033"),
                                    # on_click= lambda tmp_widget: event_4033(
                                    #        payload="Icon_4033",
                                    #        page= self.page ),
                                ),
                            ),),
                        #: DRAG-BOX-CONTENT [ID: 4034]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4035"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.Icon(
                                    **self.dict_style("Icon_4036"),
                                    # on_click= lambda tmp_widget: event_4036(
                                    #        payload="Icon_4036",
                                    #        page= self.page ),
                                ),
                            ),),]
                    ),
                ),),
            #: DRAG-BOX-CONTROLS [ID: 4037]
            self.draggin_framework(
                content=ft.Container(
                    **self.dict_style("Container_4038"),
                    on_click=lambda dragg_item: self.dragg_event(
                                     selected_widget=dragg_item ),

                    content=ft.Row(
                        **self.dict_style("Row_4039"),
                        controls=[
                        #: DRAG-BOX-CONTENT [ID: 4040]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4041"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.Icon(
                                    **self.dict_style("Icon_4042"),
                                    # on_click= lambda tmp_widget: event_4042(
                                    #        payload="Icon_4042",
                                    #        page= self.page ),
                                ),
                            ),),
                        #: DRAG-BOX-CONTENT [ID: 4043]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4044"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.Icon(
                                    **self.dict_style("Icon_4045"),
                                    # on_click= lambda tmp_widget: event_4045(
                                    #        payload="Icon_4045",
                                    #        page= self.page ),
                                ),
                            ),),
                        #: DRAG-BOX-CONTENT [ID: 4046]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4047"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.Icon(
                                    **self.dict_style("Icon_4048"),
                                    # on_click= lambda tmp_widget: event_4048(
                                    #        payload="Icon_4048",
                                    #        page= self.page ),
                                ),
                            ),),
                        #: DRAG-BOX-CONTENT [ID: 4049]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4050"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.Icon(
                                    **self.dict_style("Icon_4051"),
                                    # on_click= lambda tmp_widget: event_4051(
                                    #        payload="Icon_4051",
                                    #        page= self.page ),
                                ),
                            ),),
                        #: DRAG-BOX-CONTENT [ID: 4052]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4053"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.Icon(
                                    **self.dict_style("Icon_4054"),
                                    # on_click= lambda tmp_widget: event_4054(
                                    #        payload="Icon_4054",
                                    #        page= self.page ),
                                ),
                            ),),]
                    ),
                ),),
            #: DRAG-BOX-CONTROLS [ID: 4055]
            self.draggin_framework(
                content=ft.Container(
                    **self.dict_style("Container_4056"),
                    on_click=lambda dragg_item: self.dragg_event(
                                     selected_widget=dragg_item ),

                    content=ft.Row(
                        **self.dict_style("Row_4057"),
                        controls=[
                        #: DRAG-BOX-CONTENT [ID: 4061]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4062"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.Icon(
                                    **self.dict_style("Icon_4063"),
                                    # on_click= lambda tmp_widget: event_4063(
                                    #        payload="Icon_4063",
                                    #        page= self.page ),
                                ),
                            ),),
                        #: DRAG-BOX-CONTENT [ID: 4064]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4065"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.CupertinoSlider(
                                    **self.dict_style("CupertinoSlider_4103"),
                                    # on_click= lambda tmp_widget: event_4103(
                                    #        payload="CupertinoSlider_4103",
                                    #        page= self.page ),
                                ),
                            ),),
                        #: DRAG-BOX-CONTENT [ID: 4067]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_4068"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.Icon(
                                    **self.dict_style("Icon_4069"),
                                    # on_click= lambda tmp_widget: event_4069(
                                    #        payload="Icon_4069",
                                    #        page= self.page ),
                                ),
                            ),),]
                    ),
                ),),
            #: DRAG-BOX-CONTENT [ID: 4058]
            self.draggin_framework(
                content=ft.Container(
                    **self.dict_style("Container_4059"),
                    on_click=lambda dragg_item: self.dragg_event(
                                     selected_widget=dragg_item,),

                    content=ft.Divider(
                        **self.dict_style("Divider_4060"),
                        # on_click= lambda tmp_widget: event_4060(
                        #        payload="Divider_4060",
                        #        page= self.page ),
                    ),
                ),),
        ]

        #: DRAGGIN CONTENT WIDGETS
        self.content = ft.Container(
            height=self.page.window.height if self.main_page else None,
            width=self.drag_width,
            **self.main_screen_style(code="main_container"),
            content=ft.Container(
                **self.main_screen_style(code="second_container"),
                content=self.draggin_framework(
                    content=ft.Container(
                        content=ft.Column(
                            **self.main_screen_style(code="column_attributes"),
                            controls=list_controls
                        ),
                        # on_click=lambda dragg_item: self.dragg_event(
                        #     selected_widget=dragg_item,),
                    ),
                ),)
        )
        self.on_will_accept    = lambda dragg_item : self.dragg_on_will_accept(DragTargetEvent=dragg_item) # Traslate Drop
        self.on_leave          = lambda dragg_item : self.dragg_on_leave(DragTargetEvent=dragg_item) # Leafing Drop Line Border
        self.on_accept         = lambda dragg_item : self.dragg_on_accept(DragTargetEvent=dragg_item) # Leafing Drop Line Border

    def main_screen_style(self, code: str = ""):
        #: SET MAIN STYLE WIDGET
        return phone_style_widget.get(code)

    def dict_style(self, code: str = ""):
        #: SET CONTENT STYLE WIDGET
        return styles.get(code)

    def show_text_dragg_selected(self, name_selected: str = "") -> None:
        # session_id = self.page._session_id
        # self.name_selected = self.page.session.get(session_id)
        self.name_selected = name_selected
        self.widget_selected = self.page.session.get("SHOW_TEXT_SELECTED_DRAGG_WIDGET")
        self.draggs_selected = self.page.session.get("SHOW_TEXT_SELECTED_PHONE_WIDGET")

        self.widget_selected.content.controls[1].content.spans[0].text = "None"
        self.draggs_selected.content.controls[1].content.spans[0].text = self.name_selected
        self.widget_selected.bgcolor = ft.colors("black12")
        self.draggs_selected.bgcolor = ft.Colors.with_opacity(0.1,ft.colors("cyan"))
        self.widget_selected.update()
        self.draggs_selected.update()

    def dragg_on_will_accept(self, DragTargetEvent: object = None):
        DragTargetEvent.control.content.border = None
        DragTargetEvent.control.content.border = ft.border.all(4, ft.colors("cyan900"))
        DragTargetEvent.control.update()
        self.page.update()

    def dragg_on_accept(self, DragTargetEvent: object = None):
        # print(DragTargetEvent.control.content.content)
        self.widgetFilter = self.page.session.get("ONLY_CONTROLS_ADDING_IN_APP")

        session_id = self.page._session_id
        selectWidgetBox = self.page.session.get(session_id)

        self.InfinityBox = self.page.session.get("infinity_box")
        self.InstanceNewWidget = self.InfinityBox(
                                        dataPassed=selectWidgetBox,
                                        page=self.page
                                    )

        self.right_widget = DragTargetEvent.control.content.content
        self.right_control = self.right_widget._get_control_name()

        if self.right_control in self.widgetFilter:
            DragTargetEvent.control.content.content.controls.append(self.InstanceNewWidget)

        else:
            if self.right_control in self.widgetFilter:
                DragTargetEvent.control.content.content.controls.append(self.InstanceNewWidget)

            else:
                # GET FROM INFINITY DRAGG BOX CONTENT OF MAIN CONTAINER
                DragTargetEvent.control.content.content = self.InstanceNewWidget.widgets.get(selectWidgetBox)[0].content

        #: UPDATE COLOR WIDGET
        DragTargetEvent.control.content.border = True
        DragTargetEvent.control.content.border = ft.border.all(0, ft.colors("transparent"))
        DragTargetEvent.control.update()

        self.page.update()

    def draggin_framework(self, content: object =None) -> object():
        return ft.DragTarget(
            group="GroupDragg",
            on_will_accept    = lambda dragg_item : self.dragg_on_will_accept(DragTargetEvent=dragg_item), # Traslate Drop
            on_leave          = lambda dragg_item : self.dragg_on_leave(DragTargetEvent=dragg_item), # Leafing Drop Line Border
            on_accept         = lambda dragg_item : self.dragg_on_accept(DragTargetEvent=dragg_item), # Leafing Drop Line Border
            content=content
        )

    def dragg_on_leave(self, DragTargetEvent: object = None):
        DragTargetEvent.control.content.border = True
        DragTargetEvent.control.content.border = ft.border.all(0, ft.colors("transparent"))

        DragTargetEvent.control.update()
        self.page.update()

        # return ft.DragTarget(group="GroupDragg",on_will_accept=lambda dragg_item: self.dragg_on_will_accept(DragTargetEvent=dragg_item),  # Traslate Drop
        #     on_leave=lambda dragg_item: self.dragg_on_leave(DragTargetEvent=dragg_item),  # Leafing Drop Line Border
        #     on_accept=lambda dragg_item: self.dragg_on_accept(DragTargetEvent=dragg_item),  # Leafing Drop Line Border
        #     content=content
        # )

    def switch_border_selected(self, selected: object =None):
        selected_widget = self.page.session.get("SELECTED_CONTAINER")

        # print(selected_widget)
        if not selected_widget == None:
            selected_widget.border = ft.border.all(2, ft.colors("transparent"))
            selected_widget.update()

        selected.border = ft.border.all(2, ft.colors("yellow900"))
        selected.update()

        self.show_text_dragg_selected(
            name_selected=selected.content._get_control_name())

    def set_selected_widget(self, selected):
        self.page.session.set("SELECTED_CONTAINER", selected)

    def set_selected_widget_id(self, selected):
        self.page.session.set("SELECTED_CONTAINER_ID", selected.uid)

    def dragg_event(self, selected_widget: object =None):
        # def dragg_event(self,listWidget,e: ft.ContainerTapEvent):
        """
        NOTE:

        WE CAPTURE THE CLICK SELECTION_WIDGET SHOWING BORDER COLOR YELLOW

        IF PRESS IN OTHER WIDGET WE COMPARE tmp_list listWidgetUpdate
        IF IS DIFERENT SHOW BLACK COLOR THE PREVIEW SELECT_WIDGET

        NOTE:

        WE PASS TO Build_Editor => self.infinityDropWidget[0] THAT IS CLICKED SELECTION
        Build_Editor.update_widget_attributes(widget_cliked=ft.Container(content=ft.Text()))

        """

        # print(selected_widget.control)
        # SWITCH BORDER COLOR IN SELECTED CONTAINER PHONE
        self.selected = selected_widget.control
        # self.selected = selected_widget[0]
        self.page.session.set("cover_widget", self.selected.parent.parent)

        self.switch_border_selected(selected=selected_widget.control)
        self.set_selected_widget(selected=self.selected)
        self.set_selected_widget_id(selected=self.selected)

        # print(f"[-] {self.selected.tooltip} ID: <<< dragg_event: [infinity_box_layer_one.py]")


# MAKE CLASS A DYNAMIC MODULE
load_module_str = main_screen

if __name__ == "__main__":
    # RUN IN LINE
    # flet flet_box/extra_utils/phone_container/app_manager/views/main_screen.py  -r

    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.DARK  # ft.ThemeMode.LIGHT
        page.window.left = 0
        page.window.top = 0
        page.window.height = 567
        page.window.width = 320
        page.padding = 0
        page.spacing = 0
        page.add(
            load_module_str(
                    page= page,
                    main_page=True
            )
        )
        page.update()

    ft.app(
        target=main,
    )
