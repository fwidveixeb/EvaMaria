import asyncio
from info import ADMINS
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("pin") & filters.user(ADMINS))
async def pin(_, message: Message):
    
    replied = message.reply_to_message
    
    if replied:
        try:
            chat = message.chat.id
            delm = message.message_id + 1
            await message.delete()
            await replied.pin(disable_notification=True)
            await Client.delete_messages(chat_id=chat, message_ids=delm)
    
        except Exception as e:
            await message.reply(f"#Error {e}")
    
    if not replied:
        await message.delete()
        k = await message.reply("Reply to a message to Pin it.")
        await asyncio.sleep(5)
        await k.delete()
        


@Client.on_message(filters.command("unpin") & filters.user(ADMINS))
async def unpin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()
