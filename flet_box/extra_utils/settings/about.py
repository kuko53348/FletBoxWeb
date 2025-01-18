import flet as ft


class profile_container(ft.Stack):

    def __init__(self, data='Erase this test'):
        super().__init__()

        self.title = data

    def build(self):
        Drop_profile_container = ft.Container(
            ink=False,
            padding=ft.padding.all(0),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,

            content=ft.Column(
                controls=[
                    ft.Container(
                        ink=False,
                        padding=ft.padding.all(0),
                        margin=ft.margin.all(0),
                        alignment=ft.alignment.center,
                        content=ft.Text(
                            value="FOLLOW ME",
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.BOLD,
                            font_family="Consolas",
                            size=16,
                        ),),
                    ft.Container(
                        ink=False,
                        padding=ft.padding.all(0),
                        margin=ft.margin.all(0),
                        alignment=ft.alignment.center,
                        content=ft.Row(
                            controls=[
                                ft.IconButton(icon=ft.icons('facebook'), tooltip='FACEBOOK',
                                              url='https://facebook.com/groups/315046001621078/?mibextid=rS40aB7S9Ucbxw6v',),
                                ft.IconButton(icon=ft.icons(
                                    'discord'), tooltip='@legend_53348#0000',),
                                ft.IconButton(icon=ft.icons('chat'), tooltip='WHATSAPP GROUP',
                                              url='https://chat.whatsapp.com/ELFB8fSbdMS2chOjXiYAMo'),
                                ft.IconButton(icon=ft.icons(
                                    'email_rounded'), tooltip='xavier53348@gmail.com',   url='mailto:xavier53348@gmail.com'),
                                ft.IconButton(icon=ft.icons(
                                    'phone'), tooltip='(+53) 54448442',),
                                ft.IconButton(icon=ft.icons(
                                    'video_collection'), tooltip='YOUTUBE',                 url='https://www.youtube.com/@flet-box'),
                            ],),
                    ),
                ],
            ),
        )

        return Drop_profile_container


class ABOUT_BOX(ft.Stack):

    INFO_ABOUT = {

        'about_me': """With Flet-Box GUI, you can seamlessly build apps that run smoothly on various platforms, from desktop to mobile. Say goodbye to platform-specific limitations and hello to a unified development experience. Plus, with Python3 as the language of choice, you'll enjoy the simplicity and versatility that comes with one of the most popular programming languages in the world.""",
        'invitation': """So, are you ready to join us on this exciting adventure? Whether you're a developer looking to build your next big project or simply curious about the world of cross-platform app development, Flet-Box GUI welcomes you with open arms. Let's embark on this journey together and unlock the full potential of Flet framework.\nFeel free to reach out for inquiries or collaboration opportunities.""",

    }

    def __init__(self, header='header', body='body', footer='footer', ref_url='reference'):
        super().__init__()

        self.header = header
        self.body = body
        self.footer = footer
        self.reference = ref_url

    def build(self):
        Drop_ABOUT_BOX = ft.Container(
            padding=ft.padding.all(0),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            content=ft.Column(
                spacing=18,

                controls=[
                    ft.Container(
                        padding=ft.padding.all(0),
                        margin=ft.margin.all(0),
                        alignment=ft.alignment.center_left,
                        content=ft.Text(

                            value=self.header,
                            text_align=ft.TextAlign.LEFT,
                            weight=ft.FontWeight.BOLD,
                            font_family="Consolas",  # "Consolas ,RobotoSlab
                            size=18,
                        ),),
                    ft.Container(
                        padding=ft.padding.all(0),
                        margin=ft.margin.all(0),
                        alignment=ft.alignment.center_left,
                        width=400,
                        content=ft.Text(

                            value=self.INFO_ABOUT.get(self.body),
                            text_align=ft.TextAlign.LEFT,

                            font_family="Consolas",
                            color=ft.colors('white38'),
                            size=12,
                        ),),
                    ft.Container(
                        padding=ft.padding.all(0),
                        margin=ft.margin.all(0),
                        alignment=ft.alignment.center_left,
                        content=ft.Column(
                            spacing=0,
                            controls=[
                                ft.TextButton(
                                    text=self.footer,
                                    url=self.reference,
                                ),
                                ft.Container(height=4, width=124,
                                             bgcolor=ft.colors('white12')),
                            ]),
                    ),
                ],),
        )

        return Drop_ABOUT_BOX


