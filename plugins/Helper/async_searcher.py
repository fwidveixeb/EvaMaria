import aiohttp

async def async_searcher(
    url: str,
    post: bool = None,
    headers: dict = None,
    params: dict = None,
    json: dict = None,
    data: dict = None,
    ssl=None,
    re_json: bool = False,
    re_content: bool = False,
    real: bool = False,
    *args,
    **kwargs,
):
    try:
        import aiohttp
    except ImportError:
        raise DependencyMissingError(
            "'aiohttp' is not installed!\nthis function requires aiohttp to be installed."
        )
    async with aiohttp.ClientSession(headers=headers) as client:
        if post:
            data = await client.post(
                url, json=json, data=data, ssl=ssl, *args, **kwargs
            )
        else:
            data = await client.get(url, params=params, ssl=ssl, *args, **kwargs)
        if re_json:
            return await data.json()
        if re_content:
            return await data.read()
        if real:
            return data
        return await data.text()
