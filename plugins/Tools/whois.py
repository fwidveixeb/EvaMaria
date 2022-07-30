import io, os
import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("whois"))
async def whois(bot, message):
  
  whois = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
    return await whois.edit("No URL provided to check Whois Details, Read Help Menu to know how command works")
  
  elif len(message.command) == 2:
    url = message.command[1]
    xurl = url.split('/')
    mlist = ["http:", "https:"]
    if xurl[0] in mlist:
      final = xurl[2]
      response = requests.get(f"https://da.gd/w/{final}").text
      if len(response) > 4096:
        with io.BytesIO(str.encode(response)) as out_file:
            out_file.name = f"whois_{message.chat.id}.text"
            await message.reply_document(document=out_file, thumb="resources/devoloper.png")
            await whois.delete()
            os.remove(f"whois_{message.chat.id}.text")
      else:
        await whois.edit(f"{response}")
    else:
      await whois.edit(f"URL must starts with http:// or https:// schema.")
  else:
    await whois.edit("Parameter limit exceeded, Read Help Menu to know how command works.")  
