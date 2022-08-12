from info import ADMINS
from wordpress_xmlrpc import Client
from pyrogram import Client, filters
from wordpress_xmlrpc import WordPressPost
from wordpress_xmlrpc.methods import posts

@Client.on_message(filters.command('publish') & filters.user(ADMINS))
async def publish(bot, message):
  
  pb = await message.reply("`Processing...`")
  
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


postx = WordPressPost()
postx.title = "Hello World PYTHON"
   postx.slug = "Hello-World-Python"
postx.content = """ Ranjit's Portfolio = https://www.linkedin.com/redir/general-malware-page?url=http%3A%2F%2Franjitpanda224-com%2estackstaging%2ecom """
postx.post_status = "publish"
client.call(posts.NewPost(postx))
