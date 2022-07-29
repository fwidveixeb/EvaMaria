from shutil import rmtree
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from plugins.Helper.google_image import googleimagesdownload

def listToString(s):
    str1 = " "
    return (str1.join(s))

@Client.on_message(filters.command("img"))
async def img(bot, message):
 
    img = await message.reply("`Processing...`")
    
    if len(message.command) == 1:
      return await img.edit("No query provided to search, Read Help Menu to know how command works.")
       
    elif len(message.command) > 1:
      query = message.command[1:]
      hemlo = query[0]
      limit = 5
      if ";" in query:
        try:
            query = query.split(";")[0]
            limit = int(query.split(";")[1])
        except BaseException:
            pass
      
      ggl = googleimagesdownload()
      args = {
          "keywords": query,
          "limit": limit,
          "format": "jpg",
          "output_directory": "./resources/",
      }
      path = await ggl.download(args)
      s = [InputMediaPhoto(path[0][hemlo][0]), InputMediaPhoto(path[0][hemlo][1]), InputMediaPhoto(path[0][hemlo][2]), InputMediaPhoto(path[0][hemlo][3]), InputMediaPhoto(path[0][hemlo][4])]
      await message.reply_media_group(media=s)
      rmtree(f"./resources/{hemlo}/")
      await img.delete()
      
    else:
      return await img.edit("Parameter limit exceeded, Read Help Menu to know how command works.")
