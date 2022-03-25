from os import environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    BIN_CHANNEL = int(environ.get("BIN_CHANNEL", None)
     
