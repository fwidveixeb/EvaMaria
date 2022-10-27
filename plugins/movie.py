import mongo, helper, asyncio, traceback
from pyrogram import filters, Client as bot

@bot.on_message(filters.command('addmovie'))
async def addMovie(bot, message):
    try:
        if len(message.command) == 1:
            return await message.reply("Give me movie name to add in upcomingList, if more than one, seperated by '|'.")
        added = mongo.addMovieToUpcomingList(message.text[10::])
        await helper.updateStatusMessage(bot)
        if added == 0:
            return await message.reply(f"No movies added in upcomingList because these movies are already added.")
        else:
            return await message.reply(f"Successfully added {added} movies to upcomingList.")
    except Exception as e:
        return await message.reply(f"**Traceback Info:**\n`{traceback.format_exc()}`\n**Error Text:**\n`{e}`")
    
@bot.on_message(filters.command('givemovie'))
async def giveMovie(bot, message):
    try:
        movie, year = mongo.giveMovie()
        if movie == "Permission Denied":
            return await message.reply("Permission Denied.")
        if year == "":
            return await message.reply("No movies left in upcomingList.")
        return await message.reply(f".upload {movie} {year}")
    except Exception as e:
        return await message.reply(f"**Traceback Info:**\n`{traceback.format_exc()}`\n**Error Text:**\n`{e}`")
    
@bot.on_message(filters.command('maintenance'))
async def maintenanceCommand(bot, message):
    try:
        if len(message.command) == 1:
            mode = list(mongo.variables.find({}, {"_id": 0, "maintenanceMode": 1}))[0]["maintenanceMode"]
            return await message.reply(f"Maintenance mode is now **{mode.title()}**.")
        if message.command[1].lower() == "on":
            mongo.maintenanceMode("on")
            await message.reply(f"Maintenance mode is now **On**.")
        elif message.command[1].lower() == "off":
            mongo.maintenanceMode("off")
            await message.reply(f"Maintenance mode is now **Off**.")
        else:
            await message.reply("Sorry, I couldn't understand your command.")
    except Exception as e:
        return await message.reply(f"**Traceback Info:**\n`{traceback.format_exc()}`\n**Error Text:**\n`{e}`")
    
@bot.on_message(filters.command('fastupload'))
async def fastUpload(bot, message):
    try:
        if len(message.command) == 1:
            return await message.reply("Give me a movie name whom to upload first.")
        query = helper.listToString(message.command[1:])
        mata = [x for x in mongo.upcomingMovies.find({}, {"_id":0, "movieName": 1, "releaseYear": 1})]
        sata = [x for x in mongo.uploadedMovies.find({}, {"_id":0, "movieName": 1, "releaseYear": 1})]
        if {"movieName": query[:len(query)-5], "releaseYear": query[-4:]} in sata:
            return await message.reply(f"This movie is already uploaded on website.")
        if {"movieName": query[:len(query)-5], "releaseYear": query[-4:]} in mata:
            mongo.shift(query)
            await helper.updateStatusMessage(bot)
            return await message.reply(f"This movie was already in upcoming list, but i've changed it's position.")
        mongo.fastUpload(query)
        movie = mongo.variables.find({}, {"_id":0, "petrionaUploading": 1, "files": 1})[0]["petrionaUploading"]
        if movie == "false":
            await message.reply(f"I'll be uploading **{query[:len(query)-5]} ({query[-4:]})** on next command.")
        else:
            await message.reply(f"I'll be uploading **{query[:len(query)-5]} ({query[-4:]})** after **{movie}**.")
        return await helper.updateStatusMessage(bot)
    except Exception as e:
        return await message.reply(f"**Traceback Info:**\n`{traceback.format_exc()}`\n**Error Text:**\n`{e}`")
       
@bot.on_message(filters.command('shift'))
async def shift(bot, message):
    try:
        if len(message.command) == 1:
            return await message.reply("Give me a movie name whom to shift first.")
        query = helper.listToString(message.command[1:])
        mata = [x for x in mongo.upcomingMovies.find({}, {"_id":0, "movieName": 1, "releaseYear": 1})]
        if {"movieName": query[:len(query)-5], "releaseYear": query[-4:]} not in mata:
            mongo.fastUpload(query)
            await helper.updateStatusMessage(bot)
            return await message.reply(f"This movie was not in upcoming List, but now i've added at 1st position.")
        mongo.shift(query)
        movie = mongo.variables.find({}, {"_id":0, "petrionaUploading": 1, "files": 1})[0]["petrionaUploading"]
        if movie == "false":
            await message.reply(f"I'll be uploading **{query[:len(query)-5]} ({query[-4:]})** on next command.")
        else:
            await message.reply(f"I'll be uploading **{query[:len(query)-5]} ({query[-4:]})** after **{movie}**.")
        return await helper.updateStatusMessage(bot)
    except Exception as e:
        return await message.reply(f"**Traceback Info:**\n`{traceback.format_exc()}`\n**Error Text:**\n`{e}`")
    
