from app.helpers.p1_processor import processor as p1


def admin_start_comm_handler(client, message):
    msg = f"Hi! {message.from_user.first_name}.\nThe bot is currently running."
    message.reply_text(msg)


def convert_comm_handler(client, message):
    if message.media:
        msg = p1(message.reply_to_message.caption).process()
        if msg != "":
            message.reply_photo(photo=message.photo.file_id,
                                caption=msg, quote=True)
    else:
        msg = p1(message.reply_to_message.text).process()
        if msg != "":
            message.reply_text(msg, quote=True, disable_web_page_preview=True)


def start_comm_handler(client, message):
    msg = "Sorry......... \n This bot is not for you"
    message.reply_text(msg)
