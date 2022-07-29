import requests
from requests.exceptions import MissingSchema

def is_url_ok(url: str):
    try:
        r = requests.head(url)
    except MissingSchema:
        return None
    except BaseException:
        return False
    return r.ok
