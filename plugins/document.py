from pyrogram import Client, filters
from telegraph import Telegraph

telegraph = Telegraph()
telegraph.create_account(short_name="Hagadmansa")

def listToString(s):
    str1 = " "
    return (str1.join(s))

@Client.on_message(filters.command("abcd"))
async def kdneidhd(bot, message):
  
  replied = message.reply_to_message
  
  if replied.document:
    path = (f"./DOWNLOADS/{message.chat.id}.txt")
    await bot.download_media(message=replied, file_name=path)
    k = open(path)
    p = k.read()
    if (message.command):
      pk = message.command[1:]
    else:
        pk = "Hagadmansa"
    if pk == "Hagadmansa":
        monu = "Hagadmansa"
    else:
        monu = listToString(pk)
    try:
      response = telegraph.create_page(title=f'{monu}', content=[f"{p}"], author_name="Hagadmansa", author_url="https://hagadmansa.com")
      await message.reply(f"Here is your link:\n\n{response['url']}", disable_web_page_preview=True)
      k.close()
    except Exception as e:
      await message.reply(f"{e}")
      await message.reply(f"{p}")
    
