from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from utils import message_processor as tool
from params import h_chat, r_chat, admins , bot_name,self_name

self = Client(self_name,)
bot = Client(bot_name)

bot.start()

bot_status = "running"
bot_mode= True


def bot_swith(comm):
    global bot_status , bot_mode
    if comm == "run" and bot_status != "running":
        bot_status = "running"
        bot_mode = True

    if comm == "stop" and bot_status != "stopped":
        bot_status = "stopped"
        bot_mode = False



@self.on_message(filters.chat(h_chat) & ~ filters.edited & ~ filters.media)
def txt_msg_fuc(client, message):
    if bot_mode:
        msg_raw = message.text
        if msg_raw != "":
            msg = tool(msg_raw)
            if msg != "":
                bot.send_message(chat_id=r_chat, text=msg)


# @self.on_message(filters.media & ~ filters.edited)
# def media_msg_fuc(client, message):
#     if bot_mode:
#         if message.photo:
#             file_id = message.photo.file_id
#             file_ref = message.photo.file_ref
#             if message.caption:
#                 caption = tool(message.caption)
#                 self.send_photo(r_chat, file_id, caption=caption)
#             else:
#                 self.send_photo(r_chat, file_id, file_ref)


@bot.on_message(filters.user(admins) & filters.command("start"))
def start_comm_function(client, message):
    msg = f"Hi! {message.from_user.first_name}.\nThe bot is currently {bot_status}"
    message.reply_text(msg)  # reply_markup=reply_markup


@bot.on_message(filters.user(admins) & filters.command("run"))
def run_comm_function(client, message):
    bot_swith("run")
    message.reply_text(f"The bot has been {bot_status} ")
    
@bot.on_message(filters.command("convert") & filters.reply)
def convert_comm_function(client, message):
    msg_raw = message.reply_to_message.text
    if msg_raw != "":
        msg = tool(msg_raw)
        if msg != "":
            message.reply_text(msg, quote=True)


@bot.on_message(filters.user(admins) & filters.command("stop"))
def stop_comm_function(client, message):
    bot_swith("stop")
    message.reply_text(f"The bot has been {bot_status} ")


@bot.on_message(filters.command("start") & ~ filters.user(admins))
def comm_function(client, message):
    msg = "Sorry......... \n This bot is not for you"
    message.reply_text(msg)

self.run()