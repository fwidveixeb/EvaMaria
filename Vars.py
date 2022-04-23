import os
from os import environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    URL = f"https://download.hagadmansa.com/"
    BANNED_ID = os.environ.get("BANNED_ID", "")
    TARGET_CHANNEL = int(environ.get("TARGET_CHANNEL", None))
     
