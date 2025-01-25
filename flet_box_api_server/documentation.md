# Documntation FAST-API server Flet-Box Web API

```bash
>>> 'https://kuko53348.pythonanywhere.com/docs#/'
```

## Start FAST-API server local host

```bash
>>> uvicorn --app-dir "./flet_box_api_server/" main:app --host 0.0.0.0 --port 8080 --reload
```

## Start FAST-API server in pythonanywhere.com

```bash
>>> mkvirtualenv .venv --python=python3.10
```

## Install basic dependecies

``` bash
>>> pip install "uvicorn[standard]" fastapi
>>> pip install --upgrade pythonanywhere
```

## Create file

```bash
>>> mkdir ~/flet_box_api_server/
>>> touch ~/flet_box_api_server/main.py
```

## Create demo in main.py

```python
>>> from fastapi import FastAPI
>>>
>>> app = FastAPI()
>>>
>>> @app.get("/")
>>> async def root():
>>>    return {"message":"Hello from FastAPI"}
```

## Create web app

```bash

# pa website get kuko53348.pythonanywhere.com
# pa website delete --domain kuko53348.pythonanywhere.com
# pa website reload kuko53348.pythonanywhere.com

# pa website create --domain USERNAME.pythonanywhere.com -c '/home/USERNAME/.virtualenvs/.venv/bin/uvicorn --app-dir "/home/USERNAME/folder_app" --uds ${DOMAIN_SOCKET} main:app'
>>> pa website create --domain kuko53348.pythonanywhere.com -c '/home/kuko53348/.virtualenvs/.venv/bin/uvicorn --app-dir "/home/kuko53348/flet_box_api_server" --uds ${DOMAIN_SOCKET} main:app'
```

## Run manually web app

```bash
# RUN
# https://kuko53348.pythonanywhere.com/
>>> home/kuko53348/.virtualenvs/.venv/bin/uvicorn --app-dir /home/kuko53348/flet_box_api/ --uds kuko53348.pythonanywhere.com main:app
```
