import os
from os import environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    URL = f"https://download.hagadmansa.com/"
    BANNED_ID = os.environ.get("BANNED_ID", "")
    TARGET_CHANNEL = int(environ.get("TARGET_CHANNEL", None))
     
def get_size(size):
    """Get size in readable format"""

    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])