@bot.on_message(filters.command('remmovie'))
async def remMovie(bot, message):
    try:
        if len(message.command) == 1:
            return await message.reply("Give me a movie whom to remove from upcoming List.")
        query = helper.listToString(message.command[1:])
        mata = [x for x in mongo.upcomingMovies.find({}, {"_id":0, "movieName": 1, "releaseYear": 1})]
        if {"movieName": query[:len(query)-5], "releaseYear": query[-4:]} not in mata:
            return await message.reply(f"This movie is not in upcoming List, how do i remove it?")
        mongo.removeMovieFromUpcomingList(query)
        await message.reply(f"I've removed **{query[:len(query)-5]} ({query[-4:]})** from upcoming list.")
        return await helper.updateStatusMessage(bot)
    except Exception as e:
        return await message.reply(f"**Traceback Info:**\n`{traceback.format_exc()}`\n**Error Text:**\n`{e}`")
    
@bot.on_message(filters.command('deletemovie'))
async def deleteMovie(bot, message):
    try:
        if len(message.command) == 1:
            return await message.reply("Give me a movie whom to remove from website.")
        response = await message.reply("Processing")
        query = helper.listToString(message.command[1:])
        mata = [x for x in mongo.uploadedMovies.find({}, {"_id":0, "movieName": 1, "releaseYear": 1})]
        if {"movieName": query[:len(query)-5], "releaseYear": query[-4:]} not in mata:
            return await response.edit(f"This movie is not uploaded on website yet, how do i remove it?")
        pata = mongo.uploadedMovies.find_one({"movieName": query[:len(query)-5], "releaseYear": query[-4:]})["_id"]
        await response.edit("Deleting from Database...")
        mongo.removeMovieFromUploadedMovies(pata)
        await response.edit("Deleting from Website...")
        await helper.deleteMovie(query[:len(query)-5])
        await response.edit(f"I've deleted **{query[:len(query)-5]} ({query[-4:]})** from Database and Website.")
        return await helper.updateStatusMessage(bot)
    except Exception as e:
        return await response.edit(f"**Traceback Info:**\n`{traceback.format_exc()}`\n**Error Text:**\n`{e}`")
    
@bot.on_message(filters.command('status'))
async def statusMessage(bot, message):
    try:
        await message.delete()
        if message.reply_to_message:
            statusMessage = await helper.sendStatusMessage(message, message.reply_to_message.id)
        else:
            statusMessage = await helper.sendStatusMessage(message)
        Id = mongo.searchStatusMessageId()
        try:
            await bot.delete_messages(
                chat_id=message.chat.id,
                message_ids=int(Id)
            )
        except Exception as e:
            print(e)
        mongo.updateStatusMessageId(statusMessage.id)
        return await helper.updateStatusMessage(bot)
    except Exception as e:
        return await message.reply(f"**Traceback Info:**\n`{traceback.format_exc()}`\n**Error Text:**\n`{e}`")
    
@bot.on_message(filters.command('request'))
async def request(bot, message):
    try:
        await message.delete()
        requests = ""
        if len(message.command) == 1:
            return await message.reply("Give me a movie name to add in requests.")
        mongo.addInUserRequests(helper.listToString(message.command[1::]))
        msg = await message.reply(
            text=f"I've added **{helper.listToString(message.command[1::])}** to requests!"
        )
        await asyncio.sleep(10)
        return await msg.delete()
    except Exception as e:
        return await message.reply(f"**Traceback Info:**\n`{traceback.format_exc()}`\n**Error Text:**\n`{e}`")

@bot.on_message(filters.command('requests'))
async def requests(bot, message):
    try:
        await message.delete()
        if len(message.command) != 1 and message.command[1] in ['c', 'clear']:
            mongo.userRequests.drop()
            return await message.reply("All Requests Cleared!")
        else:
            requests = ""
            chata = [x for x in mongo.userRequests.find({}, {"_id":0, "movie": 1})]
            for x in range(len(chata)):
                requests += f"**{x+1}:** {chata[x]['movie']}\n" 
            if len(requests) == 0:
                requests = "No Requests!"
        msg = await message.reply(requests)
        await asyncio.sleep(30)
        return await msg.delete()
    except Exception as e:
        return await message.reply(f"**Traceback Info:**\n`{traceback.format_exc()}`\n**Error Text:**\n`{e}`")
    
