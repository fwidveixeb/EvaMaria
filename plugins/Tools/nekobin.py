import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("nekobin"))
async def nekobin(bot, message):
  
  nb = await message.reply("`Processing...`")
  replied = message.reply_to_message
  
  if not replied:
    return await nb.edit(text="Reply to a Text or file to upload it on Nekobin, Read Help Menu to know how command works.", disable_web_page_preview=True)
  
  if replied.text:
    hemlo = requests.get(f"https://open-apis-rest.up.railway.app/api/nekobin?text={replied.text}").json()
    url = hemlo["data"]["url"]
    return await nb.edit(text=f"Given text is successfully pasted on [Nekobin]({url}).", disable_web_page_preview=True)
  
  if replied.document:
     if replied.document.file_size > 5242880:
        return await nb.edit("Replied file must be less then 5 Mb.")
     try:
        down = await bot.download_media(replied)
        with open(down) as a:  
           msg = a.read()
           os.remove(down)
     except:
        return await nb.edit("Reply only to a Text file only, Read Help Menu to know how command works.")
     hemlo = requests.get(f"https://open-apis-rest.up.railway.app/api/nekobin?text={msg}").json()
     url = hemlo["data"]["url"]
     return await nb.edit(text=f"Given file is successfully pasted on [Nekobin]({url}).", disable_web_page_preview=True)
  await nb.edit("Reply only to a Text or file, Read Help Menu to know how command works.")
