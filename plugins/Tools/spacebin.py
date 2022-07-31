from pyrogram import Client, filters
from plugins.Helper.spacebin import get_paste
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command("spacebin"))
async def spacebin(bot, message):
  
  sb = await message.reply("`Processing...`")
  replied = message.reply_to_message
  
  if not replied:
    return await sb.edit(text="Reply to a Text or file to upload it on Spaceb.in, Read Help Menu to know how command works.", disable_web_page_preview=True)
  
  if replied.text:
    msg = replied.text
    done, key = await get_paste(msg)
    if not done:
        return await sb.edit(key)
    link = "https://spaceb.in/" + key
    raw = f"https://spaceb.in/api/v1/documents/{key}/raw"
    return await sb.edit(
      text="Given text is successfully pasted on Spaceb.in",
      disable_web_page_preview=True,
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Spacebin', url=link), InlineKeyboardButton(text='Raw Text', url=raw)]])
    )
  
  if replied.document:
     if replied.document.file_size > 5242880:
        return await sb.edit("Replied file must be less then 5 Mb.")
     try:
        down = await bot.download_media(replied)
        with open(down) as a:  
           msg = a.read()
           os.remove(down)
     except:
        return await sb.edit("Reply only to a Text file only, Read Help Menu to know how command works.")
     done, key = await get_paste(msg)
     if not done:
        return await sb.edit(key)
     link = "https://spaceb.in/" + key
     raw = f"https://spaceb.in/api/v1/documents/{key}/raw"
     return await sb.edit(
      text="Given text is successfully pasted on Spaceb.in",
      disable_web_page_preview=True,
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Spacebin', url=link), InlineKeyboardButton(text='Raw Text', url=raw)])
    )
  await sb.edit("Reply only to a Text or file, Read Help Menu to know how command works.")
