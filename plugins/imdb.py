from utils import get_poster
from info import IMDB_TEMPLATE
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty

def listToString(s):
 str1 = " "
 return (str1.join(s))

async def searchIMDb(query):
    imdb = await get_poster(query)
    try:
        Id = imdb['imdb_id']
        return imdb
    except TypeError:
        imdb = await searchIMDb(query)
        return imdb

@Client.on_message(filters.command("rimdb"))
async def imdb_search(client, message):
    
    await message.delete()
    data = listToString(message.command[1:]).split('|')
    title = data[0]
    qualities = data[1]
    languages = data[2]
    imdb = await searchIMDb(pata)

    reply_markup = InlineKeyboardMarkup(
       [
           [
                InlineKeyboardButton(
                    text=f"📥 {imdb['title']}",
                    url=f"https://hagadmansa.com/movies/{imdb['title']}".replace(' ', '-')
                )
            ]
        ]
    )

    fcaption = IMDB_TEMPLATE.format(
            title = imdb['title'],
            votes = imdb['votes'],
            aka = imdb["aka"],
            seasons = imdb["seasons"],
            box_office = imdb['box_office'],
            localized_title = imdb['localized_title'],
            kind = imdb['kind'],
            imdb_id = imdb["imdb_id"],
            cast = imdb["cast"],
            runtime = imdb["runtime"],
            countries = imdb["countries"],
            certificates = imdb["certificates"],
            languages = imdb["languages"],
            director = imdb["director"],
            writer = imdb["writer"],
            producer = imdb["producer"],
            composer = imdb["composer"],
            cinematographer = imdb["cinematographer"],
            music_team = imdb["music_team"],
            distributors = imdb["distributors"],
            release_date = imdb['release_date'],
            year = imdb['year'],
            genres = imdb['genres'],
            poster = imdb['poster'],
            plot = imdb['plot'],
            rating = imdb['rating'],
            url = imdb['url']
    )
    
    caption = fcaption + f"\n**📂 Qualities** - {qualities}\n**🗣 Languages** - {languages}"
        
    try:
        await message.reply_photo(
            photo = imdb['poster'],
            caption = caption,
            reply_markup = reply_markup
        )
    except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb['poster']
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            await message.reply(
                photo = poster,
                caption = caption,
                reply_markup = reply_markup
            )
    except Exception:
            await message.reply_photo(
            photo = "https://telegra.ph/file/3e5e63094d28f9c870a8b.jpg",
            caption = caption,
            reply_markup = reply_markup
        )
