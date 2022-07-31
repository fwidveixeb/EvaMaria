from io import BytesIO
from plugins.Helper.async_searcher import async_searcher

async def Carbon(
    code,
    base_url="https://carbonara-42.herokuapp.com/api/cook",
    file_name="ultroid",
    download=False,
    rayso=False,
    **kwargs,
):
    if rayso:
        base_url = "https://raysoapi.herokuapp.com/generate"
        kwargs["text"] = code
        kwargs["theme"] = kwargs.get("theme", "meadow")
        kwargs["darkMode"] = kwargs.get("darkMode", True)
        kwargs["title"] = kwargs.get("title", "Ultroid")
    else:
        kwargs["code"] = code
    con = await async_searcher(base_url, post=True, json=kwargs, re_content=True)
    if not download:
        file = BytesIO(con)
        file.name = file_name + ".jpg"
    else:
        file = file_name + ".jpg"
        open(file_name, "wb").write(con)
    return file
