import traceback
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def getBold(text): 
    output = text.replace('|', '\n').replace('1:', '<b>1:</b>').replace('2:', '<b>2:</b>').replace('3:', '<b>3:</b>').replace('4:', '<b>4:</b>').replace('5:', '<b>5:</b>').replace('6:', '<b>6:</b>').replace('7:', '<b>7:</b>').replace('8:', '<b>8:</b>').replace('9:', '<b>9:</b>').replace('10:', '<b>10:</b>').replace('11:', '<b>11:</b>').replace('12:', '<b>12:</b>').replace('13:', '<b>13:</b>').replace('14:', '<b>14:</b>').replace('15:', '<b>15:</b>')
    return output

@Client.on_message(filters.command('sendnotification'))
async def sendNotification(bot, message):
    try:
        if message.from_user.id not in [1250003833, 5099088450]:
            return
    
        chat_id = message.command[1]
        moviename = message.command[2]
        quality = message.command[3]
        await message.delete()
        
        hello = await bot.send_message(
            chat_id=chat_id,
            text=f"📤 Uploading **{moviename} [{quality} Qualities]** on website..."
        )
        
        await message.reply(hello.id)
    except Exception as e:
        txt = traceback.format_exc() 
        await message.reply(f"**Traceback Info:**\n`{txt}`\n**Error Text:**\n`{e}`")
        
@Client.on_message(filters.command('editnotification'))
async def editNotification(bot, message):
    try:
        if message.from_user.id not in [1250003833, 5099088450]:
            return
        
        chat_id = message.command[1]
        messageId = int(message.command[2])
        movie = message.command[3]
        moviename = message.command[4]
        quality = int(message.command[5])
        time = message.command[6]
        text = message.command[7]
        await message.delete()
        
        reply_markup = InlineKeyboardMarkup(  
            [
                [
                    
                    InlineKeyboardButton(
                        text = f"📥 {movie}",
                        url = f"https://hagadmansa.com/movies/{movie}".replace(' ', '-')
                    ) 
                ]
            ]
        )
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=messageId,
            text=f"✅ Successfully Uploaded **{moviename} [{str(quality)} Qualities]** on website in {time}.\n\n {getBold(text)}",
            reply_markup=reply_markup
        )
    except Exception as e:
        txt = traceback.format_exc() 
        await message.reply(f"**Traceback Info:**\n`{txt}`\n**Error Text:**\n`{e}`")   
        
@Client.on_message(filters.command('errornotification'))
async def errorNotification(bot, message):
    try:
        if message.from_user.id not in [1250003833, 5099088450]:
            return
    
        chat_id = message.command[1]
        messageId = int(message.command[2])
        movie = message.command[3]
        await message.delete()
        
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=messageId,
            text=f"❌ Something went wrong while uploading {movie} on website, contact Admin."
        )
    except Exception as e:
        txt = traceback.format_exc() 
        await message.reply(f"**Traceback Info:**\n`{txt}`\n**Error Text:**\n`{e}`")
