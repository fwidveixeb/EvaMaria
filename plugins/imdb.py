from utils import get_poster
from info import IMDB_TEMPLATE
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def listToString(s):
 str1 = " "
 return (str1.join(s))

@Client.on_message(filters.command("imdb"))
async def imdb_search(client, message):
    
    await message.delete()
    data = message.command[1:]
    pata = listToString(data)
    
    imdb = await get_poster(pata)
    title = imdb['title']
    p = imdb['poster']

    btn = InlineKeyboardMarkup(
       [
           [
                InlineKeyboardButton(
                    text=f"📥 {title}",
                    url=f"https://hagadmansa.com/movies/{title}".replace(' ', '-')
                )
            ]
        ]
    )

    c = IMDB_TEMPLATE.format(
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
        
    await message.reply_photo(photo=p, caption=c, reply_markup=btn)
