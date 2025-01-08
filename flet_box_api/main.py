from datetime import datetime
from flet_box_database.sqlite_db import sqlite_db
from fastapi import FastAPI

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

    tmp_data = requests.get(f'{host_api_server}')
    data_returned = tmp_data.json()
    ```
    """

    return {'home': 'welcome to home page flet box Api server'}

# GET LOGIN


@app.get('/login', tags=['Loggin Account'])
async def get_login_user(user_email: str = "", user_password: str = "") -> list:
    """
    Login with your email and paswword

    ```python
    import requests

    tmp_data = requests.get(f'{host_api_server}login?user_email={self.user_email}&user_password={self.user_password}')
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


@app.get('/email_recover', tags=['email_recover'])
async def get_login_user(user_email: str = "") -> list:
    """
    Recover your account passord by email

    ```python

    import requests

    tmp_data = requests.get(f'{host_api_server}email_recover?user_email={self.user_email}')
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


@app.get('/validation_account', tags=['validation_account'])
async def get_login_user(user_name: str = "", user_email: str = "") -> dict:
    """
    This validation let not have duplicates emails and usernames

    ```python
    import requests

    tmp_data = requests.get(f'{host_api_server}email_recover?user_email={self.user_email}')
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
@app.post('/register_account', tags=['register_account'])
async def get_login_user(user_name: str = "", user_email: str = "", user_password: str = "") -> list:
    """
    Register your account in FletBox web database

    ```python
    import requests

    requests.post(f'{host_api_server}register_account?user_name={self.user_name}&user_email={self.user_email}&user_password={self.user_password}')
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
