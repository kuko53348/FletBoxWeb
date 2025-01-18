import json

from datetime import datetime
from flet_box_database.sqlite_db import sqlite_db
from fastapi import FastAPI
from fastapi import Body


# host_api_server: str = 'https://kuko53348.pythonanywhere.com/'

# python everywhere path
PATH_DB: str = "flet_box_api_server/flet_box_database/flet_box_database.db"

app = FastAPI()

# show_hide_shemas: bool =True # Will show hidden shemas
show_hide_shemas: bool =False

# APP TAGS
app.title: str = "Flet Box Api"
app.version: str = "0.0.1"
app.description: str = """
Fletbox is an intuitive GUI builder interface designed for creating cross-platform applications with ease. It features a drag-and-drop functionality, allowing users to visually design user interfaces without extensive coding knowledge
"""

@app.get('/', tags=['Welcome to FletBox api server'])
async def home_screen():
    """
    FletBox Web Api lobby

    ```python

    import requests

    request_session = requests.session()

    # lobby screen
    tmp_data = request_session.get(f'https://kuko53348.pythonanywhere.com/')
    data_returned = tmp_data.json()
    ```
    """

    return {'home': 'welcome to home page flet box Api server'}

# GET LOGIN


@app.get('/login', tags=['Loggin Account'])
async def login(user_email: str = "", user_password: str = "") -> list:
    """
    Login with your email and paswword

    ```python
    import requests

    request_session = requests.session()

    # Exemple: 1
    tmp_data = request_session.get(f'https://kuko53348.pythonanywhere.com/login?user_email={self.user_email}&user_password={self.user_password}')

    # Exemple: 2
    tmp_data = request_session.get(f'https://kuko53348.pythonanywhere.com/login',params={'user_email': self.user_email,'user_password':self.user_password})

    data_returned = tmp_data.json()
    ```
    """
    # kuko53348@gmail.com
    sqlite_obj = sqlite_db(path_db=PATH_DB)
    data_returned = sqlite_obj.find_name(
        table_name='register',
        column='user_email',
        name=user_email,
        match=['user_password', user_password])

    if data_returned:
        return data_returned[0]
    else:
        return []

# GET EMAIL RECOVER


@app.get('/email_recover', tags=['Loggin Account'])
async def email_recover(user_email: str = "") -> list:
    """
    Recover your account passord by email

    ```python

    import requests

    request_session = requests.session()

    # Exemple: 1
    tmp_data = request_session.get(f'https://kuko53348.pythonanywhere.com/email_recover?user_email={self.user_email}')

    # Exemple: 2
    tmp_data = request_session.get(f'https://kuko53348.pythonanywhere.com/email_recover',params={'user_email': self.user_email})

    data_returned = tmp_data.json()
    ```
    """
    # kuko53348@gmail.com
    sqlite_obj = sqlite_db(path_db=PATH_DB)
    data_returned = sqlite_obj.find_name(
        table_name='register',
        column='user_email',
        name=user_email
    )
    if data_returned:
        return data_returned[0]
    else:
        return []

# CHECK USERNAME EMAIL


@app.get('/validation_account',include_in_schema=show_hide_shemas, tags=['Loggin Account'])
async def validation_account(user_name: str = "", user_email: str = "") -> dict:
    """
    This validation let not have duplicates emails and usernames

    ```python
    import requests

    request_session = requests.session()

    # Exemple: 1
    tmp_data = request_session.get(f'https://kuko53348.pythonanywhere.com/validation_account?user_name={self.user_register_str}&user_email={self.email_register_str}')

    # Exemple: 2
    validation = {'user_name': self.user_register_str,'user_email':self.email_register_str}
    tmp_data = request_session.get(f'https://kuko53348.pythonanywhere.com/validation_account',params=validation)

    data_returned = tmp_data.json()
    ```
    """
    # kuko53348@gmail.com
    # IF NO EXIT DUPLICATE USER_NAME CONTINUE
    sqlite_obj = sqlite_db(path_db=PATH_DB)
    user_name = sqlite_obj.find_name(
        table_name='register',
        column='user_name',
        name=user_name
    )

    # IF NO EXIT DUPLICATE USER_EMAIL CONTINUE
    sqlite_obj = sqlite_db(path_db=PATH_DB)
    user_email = sqlite_obj.find_name(
        table_name='register',
        column='user_email',
        name=user_email
    )

    if not user_name and not user_email:
        # return user_name[0],user_email[0]
        return {'validated_account': True}

    elif not user_name and user_email:
        return {
            'user_name': False,
            'user_email': True
        }
    elif user_name and not user_email:
        return {
            'user_name': True,
            'user_email': False
        }
    else:
        return {
            'user_name': True,
            'user_email': True
        }


