from pyrogram import Client, filters
from plugins.Helper.async_searcher import async_searcher

@Client.on_message(filters.command("ip"))
async def ip(bot, message):
  
  ip = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
    return await dagd.edit("No IP Address provided, Read Help Menu to know how command works")
  
  elif len(message.command) == 2:
    ipp = message.command[1]
    mota = await async_searcher(f"https://ipinfo.io{ipp}/geo", re_json=True)
    try:
        err = mota["error"]["title"]
        msg = mota["error"]["message"]
        return await ip.edit(f"Error = {err}/nMessage = {msg}")
    except:
        pass
    ipa = mota["ip"]
    city = mota["city"]
    region = mota["region"]
    country = mota["country"]
    cord = mota["loc"]
    try:
        zipc = mota["postal"]
    except KeyError:
        zipc = "None"
    tz = mota["timezone"]
    data = f"""**IP Details Fetched**

**IP:** `{ipa}`
**City:** `{city}`
**Region:** `{region}`
**Country:** `{country}`
**Co-ordinates:** `{cord}`
**Postal Code:** `{zipc}`
**Time Zone:** `{tz}`
"""
    return await ip.edit(data)
  else:
    await ip.edit("Parameter limit exceeded, Read Help Menu to know how command works.")  
