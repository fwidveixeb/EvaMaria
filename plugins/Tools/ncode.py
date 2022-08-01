import os
import pygments
from pyrogram import Client, filters
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter

@Client.on_message(filters.command("ncode"))
async def ncode(bot, message):
  
  ncode = await message.reply("`Processing...`")
  replied = message.reply_to_message
  
  if replied.text:
      pygments.highlight(
          replied.text,
          Python3Lexer(),
          ImageFormatter(line_numbers=True),
          f"ncode_{message.chat.id}.png",
      )
      await message.reply_photo(
        photo=f"ncode_{message.chat.id}.png,
        caption="Here is your ncoded Image of given text"
      )
      os.remove(f"ncode_{message.chat.id}.png)
      return await ncode.delete()
  await ncode.edit("Reply to a text or a file to get a Image.")
