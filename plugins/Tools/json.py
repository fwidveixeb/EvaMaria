import io
from pyrogram import Client, filters

@Client.on_message(filters.command("json"))
async def json(bot, message):
  
    json = await message.reply("`Processing...`")
    replied = message.reply_to_message
    lomu = None
    
    if replied:
        lomu = replied.stringify()
    else:
        lomu = message.stringify()
        
    if len(lomu) > 4096:
        with io.BytesIO(str.encode(lomu)) as out_file:
            out_file.name = f"json_{message.chat.id}.text"
            await reply_document(
              document=f"json_{message.chat.id}.text",
              caption="Here is your JSON data.",
              thumb="resources/dovoloper.png"
            ) 
            return await json.delete()
    else:
        await json.edit(lomu)
