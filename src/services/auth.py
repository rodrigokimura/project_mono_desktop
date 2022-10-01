import json

import requests

from config import Config


class Auth:
    def login(self, username, password):
        r = requests.post(
            Config().MONO_URL + "api-token-auth/",
            data={"username": username, "password": password},
        )
        if r.ok:
            token = r.json().get("token")
            self.store_token(token)
            print(token)
            return True
        print(r.status_code)
        print(r.content)
        return False

    def store_token(self, token):
        with open(Config().TOKEN_FILE, "w+") as file:
            json.dump({"token": token}, file, indent=4)

    def read_token(self):
        try:
            with open(Config().TOKEN_FILE, "r") as file:
                return json.load(file).get("token")
        except FileNotFoundError:
            return None

    def has_valid_token(self):
        token = self.read_token()
        if token is None:
            return False
        r = requests.get(
            Config().MONO_URL + "accounts/api-me/",
            headers={"authorization": f"Token {token}"},
        )
        return r.ok
