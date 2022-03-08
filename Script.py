class script(object):
    START_TXT = """👋 Hello {},
    
🤖 My Name is <a href=https://t.me/{}>{}</a>, I can provide you movies, Just visit my website <i><b>www.hagadmansa.com</b></i>. 

🧐 Don't know how to watch or download? No worry just <a href=https://t.me/hagadmansa/2>Click here</a> to watch a tutorial on YouTube.
    
👨‍💻 My Creator is <a href=https://t.me/himanshurastogiofficial>Himanshu Rastogi</a>."""
    HELP_TXT = """👋 Hey {}
Here is the help for my commands"""
    ABOUT_TXT = """✯ My Name: {}
✯ Creator: <a href=https://t.me/himanshurastogiofficial>Himanshu Rastogi</a>
✯ Library: <a href=https://pyrogram.org>Pyrogram</a>
✯ Language: <a href=https://python.org>Python 3</a>
✯ Database: <a href=https://mongodb.com/>MongoDB</a>
✯ Server: <a href=https://heroku.com/>Heroku</a>
✯ Build Status: v1.0.1 [Beta]"""
    SOURCE_TXT = """<b>❗️NOTE:</b>
    
- Get my source code <a href=https://github.com/HagadMansa/EvaMaria>here</a>.
- Eva Maria is a open source project.

<b>👨‍💻 My Creator </b> is <a href=https://t.me/himanshurastogiofficial>Himanshu Rastogi</a>.

<b>👨‍💻 My Devoloper</b> is <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """<b>ℹ️ Help</b> > Manual Filters

🔑 Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message.
<b❗️NOTE:</b>

1. Your Bot should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>🧩 Commands and Usage:</b>

• /filter - add a filter in chat
• /filters - list all the filters of a chat
• /del - delete a specific filter in chat
• /delall - delete the whole filters in a chat (chat owner only)"""
    BUTTON_TXT = """<b>ℹ️ Help</b> > Manual Filters > Buttons

- This Bot Supports both url and alert inline buttons.

<b>❗️NOTE:</b>

1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>🔗 URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/hagadmansa)</code>

<b>🔔 Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>ℹ️ Help</b> > Auto Filter

<b>❗️NOTE:</b>

1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """<b>ℹ️ Help</b> > Connections

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>❗️NOTE:</b>

1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>🧩 Commands and Usage:</b>

• /connect  - connect a particular chat to your PM.
• /disconnect  - disconnect from a chat.
• /connections - list all your connections."""
    EXTRAMOD_TXT = """<b>ℹ️ Help</b> > Extra Mods

<b>❗️NOTE:</b>

- These are the extra features of This Bot.

<b>🧩 Commands and Usage:</b>

• /id - get id of a specified user.
• /info  - get information about a user.
• /imdb  - get the film information from IMDb source.
• /search  - get the film information from various sources."""
    ADMIN_TXT = """<b>ℹ️ Help</b> > Extra Mods > Admin

<b>❗️NOTE:</b>

- This module only works for my admins

<b>🧩 Commands and Usage:</b>

• /logs - to get log file, you can check recent errors.
• /stats - to get status of all files in all databases.
• /delete - to delete a specific file from database.
• /users - to get list of all users and ids.
• /chats - to get list of all chats and ids.
• /leave  - to leave from a chat.
• /disable  -  do disable a chat.
• /ban  - to ban a user.
• /unban  - to unban a user.
• /channel - to get list of total connected channels.
• /broadcast - to broadcast a message to all users."""
    STATUS_TXT = """★ Total Files: {}
★ Total Users: {}
★ Total Chats: {}
★ Used Storage: {} MiB
★ Free Storage: {} MiB"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
