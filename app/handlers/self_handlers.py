from pyrogram.types import Message

from app.helpers.p1_processor import processor as p1
from app.helpers.p2_processor import processor as p2
from app.helpers.db import insert_query, select_query
from app.config import r_chat
from __main__ import bot

# H1 Handler


def main_channel_handler(client, message: Message):

    msg_text = message.caption if (
        message.media and not message.web_page) else message.text

    processed_msg_txt = p1(msg_text).process()
    msg_reply = message.reply_to_message

    if processed_msg_txt == "":
        return

    if msg_reply:

        source_reply_msg_id = message.reply_to_message_id

        query1 = f"SELECT dest_id FROM message_id WHERE source_id={source_reply_msg_id};"
        message_id_to_reply = select_query(query1)

        sent_messge = bot.send_message(
            chat_id=r_chat, text=processed_msg_txt,
            reply_to_message_id=message_id_to_reply,
            disable_web_page_preview=True
        )

    else:
        sent_messge = bot.send_message(
            chat_id=r_chat, text=processed_msg_txt, disable_web_page_preview=True)

    sent_message_id = sent_messge.id
    source_msg_id = message.id

    query1 = f"INSERT INTO message_id (source_id,dest_id) VALUES ({source_msg_id},{sent_message_id});"
    insert_query(query1)

# H2 Handler


def secondary_channel_handler(client, message):
    msg = p2(message.caption).process()
    if msg == ("" or None):
        return
    bot.send_photo(chat_id=r_chat, photo=message.photo.file_id, caption=msg)
