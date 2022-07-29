from htmlwebshot import WebShot
from pyrogram import Client, filters
from plugins.Helper.url_checker import is_url_ok

@Client.on_message(filters.command("webss"))
async def webss(bot, message):
  
  webss = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
    return await webss.edit("No URL provided to take Screenshot, Read Help Menu to know how command works.")
  
  elif len(message.command) == 2:
    xurl = message.command[1]
    if not is_url_ok(xurl):
      return webss.edit("Invalid URL Provided.")
    
    shot = WebShot(quality=88, flags=["--enable-javascript", "--no-stop-slow-scripts"])
    pic = await shot.create_pic_async(url=xurl)
    await message.reply_document(document=pic, thumb="resources/devoloper.png", caption=f"**Here is the Screenshot of** `{xurl}`")
    os.remove(pic)
    await webss.delete()
  else: 
    await webss.edit("Parameter limit exceeded, Read Help Menu to know how command works.")  
