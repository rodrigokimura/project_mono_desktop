import json
from dataclasses import dataclass
from typing import List

import requests

from config import Config
from services.auth import Auth


@dataclass
class Checklist:
    id: int
    name: str


class Checklists:
    def list(self):
        r = requests.get(
            Config().MONO_URL + "cl/api/checklists/",
            headers={"authorization": f"Token {Auth().read_token()}"},
        )
        for c in r.json().get("results"):
            yield Checklist(**c)