class about_page(ft.Stack):
    data_dev = {
        'profile': """Experienced software developer with a passion for creating intuitive graphical user interfaces (GUIs) across multiple platforms. Dedicated to delivering high-quality, user-centric applications tailored to meet specific client needs.
        """
    }

    def __init__(self, page: object = None):
        super().__init__()
        self.page = page

    def build(self):
        self.left_column = ft.Container(
            ink=False,
            padding=ft.padding.all(4),
            margin=ft.margin.all(4),
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.START,

                controls=[
                    ft.Container(height=7, width=123,
                                 bgcolor=ft.colors('white12')),
                    ft.Container(
                        ink=False,
                        padding=ft.padding.all(0),
                        margin=ft.margin.all(0),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(80),
                        border=ft.border.all(2, ft.colors('black45')),
                        width=150,
                        height=150,
                        bgcolor=ft.colors('black45'),
                        content=ft.Image(
                            src='.my_avatar.png',
                            fit=ft.ImageFit.COVER,
                            repeat=ft.ImageRepeat.NO_REPEAT,
                            border_radius=ft.border_radius.all(80),
                            opacity=0.6,
                            expand=True,
                        ),),
                    ft.Container(
                        ink=False,
                        padding=ft.padding.all(0),
                        margin=ft.margin.all(0),
                        alignment=ft.alignment.center_left,
                        width=350,
                        content=ft.Text(
                            value="Hi There!!",
                            text_align=ft.TextAlign.LEFT,
                            weight=ft.FontWeight.BOLD,
                            font_family="Consolas",  # "Consolas ,RobotoSlab
                            size=24,
                        ),),
                    ft.Container(
                        ink=False,
                        padding=ft.padding.all(0),
                        margin=ft.margin.all(0),
                        alignment=ft.alignment.center_left,
                        width=350,
                        content=ft.Text(
                            value="DEV:      Maenys Javier Quesada Reyes\nFrom:    CUBA",
                            text_align=ft.TextAlign.LEFT,
                            weight=ft.FontWeight.BOLD,
                            font_family="Consolas",  # "Consolas ,RobotoSlab
                            size=18,
                        ),),
                    ft.Container(
                        ink=False,
                        padding=ft.padding.all(0),
                        margin=ft.margin.all(0),
                        alignment=ft.alignment.center_left,
                        width=350,
                        content=ft.Text(
                            value=self.data_dev.get('profile'),
                            text_align=ft.TextAlign.LEFT,
                            font_family="RobotoSlab",  # "Consolas ,RobotoSlab
                            color=ft.colors('white38'),
                            size=12,
                        ),),
                    ft.Container(
                        ink=False,
                        padding=ft.padding.all(8),
                        margin=ft.margin.all(8),
                        alignment=ft.alignment.center,
                        content=ft.ElevatedButton(
                            text='GIT-HUB',
                            bgcolor=ft.colors('white12'),
                            url='https://github.com/xavier53348/Flet-Box',
                            elevation=16,
                        ),),
                ],
            ),
        )

        self.right_column = ft.Container(
            ink=False,
            padding=ft.padding.all(8),
            margin=ft.margin.all(8),
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ABOUT_BOX(
                        header="FLET-BOX",
                        body='about_me',
                        footer="LEARN MORE 🮥",
                        ref_url='https://github.com/xavier53348/Flet-Box/blob/main/docs/Roadmap.md',
                    ),
                    ABOUT_BOX(
                        header="WORK TOGETHER",
                        body='invitation',
                        footer="LEARN MORE 🮥",
                        ref_url='https://github.com/xavier53348/Flet-Box/blob/main/WIDGET.md',
                    ),
                    profile_container(),
                ],
            ),
        )

        Drop_about_page = ft.Container(
            ink=False,
            bgcolor=ft.colors('black12'),
            padding=ft.padding.all(32),
            margin=ft.margin.all(8),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(30),
            border=ft.border.all(1, ft.colors('white12')),
            # height        = 650,
            # width=1200,
            # blur=(20,20),
            expand=True,
            image=ft.DecorationImage(
                src='backend.webp',
                fit=ft.ImageFit.COVER,
                opacity=0.04
            ),
            on_click=lambda _: self.show_widgets(show_widget='about_page'),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self.left_column,
                    self.right_column,
                ],),
        )
        return Drop_about_page

    def show_widgets(self, show_widget):
        """SHOW PAGES"""
        ...
        self.page.go('/')


if __name__ == '__main__':
    def main(page: ft.Page):
        page.scroll = "HIDDEN"  # AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK  # ft.ThemeMode.LIGHT
        page.window_bgcolor = ft.colors('red100')
        page.window_left = 3
        page.window_top = 3
        page.window_height = 700
        page.window_width = 800
        page.padding = 0
        page.spacing = 0
        page.add(about_page())

    ft.app(
        target=main,
        assets_dir="assets"

    )
