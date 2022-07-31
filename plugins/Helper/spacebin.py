import ssl
import certifi

from plugins.Helper.async_searcher import async_searcher

async def get_paste(data: str, extension: str = "txt"):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    json = {"content": data, "extension": extension}
    key = await async_searcher(
        url="https://spaceb.in/api/v1/documents/",
        json=json,
        ssl=ssl_context,
        post=True,
        re_json=True,
    )
    try:
        return True, key["payload"]["id"]
    except KeyError:
        if "the length must be between 2 and 400000." in key["error"]:
            return await get_paste(data[-400000:], extension=extension)
        return False, key["error"]
    except Exception as e:
        LOGS.info(e)
        return None, str(e)