# POST REGISTER ACCOUNT
@app.post('/register_account', tags=['Loggin Account'])
async def register_account(user_name: str = "", user_email: str = "", user_password: str = "") -> list:
    """
    Register your account in FletBox web database

    ```python
    import requests

    request_session = requests.session()

    # Exemple: 1
    tmp_data = request_session.post(f'https://kuko53348.pythonanywhere.com/register_account?user_name={self.user_name}&user_email={self.user_email}&user_password={self.user_password}')

    # Exemple: 2
    validation = {'user_name': self.user_register_str,'user_email':self.email_register_str, 'user_password': self.password_register_str}
    tmp_data = request_session.post(f'https://kuko53348.pythonanywhere.com/validation_account',params=validation)

    data_returned = tmp_data.json()

    ```
    """
    # kuko53348@gmail.com
    # WRITE DATA IN REGISTER TABLE
    sqlite_obj = sqlite_db(path_db=PATH_DB)
    sqlite_obj.write_data(
        table_name='register',
        column=(
            user_name,
            user_email,
            user_password,
            str(datetime.now())
        ))

    # WITE DATA BY DEFAULD IN SCREENS TABLE
    sqlite_obj = sqlite_db(path_db=PATH_DB)
    sqlite_obj.write_data(
        table_name='user_screen',
        column=(
            user_name,  # user_name
            'None',  # main_screen
            'None',  # screen_one
            'None',  # screen_two
            'None',  # screen_three
            'None',  # screen_four
            'None',  # screen_five
            'None',  # screen_six
            'None',  # screen_seven
            'None',  # screen_eigth
            'None',  # screen_nine
            'None',  # screen_ten
            'None',  # screen_eleven
            'None',  # screen_twelve
        )
    )

    return {'Account was registered succesfully'}

# POST SAVED WIDGETS IN DATABASE ACCOUNT
@app.get('/get_widgets',include_in_schema=show_hide_shemas, tags=['Widgets Edition'])
async def get_widgets(user_name: str = ""):
    """
    Dump all index in marketplace by selected column

    ```python

    import requests

    request_session = requests.session()

    data_returned = request_session.get('https://kuko53348.pythonanywhere.com/get_widgets', params={'user_name': self.tmp_session_user_name})
    data_returned = tmp_data.json()
    ```
    """
    sqlite_obj = sqlite_db(path_db=PATH_DB)
    data_returned = sqlite_obj.find_name(
        table_name='user_screen',
        column='user_name',
        name=user_name
    )

    if data_returned:
        return data_returned[0]
    else:
        return []


# GET PROJECTS WIDGETS IN DATABASE
@app.get('/get_projects_widgets',include_in_schema=show_hide_shemas, tags=['Widgets Edition'])
async def get_projects_widgets(table_name: str = ""):
    """
    Dump all projects widgets in marketplace by selected column

    ```python

    import requests

    request_session = requests.session()

    data_returned = request_session.get('https://kuko53348.pythonanywhere.com/get_projects_widgets', params={'table_name': self.table_name})
    data_returned = tmp_data.json()
    ```
    """
    sqlite_obj = sqlite_db(path_db=PATH_DB)
    data_returned = sqlite_obj.find_all(table_name=table_name)


    if data_returned:
        return data_returned
    else:
        return []

