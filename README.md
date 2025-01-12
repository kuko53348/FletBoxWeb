<!-- <img src="docs/gallery/full_screen.png" alt="Imagen Flet-Box"> -->
<!-- markdownserver http://localhost:8009/README.md -->
<!-- http://localhost:8080/Desktop/git_hub/flet_box/docs/Roadmap#flet-box-framework-roadmap -->
<!-- pip error -->
<!-- pip install coincurve --only-binary :all: -->

## Flet-Box:
### It's a Python GUI Framework for Multi-Platform Apps

[![Gallery Preview FLET-BOX](https://github.com/xavier53348/Flet-Box/blob/main/flet_box/assets/.screen_1.png)](https://www.youtube.com/watch?v=15DDAACb0Hw)

<details>
    <summary>Gallery Preview FLET-BOX</summary>
    <img src="https://github.com/xavier53348/Flet-Box/blob/main/flet_box/assets/.screen_1.png"    alt="Imagen Flet-Box">
    <img src="https://github.com/xavier53348/Flet-Box/blob/main/flet_box/assets/.screen_2.png"    alt="Imagen Flet-Box">
    <img src="https://github.com/xavier53348/Flet-Box/blob/main/flet_box/assets/.screen_3.png"    alt="Imagen Flet-Box">
    <img src="https://github.com/xavier53348/Flet-Box/blob/main/flet_box/assets/.screen_4.png"    alt="Imagen Flet-Box">
</details>


[More info documentation](https://github.com/xavier53348/Flet-Box/blob/main/docs/WIDGET.md)

[Our goals and Roadmap](https://github.com/xavier53348/Flet-Box/blob/main/docs/Roadmap.md)

**Certainly!** Let's create a documentation for **Flet-Box**, a GUI framework that simplifies building multi-platform apps using drag-and-drop widgets in the Python language.

### Certainly!

If you're passionate about shaping the future of frameworks and contributing to their development, I invite you to join our collaborative efforts. Here's how you can get involved:

1. **Documentation and Modules**:

- **Documentation**: We're actively working on creating comprehensive documentation for our Flet-Box framework. Your contributions can help make it more accessible, accurate, and user-friendly. Whether you're an expert or a beginner, your insights matter!

- **Modules**: Our framework consists of various modules that handle different aspects of Flet activities. If you have expertise in any specific area (such as Documentation, Modules, or consensus algorithms ), consider contributing by improving existing modules or proposing new ones.

2. **Financial Considerations**:

- If you're passionate about supporting open-source projects and want to contribute to the **Flet-box Framework**, here's a simple invitation for you:

**You may contribute Donating tokens to give suppor to the proyect in  MATIC , BINANCE or TRX Tokens**

- **Low Fees**: In transactions have extremely low fees, making it ideal for micro-donations.
- Invite me a **COFFE** or a **BEER** ..

**How to Donate Tokens:**
- **Get Token**: Purchase MATIC
- **Donate**: Visit the Flet-box page and contribute directly. **Every donation counts!**

**MATIC WALLET**

| **TOKEN POL/MATIC**                                                                         |    **ADDRESS**                                            |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <img src="flet_box/assets/.wallet_matic.jpg"  style="width:240px" align="Center">          | 0x6d437bB66af8d2c44670eA18F059BE1417Dcd7bA                |

- **Learn More**: Explore Flet-box's mission, roadmap, and community initiatives on their official website.

3. **Collaboration and Feedback**:
- We value diverse perspectives. Engage in discussions, attend working groups, and provide feedback during public consultations.

## Instalation Flet-Box
```bash

>>> mkdir My_app
>>> cd My_app
```
## Run one time
```bash

>>> sudo apt-get install python3-full
>>> python3 -m venv .venv
```

## Activate virtual env
```bash
>>> pip install secure-smtplib mime
>>> source .venv/bin/activate
>>> pip install --upgrade pip
>>> pip install -r requirements.txt
```

## Error with libmpv1

```bash
>>> sudo apt install libmpv1
```

## Error libmpv1.so no found "UBUNTU 24.04"
```bash
# install dependencies
sudo apt-get install libmpv-dev libmpv2

# will return
locate libmpv.so

# /usr/lib/x86_64-linux-gnu/libmpv.so
# /usr/lib/x86_64-linux-gnu/libmpv.so.2
# /usr/lib/x86_64-linux-gnu/libmpv.so.2.2.0

sudo cp /usr/lib/x86_64-linux-gnu/libmpv.so.2 /usr/lib/x86_64-linux-gnu/libmpv.so.1
```
## Install manually

```bash
>>> git clone https://github.com/xavier53348/Flet-Box.git
```

## Easy run Flet-Box
```bash

>>> flet flet_box/main.py -r -p 8081
```

### Introduction
**Flet-Box** is a powerful framework that enables developers to create interactive multi-user web, desktop, and mobile applications. Whether you're a seasoned developer or just starting out, **Flet-Box** makes frontend development accessible without prior experience. Here are the key features:

1. **Cross-Platform**: Build apps that run seamlessly on web browsers, desktop environments (like macOS and Windows), and mobile devices.

2. **Drag-and-Drop Widgets**: Easily design your app's user interface by dragging and dropping widgets.

3. **Based on Flutter**: **Flet-Box** is a fork of **Flet Framework** leverages the power of Flutter by Google, but it doesn't stop there. It adds its own opinion by combining smaller widgets, implementing UI best practices, and applying reasonable defaults to ensure your apps look professional without extra effort.

### Getting Started with Flet-Box in Python
To get started, you don't need to be a front-end guru, but basic knowledge of Python and object-oriented programming is recommended. Let's dive into the basics:

### Learn More
Ready to build real-world apps? Check out the [official Flet documentation](https://flet.dev/docs/) and explore tutorials for your preferred language, including Python3. Happy coding! 🚀

### Widgets aviables with Flet-Box Now on building

Certainly! In **Flet-Box**, you can create drag-and-drop interactions using the **LongPressDraggable** widget. Let's break down how to achieve this:

1. **LongPressDraggable**: This widget recognizes when a user performs a long press (sometimes called touch & hold) on a widget. It then displays a new widget near the user's finger. As the user drags, the widget follows their finger. You have full control over the widget that the user drags.

- Wrap your UI element (widget) with a **LongPressDraggable**. For example, if you have a list of menu items, each displayed using a custom **MenuListItem** widget, you can wrap it like this:

<!-- make tree -->
<!-- tree -I '__pycache__|__init__.py|test|drag_drop_proyect|flet_box.egg-info|docs|.|build|dist|LICENSE|MANIFEST.in|requeriments.txt|README.md|pyproject.toml|setup.py' > full_path.txt -->

### Path Flet-Box Modules
```bash
.
├── flet_box
│   ├── assets
│   ├── extra_utils
│   │   ├── config_container
│   │   │   ├── blur_color_entry.py
│   │   │   ├── bool_entry.py
│   │   │   ├── color_entry.py
│   │   │   ├── double_entry.py
│   │   │   ├── dual_number_entry.py
│   │   │   ├── four_entry.py
│   │   │   ├── gradient_entry.py
│   │   │   ├── photo_selection.py
│   │   │   ├── selection_button_entry.py
│   │   │   ├── selection_entry.py
│   │   │   ├── single_entry.py
│   │   │   ├── single_number_entry.py
│   │   │   ├── small_palette_color.py
│   │   │   └── widget_editor.py
│   │   ├── drag_container
│   │   │   ├── dragg_widget.py
│   │   │   ├── infinity_box_layer_one.py
│   │   │   └── widget_drag_editor.py
│   │   ├── external_library
│   │   │   ├── create_skelenton.py
│   │   │   ├── flet_box_database.db
│   │   │   ├── library_email.py
│   │   │   └── sqlite_db.py
│   │   ├── lite_menu_bar_down_phone
│   │   │   ├── footer_bar_menu_phone.py
│   │   │   └── selected_widget.py
│   │   ├── lite_menu_bar_right_phone
│   │   │   └── right_bar_menu_phone.py
│   │   ├── login_page
│   │   │   └── login_page.py
│   │   ├── menu_tab_left_phone
│   │   │   ├── refactory_flet_box.py
│   │   │   └── menu_left_editor.py
│   │   ├── menu_tab_up_phone
│   │   │   ├── basic_menu_tab_up.py
│   │   │   └── widget_menu_tab_editor.py
│   │   └── phone_container
│   │       ├── app_manager
│   │       │   ├── app_screen_manager.py
│   │       │   └── views
│   │       │       ├── main_screen_events.py
│   │       │       ├── main_screen.py
│   │       │       └── main_screen_styles.py
│   │       └── widget_phone_editor.py
│   ├── main.py
└── VERSION
```

## Widgets will be Updating ...
#### You mey use now the currents widgets that are marked

| **SPACE LAYOUTS**        |   | **IMAGE WIDGET**         |   | **ALERTS STATUS**        |   |
|--------------------------|---|--------------------------|---|--------------------------|---|
| ft.divider               | ✔ | ft.image                 | ✔ | ft.snackbar              | ✘ |
| ft.verticaldivider       | + | ft.circleavatar          | + | ft.tooltip               | ✔ |
|                          |   | ft.icon                  | ✔ | ft.cupertinoalertdialog  | ✘ |
|                          |   |                          |   | ft.cupertinodialogaction | ✘ |
|                          |   |                          |   |                          |   |
| **CONTAINERS LAYOUTS**   |   | **CHARTS LAYOUTS**       |   | **TEXT WIDGET**          |   |
| ft.stack                 | ✔ | ft.barchart              | ✘ | ft.text                  | ✔ |
| ft.row                   | ✔ | ft.charts                | ✘ | ft.textfield             | ✔ |
| ft.gridview              | ✔ | ft.linechart             | ✘ | ft.listview              | ✘ |
| ft.column                | ✔ | ft.matplotlibchart       | ✘ | ft.datatable             | ✘ |
| ft.container             | ✔ | ft.piechart              | ✘ |                          |   |
| ft.card                  | ✘ | ft.plotlychart           | ✘ |                          |   |
| ft.responsiverow         | ✘ |                          |   |                          |   |
| ft.transparentpointer    | ✘ |                          |   |                          |   |
|                          |   |                          |   |                          |   |
| **BUTTONS WIDGET**       |   | **SELECTIONS WIDGET**    |   | **ESPECIAL WIDGET**      |   |
| ft.textbutton            | ✔ | ft.switch                | ✘ | ft.tabs                  | ✘ |
| ft.filledbutton          | ✔ | ft.checkbox              | ✔ | ft.navigationbar         | ✘ |
| ft.filledtonalbutton     | ✔ | ft.cupertinocheckbox     | ✔ | ft.cupertinoappbar       | ✘ |
| ft.iconbutton            | ✔ | ft.cupertinoradio        | ✔ | ft.navigationdrawer      | ✘ |
| ft.elevatedbutton        | ✔ | ft.cupertinoslider       | ✔ | ft.navigationrail        | ✘ |
| ft.chip                  | ✔ | ft.cupertinoswitch       | ✔ | ft.menubar               | ✘ |
| ft.outlinedbutton        | ✔ | ft.submenubutton         | ✘ | ft.appbar                | ✘ |
| ft.bottomappbar          | ✘ | ft.dropdown              | ✘ | ft.cupertinonavigationbar| ✘ |
| ft.bottomsheet           | ✘ | ft.datepicker            | ✘ | ft.searchbar             | ✘ |
| ft.segmentedbutton       | ✘ | ft.timepicker            | ✘ |                          |   |
| ft.floatingactionbutton  | ✘ | ft.filepicker            | ✘ |                          |   |
|                          |   | ft.radio                 | ✘ |                          |   |
|                          |   |                          |   |                          |   |
| **WIDGETS STATUS**       |   |
| ft.slider                | ✘ |
| ft.progressbar           | ✘ |
| ft.progressring          | ✘ |
| ft.alertdialog           | ✘ |
| ft.rangeslider           | ✘ |

