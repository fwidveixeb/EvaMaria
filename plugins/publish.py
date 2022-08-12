# Importing modules
import random
from info import ADMINS
from pyrogram import Client, filters

# Importing WordPress modules
from wordpress_xmlrpc import Client
from wordpress_xmlrpc import WordPressPost
from wordpress_xmlrpc.methods import posts

# Creating command
@Client.on_message(filters.command('publish') & filters.user(ADMINS))
async def publish(bot, message):
  
  # Sending a simple message
  pb = await message.reply("`Processing...`")
  
  # Creating random slug
  ok = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  ko = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  io = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  
  papa = random.choice(ok) + random.choice(io) + random.choice(ko) + random.choice(ok) + random.choice(io) + random.choice(ko)
  
  # Defining Wordpress Password
  client = Client("https://hagadmansa.com/xmlrpc.php", "himanshurastogiofficial", "GyanSamuh@rty")
  
  # Getting message ids
  a =  message.id - 8
  b = message.id - 6
  c = message.id - 3
  d = message.id - 1
  
  # Finding text from message ids
  e = await bot.get_messages(message.chat.id, a)
  f = await bot.get_messages(message.chat.id, b)
  g = await bot.get_messages(message.chat.id, c)
  h = await bot.get_messages(message.chat.id, d)

  # Publishing on Wordpress
  x = WordPressPost()
  x.title = papa
  x.slug = papa
  content = """<html>
<body>

<script>
        function Button1() {
            window.open(
            "https://a.hagadmansa.com/st?api=284ad0efe9a3d5f77d06a23e18bd0c0b157c379b&url=one",
            "_blank");
        }
    </script>

<script>
        function Button2() {
            window.open(
            "https://a.hagadmansa.com/st?api=284ad0efe9a3d5f77d06a23e18bd0c0b157c379b&url=two",
            "_blank");
        }
    </script>

<script>
        function Button3() {
            window.open(
            "https://a.hagadmansa.com/st?api=284ad0efe9a3d5f77d06a23e18bd0c0b157c379b&url=three",
            "_blank");
        }
    </script>

<script>
        function Button4() {
            window.open(
            "https://a.hagadmansa.com/st?api=284ad0efe9a3d5f77d06a23e18bd0c0b157c379b&url=four",
            "_blank");
        }
    </script>
 
<h5 id="heading1">Please select a specific download link to proceed.<h5>

<h5 id="heading2">Upto 1024 MB (1 GB) Links<h5>

<p style="text-align: center;"><button class="button1" onClick="Button1()">📥 Direct Download</button></p>

<p style="text-align: center;"><button class="button2" onClick="Button2()">📂 Telegram File</button></p>

<h5 id="heading3">Upto 2048 MB (2 GB) Links<h5>

<p style="text-align: center;"><button class="button3" onClick="Button3()">📥 Direct Download</button></p>

<p style="text-align: center;"><button class="button4" onClick="Button4()">📂 Telegram File</button></p>

</body>
</html>"""
  mama = content.replace('one', e.text).replace('two', f.text).replace('three', g.text).replace('four', h.text)
  x.content = mama
  x.post_status = "publish"
  client.call(posts.NewPost(x))
  await pb.edit(f'https://link.hagadmansa.com/{papa}')