# POST SAVED WIDGETS IN DATABASE ACCOUNT
@app.put('/update_widgets',include_in_schema=show_hide_shemas, tags=['Widgets Edition'])
async def update_widgets(user_name: str = Body(), dragg_widget: str = Body(),app_widget: str = Body()):
    """
    Updating database widgets

    ```python
    import requests
    import json

    request_session = requests.session()

    json_data: dict = {'user_name': self.user_name, 'dragg_widget' : self.dragg_widget ,'app_widget': self.app_dragg_template}

    data_returned = request_session.put('https://kuko53348.pythonanywhere.com/update_widgets', data=json.dumps(json_data))
    print(data_returned.text)
    ```
    """
    # kuko53348@gmail.com
    # UPDATE DATA REGISTER TABLE
    sqlite_obj = sqlite_db(path_db=PATH_DB)
    sqlite_obj.update_data(
        table_name='user_screen',
        change_data=('user_name', user_name),
        by_data=('main_screen', dragg_widget)
    )

    sqlite_obj = sqlite_db(path_db=PATH_DB)
    sqlite_obj.update_data(
        table_name='user_screen',
        change_data=('user_name', user_name),
        by_data=('screen_one', app_widget)
    )

    # for _ in dragg_widget:
    #     print(_)
    return {"Source code was succesfully saved"}

# POST SAVED WIDGETS IN DATABASE ACCOUNT
@app.post('/save_module_widgets',include_in_schema=show_hide_shemas, tags=['Widgets Edition'])
async def save_module_widgets(
                                user_name: str = Body(),
                                project_tab: str = Body(),
                                name_project: str = Body(),
                                ranking_app: str = Body(),
                                dragg_screen: str = Body(),
                                app_screen: str = Body(),
                                time_created: str = Body()
                                ):
    """
    Updating database widgets

    ```python
    import requests
    import json

    request_session = requests.session()

    json_data:  dict={
            'user_name':self.user_name,
            'project_tab':column_tab_db,
            'name_project':name_project_db,
            'ranking_app':'0',
            'dragg_screen':self.class_bone,
            'app_screen':name_app_project_db,
            'time_created':time_created_db
    }

    data_returned = request_session.put('https://kuko53348.pythonanywhere.com/save_module_widgets', data=json.dumps(json_data))
    print(data_returned.text)
    ```
    """
    # UPDATE DATA REGISTER TABLE
    sqlite_obj = sqlite_db(path_db=PATH_DB)
    user_name_have_same_project = sqlite_obj.find_name(
                                table_name=project_tab,
                                column='user_name',
                                name=user_name,
                                match=['name_project', name_project]
    )


    if not user_name_have_same_project == False:
        # UPDATE IF EXIT PROJECT
        sqlite_obj = sqlite_db(path_db=PATH_DB)
        sqlite_obj.update_data(
            table_name=project_tab,
            change_data=('name_project', name_project),
            by_data=('dragg_screen', dragg_screen)
        )
        # UPDATE IF EXIT PROJECT
        sqlite_obj = sqlite_db(path_db=PATH_DB)
        sqlite_obj.update_data(
            table_name=project_tab,
            change_data=('name_project', name_project),
            by_data=('app_screen', app_screen)
        )

    else:
        # WITE NEW PROJECT IF NOT EXIT IN DATABASE
        sqlite_obj = sqlite_db(path_db=PATH_DB)
        sqlite_obj.write_data(
            table_name=project_tab,
            column=(
                user_name,
                project_tab,
                name_project,
                ranking_app,
                'None',
                app_screen,
                time_created
            )
        )

        sqlite_obj = sqlite_db(path_db=PATH_DB)
        sqlite_obj.update_data(
            table_name=project_tab,
            change_data=('dragg_screen', 'None'),
            by_data=('dragg_screen', dragg_screen)
        )
        sqlite_obj = sqlite_db(path_db=PATH_DB)
        sqlite_obj.update_data(
            table_name=project_tab,
            change_data=('dragg_screen', 'None'),
            by_data=('app_screen', app_screen)
        )
    return {"Source code was succesfully saved"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
