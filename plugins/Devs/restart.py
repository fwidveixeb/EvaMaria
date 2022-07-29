import time
import heroku3
import asyncio
from Vars import Var
from info import ADMINS
from pyrogram import Client, filters

HEROKU_API_KEY = Var.HEROKU_API_KEY
HEROKU_APP_NAME = Var.HEROKU_APP_NAME

heroku = heroku3.from_key(HEROKU_API_KEY)
app = heroku.app(HEROKU_APP_NAME)

@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def restart_bot(bot, message):
  
  tm = time.localtime()
  c_time = time.strftime("%H:%M:%S", tm)
  f_time = c_time.split(':')
  
  
  await message.reply(f"Sent for Restart at {c_time}, Check back in a minute.")
  app.restart()
