import os
from pyrogram import Client, filters
from plugins.Helper.rmbg import RemoveBG

@Client.on_message(filters.command("rmbg"))
async def rmbg(bot, message):
  
  rmbg = await message.reply("`Processing...`")
  replied = message.reply_to_message

  if not replied:
      return await rmgb.edit("Reply to a photo to Remove it's Backgroud, Read Help Menu to know how command works.")

  if replied.photo:
      photo = await bot.download_media(replied)
      dn, out = await RemoveBG(photo)
      os.remove(photo)
      if not dn:
          dr = out["errors"][0]
          de = dr.get("detail", "")
          return await rmbg.edit(f"**ERROR ~** `{dr['title']}`,\n`{de}`")
      await message.reply_photo(photo=out, caption="Here is your Image without Backgroud")
      await rmbg.delete()
      return os.remove(out)
  await rmbg.edit("Reply only to a photo to Remove it's Background, Read Help Menu to know how command works.")
