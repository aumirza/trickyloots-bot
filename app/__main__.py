from pyrogram import Client,  idle
from config import api_id, api_hash, self_string, bot_string,bot_name
from handlers.bot_handlers import BotHandler
from handlers.self_handlers import SelfHandler

if bot_string and self_string:
    self_client = Client('my_account', api_id, api_hash, session_string=self_string)
    bot_client = Client(bot_name, api_id, api_hash,
                 session_string=bot_string)


if __name__ == "__main__":

    # Self Handlers
    SelfHandler(self_client).add_handlers()

    # Bot handlers
    BotHandler(bot_client).add_handlers()



    self_client.start()
    print("Self Started", self_client.is_connected)
    bot_client.start()
    print("Bot Started", bot_client.is_connected)
    idle()
    self_client.stop()
    bot_client.stop()
