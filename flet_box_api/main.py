import json

from datetime import datetime
from flet_box_database.sqlite_db import sqlite_db
from fastapi import FastAPI
from fastapi import Body
host_api_server: str = 'https://kuko53348.pythonanywhere.com/'
PATH_DB: str = "flet_box_api/flet_box_database/flet_box_database.db"

app = FastAPI()

# APP TAGS
app.title: str = "Flet Box Api"
app.version: str = "0.0.1"
app.description: str = "Flet Box Api server is a amazing gui to make beutiful widget with flet framework"

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


@app.get('/validation_account', tags=['Loggin Account'])
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
@app.get('/get_widgets', tags=['Widgets Edition'])
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
@app.get('/get_projects_widgets', tags=['Widgets Edition'])
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
@app.put('/update_widgets', tags=['Widgets Edition'])
async def update_widgets(user_name: str = Body(), dragg_widget: str = Body()):
    """
    Updating database widgets

    ```python
    import requests
    import json

    request_session = requests.session()

    json_data: dict = {'user_name': self.user_name, 'dragg_widget' : self.dragg_widget }

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
    # for _ in dragg_widget:
    #     print(_)
    return {"Soucres code was succesfully saved"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
