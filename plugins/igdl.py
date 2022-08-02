import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("igdl"))
async def igdl(bot, message):
  
  ig = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
      return await ig.edit("No URL provided to download, Read Help Menu to know how command works")
  
  elif len(message.command) == 2:
      tk = message.text.split("/")
      pk = message.text.split()
      nk = pk[1]
      uk = nk.split("/")
      url = uk[0] + "//" + uk[2] + "/" + uk[3] + "/" + uk[4]
      if tk[4] == "reel":
          out = requests.get(f"https://open-apis-rest.up.railway.app/api/instareel?url={url}").json()
          try:
              reel = out["data"]["data"]["url"]
          except:
              return await ig.edit("API didn't responded, please report it at @HagadmansaChat or try again later.")
          await message.reply_video(video=reel, caption="Here is your reel.")
          return await ig.delete()
      elif tk[4] == "p":
          return await ig.edit("Photos Downloader will be added soon, Currently only Reels Downloader available.")
      elif tk[4] == "tv":
          return await ig.edit("IGTV Downloader will be added soon, Currently only Reels Downloader available.")
      else:
          return await ig.edit("The URL you provided is neither reel, nor igtv nor post, therefore i can't process it. If you are right please report this at @HagadmansaChat.")
  else:
      await ig.edit("Parameter limit exceeded, Read Help Menu to know how command works.")
