import requests
from bs4 import BeautifulSoup as bs
from pyrogram import Client, filters

@Client.on_message(filters.command("github"))
async def github(bot, message):
  
  gh = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
    return await gh.edit("No Username provided for GitHub, Read Help Menu to know how command works.")
  
  elif len(message.command) == 2:
    username = message.command[1]
    try:
       github = requests.get(f"https://api.github.com/users/{username}").json()
       photo = github["avatar_url"]
       link = github["html_url"]
       name = github["name"]
       acctype = github["type"]
       company = github["company"]
       blog = github["blog"]
       location = github["location"]
       email = github["email"]
       bio = github["bio"]
       twitter = github["twitter_username"]
       repo = github["public_repos"]
       gist = github["public_gists"]
       followers = github["followers"]
       following = github["following"]
       joined = github["created_at"]
       d_username = username.capitalize() 
       output = f"""**USER DETAILS**
**Name:** `{name}`
**Bio:** `{bio}`
**Email:** `{email}`
**Company:** `{company}`
**Blog:** `{blog}`
**Location:** `{location}`
**Type:** `{acctype}`
**Followers:** `{followers}`
**Following:** `{following}`
**Twitter Username:** `{twitter}`
**No of Public Repos:** `{repo}`
**No of Public Gists:** `{gist}`
**Joined Date:** `{joined}`
**View more at Github:** [{d_username}]({link})
""" 
       await message.reply_photo(photo=photo, caption=output)
       await gh.delete()
    except Exception as e:
       print(e)
       await gh.edit(f"**COMMAND:**\n`{message.text}`\n\n**ERROR:**\n`Hagadmansa Says: [173 USERNAME_NOT_FOUND] - The Username you provided is not found on Github, provide a valid username.`")
  else:
      await gh.edit("Argument limit exceeded, Read Help Menu to know how command works.")
