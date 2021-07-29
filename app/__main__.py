from pyrogram import Client, filters
from app.utils.p1_processor import processor as p1
from app.utils.p2_processor import processor as p2
from app.config import h1_chat, h2_chat, r_chat, admins, api_id, api_hash, self_string, bot_string
from app.utils.db import insert_query, select_query

if bot_string & self_string:

    self = Client(self_string, api_id, api_hash)
    bot = Client(bot_string, api_id, api_hash)

    bot.start()

    # H1 handler

    @self.on_message(filters.chat(h1_chat) & ~ filters.edited)
    def txt_msg_fuc(client, message):

        # check if message is media message
        if message.media:
            msg_text = message.caption
        else:
            msg_text = message.text

        processed_msg_txt = p1(message.text).process()
        msg_reply = message.reply_to_message

        if processed_msg_txt != "":

            if msg_reply:

                source_reply_msg_id = message.reply_to_message.message_id

                query1 = f"SELECT dest_id FROM message_id WHERE source_id={source_reply_msg_id};"
                message_id_to_reply = select_query(query1)

                sent_messge = bot.send_message(chat_id=r_chat, text=processed_msg_txt, reply_to_message_id=message_id_to_reply,
                                               disable_web_page_preview=True)

                sent_message_id = sent_messge.message_id
                source_msg_id = message.message_id

                query1 = f"INSERT INTO message_id (source_id,dest_id) VALUES ({source_msg_id},{sent_message_id});"
                insert_query(query1)

            else:
                sent_messge = bot.send_message(
                    chat_id=r_chat, text=processed_msg_txt, disable_web_page_preview=True)
                sent_message_id = sent_messge.message_id
                source_msg_id = message.message_id

                query1 = f"INSERT INTO message_id (source_id,dest_id) VALUES ({source_msg_id},{sent_message_id});"
                insert_query(query1)

    # H2 Handler

    @self.on_message(filters.chat(h2_chat) & ~ filters.edited & filters.media)
    def txt_msg_fuc(client, message):
        msg = p2(message.caption).process()
        if msg != ("" or None):
            bot.send_photo(
                chat_id=r_chat, photo=message.photo.file_id, caption=msg)

    # Bot handlers

    @bot.on_message(filters.user(admins) & filters.command("start"))
    def start_comm_function(client, message):
        msg = f"Hi! {message.from_user.first_name}.\nThe bot is currently running."
        message.reply_text(msg)

    @bot.on_message(filters.command("convert") & filters.reply & ~ filters.media)
    def convert_comm_function(client, message):
        msg = p1(message.reply_to_message.text).process()
        if msg != "":
            message.reply_text(msg, quote=True, disable_web_page_preview=True)

    @bot.on_message(filters.command("convert") & filters.reply & filters.media)
    def convert_comm_function(client, message):
        msg = p1(message.reply_to_message.caption).process()
        if msg != "":
            message.reply_photo(photo=message.photo.file_id,
                                caption=msg, quote=True)

    @bot.on_message(filters.command("start") & ~ filters.user(admins))
    def comm_function(client, message):
        msg = "Sorry......... \n This bot is not for you"
        message.reply_text(msg)

    self.run()
