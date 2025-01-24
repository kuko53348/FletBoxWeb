import requests
import asyncio
import json


def async_requests(
    type: str = str(),
    url: str = str(),
    path: str = str(),
    payload: str = str(),
):
    """
    ### Send requests by async
    ```python
    >>> code = async_requests(
            type='get',
            path='login',
            url='https://kuko53348.pythonanywhere.com/',
            payload =  {'user_name': 'kuko53348','user_email':'kuko53348@gmail.com'},
    )
    >>> print(f'Status code {code')
    ```
    ### Arguments
    - path='login'
    - url='https://kuko53348.pythonanywhere.com'
    - url_path='https://kuko53348.pythonanywhere.com/login'
    path='{url}/{path}/{payload}'
    """

    url_session = url
    request_type = type.lower()
    request_session = requests.session()

    full_path: str = f"{url_session}{path}"

    async def main():
        if request_type == "get":
            code = request_session.get(full_path, params=payload)

        if request_type == "put":
            # PUT ONLY WILL BE ON WEB
            code = request_session.put(full_path, params=payload)

        if request_type == "post":
            # PUT ONLY WILL BE ON WEB
            code = request_session.post(full_path, params=payload)

        if request_type == "delete":
            ...

        await asyncio.sleep(0.2)

        # Check if state is correct
        data_request = code.status_code
        print(data_request, "<<<<<<<< status code")
        if data_request == 200:
            return code.json()

    try:
        status_code_returned = asyncio.run(main())
        # print(status_code_returned)
        return status_code_returned

    except Exception as e:
        return False


if __name__ == "__main__":
    code_returned = async_requests(
        type="get",
        url="http://0.0.0.0:8080/",
        path="login",
        payload={"user_email": "kuko53348@gmail.com", "user_password": "123"},
    )

    print(f"Status code {code_returned}")
