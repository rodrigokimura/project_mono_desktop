import os

from dotenv import load_dotenv

load_dotenv("src/.env")


class Config:
    def __init__(self):
        self.MONO_URL = os.getenv("MONO_URL")
