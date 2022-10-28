from struct import pack
from typing import Any, Optional
import glob, mongo, base64, random
from pyrogram.file_id import FileId
from pyrogram.errors.exceptions.bad_request_400 import MessageNotModified

abcd = "abcdefghijklmnopqrstuvwxyz"
ABCD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"

def listToString(data):
    return " ".join(data)

async def sendStatusMessage(message, messageId=None):
    upcoming = ""
    uploading = ""
    chata = [x for x in mongo.upcomingMovies.find({}, {"_id":0, "movieName": 1, "releaseYear": 1})]
    now = list(mongo.variables.find({}, {"_id":0, "petrionaUploading": 1, "files": 1}))
    mode = list(mongo.variables.find({}, {"_id":0, "maintenanceMode": 1}))[0]["maintenanceMode"]
    for x in range(len(now)):
        if now[x]["petrionaUploading"] == "false":
            uploading += ""
        else:
            uploading += f"**{x+1}:** {now[x]['petrionaUploading']} [{now[x]['files']} Qualities]\n"
    for x in range(len(chata)):
        upcoming += f"**{x+1}:** {(chata[x]['movieName']).title()} ({chata[x]['releaseYear']})\n"   
    if len(uploading) == 0:
        uploading = "No Uploads!\n"
    if mode == "on" and uploading == "No Uploads!\n":
        uploading = "Maintenance Mode Enabled!\n"
    if len(upcoming) == 0:
        upcoming = "No Upcoming!"
    return await message.reply(
        text=f"**Current Uploading**\n{uploading}\n**Upcoming Uploads**\n{upcoming}",
        reply_to_message_id=messageId
    )

async def updateStatusMessage(bot):
    upcoming = ""
    uploading = ""
    chata = [x for x in mongo.upcomingMovies.find({}, {"_id":0, "movieName": 1, "releaseYear": 1})]
    now = list(mongo.variables.find({}, {"_id":0, "petrionaUploading": 1, "files": 1}))
    mode = list(mongo.variables.find({}, {"_id":0, "maintenanceMode": 1}))[0]["maintenanceMode"]
    for x in range(len(now)):
        if now[x]["petrionaUploading"] == "false":
            uploading += ""
        else:
            uploading += f"**{x+1}:** {now[x]['petrionaUploading']} [{now[x]['files']} Qualities]\n"
    for x in range(len(chata)):
        upcoming += f"**{x+1}:** {(chata[x]['movieName']).title()} ({chata[x]['releaseYear']})\n"   
    if len(uploading) == 0:
        uploading = "No Uploads!\n"
    if mode == "on" and uploading == "No Uploads!\n":
        uploading = "Maintenance Mode Enabled!\n"
    if len(upcoming) == 0:
        upcoming = "No Upcoming!"
    try:
        await bot.edit_message_caption(
            chat_id="Hagadmansa",
            message_id=2,
            text=f"**Current Uploading**\n{uploading}\n**Upcoming Uploads**\n{upcoming}"
        )
    except MessageNotModified:
            pass
#     except PeerIdInvalid:
#         msg = await bot.send_message(
#             chat_id=HAGADMANSA_LOG,
#             text="Demo Text"
#         )
#         await msg.delete()
#         try:
#             await bot.edit_message_text(
#                 chat_id="Hagadmansa",
#                 message_id=1579,
#                 text=f"**Current Uploading**\n{uploading}\n**Upcoming Uploads**\n{upcoming}"
#             )
#         except MessageNotModified:
#             pass

def randomName():
    name = random.choice(abcd) + random.choice(numbers) + random.choice(ABCD) + random.choice(abcd) + random.choice(numbers) + random.choice(ABCD) 
    return name

def encode_file_id(s: bytes) -> str:
    r = b""
    n = 0

    for i in s + bytes([22]) + bytes([4]):
        if i == 0:
            n += 1
        else:
            if n:
                r += b"\x00" + bytes([n])
                n = 0

            r += bytes([i])

    return base64.urlsafe_b64encode(r).decode().rstrip("=")

def encode_file_ref(file_ref: bytes) -> str:
    return base64.urlsafe_b64encode(file_ref).decode().rstrip("=")

def getNew(new_file_id):
    """Return file_id, file_ref"""
    decoded = FileId.decode(new_file_id)
    file_id = encode_file_id(
        pack(
            "<iiqq",
            int(decoded.file_type),
            decoded.dc_id,
            decoded.media_id,
            decoded.access_hash
        )
    )
    file_ref = encode_file_ref(decoded.file_reference)
    return file_id, file_ref

def fileId(message: "Message") -> Any:
    media_types = (
        "audio",
        "document",
        "photo",
        "sticker",
        "animation",
        "video",
        "voice",
        "video_note",
    )
    for attr in media_types:
        media = getattr(message, attr, None)
        if media:
            return media.file_id
        
def fileName(message: "Message") -> Any:
    media_types = (
        "audio",
        "document",
        "photo",
        "sticker",
        "animation",
        "video",
        "voice",
        "video_note",
    )
    for attr in media_types:
        media = getattr(message, attr, None)
        if media:
            return media.file_name
        
def fileSize(message: "Message") -> Any:
    media_types = (
        "audio",
        "document",
        "photo",
        "sticker",
        "animation",
        "video",
        "voice",
        "video_note",
    )
    for attr in media_types:
        media = getattr(message, attr, None)
        if media:
            return media.file_size
