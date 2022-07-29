import heroku3
import asycnio
from Vars import Var
from info import ADMINS
from pyrogram import Client, Filters

@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def restart(bot, message):
  
  HEROKU_API_KEY = Var.HEROKU_API_KEY
  HEROKU_APP_NAME = Var.HEROKU_APP_NAME

  heroku = heroku3.from_key(HEROKU_API_KEY)
  app = heroku.app(HEROKU_APP_NAME)
  
  k = await message.reply("`Restarting Bot... This may take time depending on the server.`"
  await app.restart()
  await k.edit("Restarted Successfully, if I'm not working Check logs.") 
