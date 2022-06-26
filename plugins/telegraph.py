import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from sample_config import Config
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery)

@Client.on_message(filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("Trying to download the photo...")
  userid = str(message.chat.id)
  img_path = (f"./DOWNLOADS/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("Now trying to Upload it on Telegra.ph.")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("Something went wrong") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
    os.remove(img_path) 
