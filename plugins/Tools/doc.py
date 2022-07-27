import os
from pyrogram import Client, filters

@Client.on_message(filters.command("doc"))
async def doc(bot, message):
  
  doc = await message.reply("`Processing...`")
  replied = message.reply_to_message
  
  if not replied.text:
    return await doc.edit("Reply to a text.")
    
  if (message.command):
    pk = message.text.split()
    kp = pk[1]
    if not pk:
      return await doc.edit("Pass a file name along with the command.")
    print(kp)
  
  with open(kp, "w") as b:
    b.write(str(replied.text))
  await doc.edit(f"Packing into `{input_str}`")
  await message.reply_document(document=pk, caption=f"Successfully Packed into `{input_str}`", thumb="resources/devoloper.png")
  await doc.delete()
  os.remove(kp)
