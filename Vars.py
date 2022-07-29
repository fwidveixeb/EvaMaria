import os
from os import environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    HEROKU_API_KEY = environ['HEROKU_API_KEY']
    HEROKU_APP_NAME = environ['HEROKU_APP_NAME']
    BIN_CHANNEL = int(environ.get("BIN_CHANNEL", None))
    URL = f"https://download.hagadmansa.com/"
