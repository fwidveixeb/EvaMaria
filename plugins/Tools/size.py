"""from PIL import Image
from pyrogram import Client, filters

@Client.on_message(filters.command("size"))
async def suze(bot, message):
  
  
    r = await e.get_reply_message()
    if not (r and r.media):
        return await e.eor(get_string("ascii_1"))
    k = await e.eor(get_string("com_1"))
    if hasattr(r.media, "document"):
        img = await e.client.download_media(r, thumb=-1)
    else:
        img = await r.download_media()
    im = Image.open(img)
    x, y = im.size
    await k.edit(f"Dimension Of This Image Is\n`{x} x {y}`")
    os.remove(img)"""
