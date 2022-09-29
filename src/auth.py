import requests

from config import Config


def login(username, password):
    r = requests.post(
        Config().MONO_URL + "api-token-auth/",
        data={"username": username, "password": password},
    )
    if r.ok:
        token = r.json().get("token")
        print(token)
    else:
        print(r.status_code)
        print(r.content)
