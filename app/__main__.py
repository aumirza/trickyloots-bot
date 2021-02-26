from pyrogram import Client, filters
from utils.p1_processor import processor as p1
from utils.p2_processor import processor as p2
from config import h1_chat, h2_chat , r_chat, admins , api_id , api_hash

self = Client(self_string, api_id , api_hash)
bot = Client(bot_string, api_id , api_hash)

bot.start()

# H1 handler
@self.on_message(filters.chat(h_chat) & ~ filters.edited & ~ filters.media)
def txt_msg_fuc(client, message):
    msg = p1(message).process()
    if msg != ""
        bot.send_message(chat_id=r_chat, text=msg)

# H2 Handler
@self.on_message(filters.chat(h1_chat) & ~ filters.edited & filters.media)
def txt_msg_fuc(client, message):
    msg=p2(message.caption).process()
    if msg != ""
        bot.send_photo(chat_id=r_chat, photo=message.photo.file_id  caption=msg)


# Bot handlers 
@bot.on_message(filters.user(admins) & filters.command("start"))
def start_comm_function(client, message):
    msg = f"Hi! {message.from_user.first_name}.\nThe bot is currently running."
    message.reply_text(msg)

    
@bot.on_message(filters.command("convert") & filters.reply)
def convert_comm_function(client, message):
    msg = p1(message.reply_to_message.text).process()
    if msg != "":
        message.reply_text(msg, quote=True)


@bot.on_message(filters.command("start") & ~ filters.user(admins))
def comm_function(client, message):
    msg = "Sorry......... \n This bot is not for you"
    message.reply_text(msg)

self.run()