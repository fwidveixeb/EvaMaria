import requests

def is_url_ok(url: str):
    try:
        import requests
    except ImportError:
        raise DependencyMissingError("This function needs 'requests' to be installed.")
    try:
        r = requests.head(url)
    except MissingSchema:
        return None
    except BaseException:
        return False
    return r.ok
