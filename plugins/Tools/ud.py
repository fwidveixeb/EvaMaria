from pyrogram import Client, filters
from plugins.Helper.async_searcher import async_searcher

@Client.on_message(filters.command("ud"))
async def ud(bot, message):
  
  ud = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
     return await ud.edit("No word provided to search on Urban Dictionary, Read Help Menu to know how command works")
    
  elif len(message.command) == 2:
    word = message.command[1]
    out = await async_searcher("http://api.urbandictionary.com/v0/define", params={"term": word}, re_json=True)
    try:
        out = out["list"][0]
    except IndexError:
        return await ud.edit(f"Nothing Found For Word `{word}`.")
    text = "**• Word: **`{}`\n**• Meaning: **`{}`\n**• Example: **__{}__".format(out["word"], out["definition"], out["example"])
    await ud.edit(text)
    
  else:
    await ud.edit("Parameter limit exceeded, Read Help Menu to know how command works.")
