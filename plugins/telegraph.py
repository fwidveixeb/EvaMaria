import os
import shutil
from pyrogram import Client, filters
from telegraph import upload_file
from pyrogram.types import Message
from pyrogram.types.messages_and_media import message

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

DOWNLOAD = "downloads/"

@Client.on_message(filters.command("telegraph"))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("Reply to a supported media file.")
        return
    file_info = get_file_id(replied)
    if not file_info:
        await message.reply_text("Not supported!")
        return
    _t = os.path.join(DOWNLOAD, str(replied.message_id))
    if not os.path.isdir(_t):
        os.makedirs(_t)
    _t += "/"
    download_location = await replied.download(_t)
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply_text(message, text=document)
    else:
        await message.reply(
            f"https://telegra.ph{response[0]}", disable_web_page_preview=True
        )
    finally:
        shutil.rmtree(_t, ignore_errors=True)
