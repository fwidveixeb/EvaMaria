<h1 align="center">
  <b>Eva Maria Bot</b>
</h1>

## Features

- [x] Auto Filter
- [x] Manual Filter
- [x] IMDB
- [x] Admin Commands
- [x] Broadcast
- [x] Index
- [x] IMDB search
- [x] Inline Search
- [x] Random pics
- [x] ids and User info 
- [x] Stats, Users, Chats, Ban, Unban, Leave, Disable, Channel
- [x] Spelling Check Feature
- [x] File Store
## Variables

### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.
* `PICS`: Telegraph links of images to show in start message.( Multiple images can be used separated by space )
### Optional Variables
* `FILE_STORE_CHANNEL`: Channel from were file store links of posts should be made.Separate multiple IDs by space
* `IMDB_TEMPLATE`: To [Customize](https://t.me/TeamEvamaria/9) imdb data.
* `SUPPORT_CHAT`: Add your own chat as a support chat instead of [@hagadmansachat](https://t.me/hagadmansachat).
* `P_TTI_SHOW_OFF`: (Use True or False) - If True users will be redirected to send /start to Bot PM. else files will be sent directly to users PM.
* `IMDB`: (Use True or False) - To disable or enable imdb data.
* `SINGLE_BUTTON`: (Use True or False) - If set True, file name and files size will be shown in a single button instead of two separate button.
* `CUSTOM_FILE_CAPTION`: Same as IMDB template , you can customize the caption for files  (available keys , file_name, file_size, file_caption ) <br> Example: File Name - {file_name} File Size - {file_size} X Join my channel [@hagadmansa](https://t.me/hagadmansa) or visit my website www.hagadmansa.com  
* `LONG_IMDB_DESCRIPTION`: (Use True or False) Long IMDB story line will be used if enabled.
* `SPELL_CHECK_REPLY`: (Use True or False) - if enabled, bot will be suggesting related movies if keyword not found in database.
* `MAX_LIST_ELM`: long lists like long casts list can be shortened using this value. list will be shortened to first n elements where n is the value for this config var. For example if 4 is used list will be shortened to foist 4 elements.
* `AUTH_CHANNEL`: To enable force subscribe (make sure bot is admin in `AUTH_CHANNEL`). Delete this var if you do not need fsub.
* `AUTH_USERS`: To restrict the use of inline queries to specified users.
* `UPSTREAM_REPO`: If you want to use a customized fork of [EvaMaria](https://github.com/hagadmansa/EvaMaria), You can fill this config with github url of your fork.
* `BATCH_FILE_CAPTION`: Same as `CUSTOM_FILE_CAPTION`, use in case you want separate captions for batch files.
* `MELCOW_NEW_USERS`: Use False if you want the bot to not to welcome new users in groups.
* `PROTECT_CONTANT`: Use True/False . If set to true files from bot cannot be forwarded to any chat.
* `PUBLIC_FILE_STORE`: Use False if you don't want your bot to be used as a filestore bot by others.
* Check [info.py](https://github.com/hagadmansa/evamaria/blob/master/info.py) for more


## Deploy

[![YouTube](https://img.shields.io/badge/YouTube-Video%20Tutorial-red?logo=youtube)](https://youtu.be/1G1XwEOnxxo)

### Deploy To Heroku
<p>
<br>
<a href="https://heroku.com/deploy?template=https://github.com/bakrapalan/AutoForwardBot">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>
<p>
<pre>
git clone https://github.com/Hagadmansa/evamaria
# Install Packages
pip3 install -U -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>

## Commands
```
• /logs - to get the rescent errors
• /stats - to get status of files in db.
* /filter - add manual filters
* /filters - view filters
* /connect - connect to PM.
* /disconnect - disconnect from PM
* /del - delete a filter
* /delall - delete all filters
* /deleteall - delete all index(autofilter)
* /delete - delete a specific file from index.
* /info - get user info
* /id - get tg ids.
* /imdb - fetch info from imdb.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids 
• /index  - to add files from a channel
• /leave  - to leave from a chat.
• /disable  -  do disable a chat.
* /enable - re-enable chat.
• /ban  - to ban a user.
• /unban  - to unban a user.
• /channel - to get list of total connected channels
• /broadcast - to broadcast a message to all Eva Maria users
• /batch - to create link for multiple posts
• /link - to create link for one post
```
## Support
[![telegram badge](https://img.shields.io/badge/Telegram-Group-30302f?style=flat&logo=telegram)](https://t.me/hagadmansachat)
[![telegram badge](https://img.shields.io/badge/Telegram-Channel-30302f?style=flat&logo=telegram)](https://t.me/hagadmansa)

## Credits 
* [![EvaMaria-Devolopers](https://img.shields.io/static/v1?label=EvaMaria&message=Devolopers&color=critical)](https://t.me/EvaMariaDevs)


## Thanks to 
 - Thanks To [Dan](https://github.com/pyrogram) For His Awesome [Library](https://github.com/pyrogram/pyrogram)
 - Thanks To [Mahesh](https://github.com/Mahesh0253) For His Awesome [Media-Search-bot](https://github.com/Mahesh0253/Media-Search-bot)
 - Thanks To [Trojanz](https://github.com/trojanzhex) for Their Awesome [Unlimited Filter Bot](https://github.com/TroJanzHEX/Unlimited-Filter-Bot) And [AutoFilterBoT](https://github.com/trojanzhex/auto-filter-bot)
 - Thanks To All Everyone In This Journey

## Disclaimer
[![GNU Affero General Public License 2.0](https://www.gnu.org/graphics/agplv3-155x51.png)](https://www.gnu.org/licenses/agpl-3.0.en.html#header)    
Licensed under [GNU AGPL 2.0.](https://github.com/EvamariaTG/evamaria/blob/master/LICENSE)
Selling The Codes To Other People For Money Is *Strictly Prohibited*.

## Inspiration
This is an attempt to create a clone of a BOAT made out of [banana trees 🌳](https://t.me/GetTGLink/4187)

