from pyrogram import Client
import os
import invoke

print("Initiating setup")
print("Checking Env variables.....")


if not os.environ["ADMINS"]: 
    print("ADMINS not defined.")
    print("Description: Name of the admins\n   Type:List ")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set ADMINS = {input_text}'
    invoke.run(cmd)

if not os.environ["API_HASH"]: 
    print("API_HASH not defined.")
    print("Description:API Hash")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set API_HASH = {input_text}'
    invoke.run(cmd)

if not os.environ["API_ID"]: 
    print("API_ID not defined.")
    print("Description: API ID")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set API_ID = {input_text}'
    invoke.run(cmd)

if not os.environ["AZ_AFF"]: 
    print("AZ_AFF not defined.")
    print('Description: Amazon param and affilate tag.\n  Type:JSON\n Example: { param: tag }  ')
    input_text = input("Enter a value:")
    cmd = F'heroku config:set AZ_AFF = {input_text}'
    invoke.run(cmd)

if not os.environ["F_AFF"]: 
    print("F_AFF not defined.")
    print('Description: Flipkart param and affilate tag.\n  Type:JSON\n Example: { param: tag }  ')
    input_text = input("Enter a value:")
    cmd = F'heroku config:set F_AFF = {input_text}'
    invoke.run(cmd)

if not os.environ["P1_BLOCK_MESSAGES"]: 
    print("P1_BLOCK_MESSAGES not defined.")
    print("Description: Blockmessage words  for main.\n  Type:List")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set P1_BLOCK_MESSAGES = {input_text}'
    invoke.run(cmd)

if not os.environ["P1_BLOCK_LINES"]: 
    print("P1_BLOCK_LINES not defined.")
    print("Description: Blocklines words  for main.\n  Type:List ")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set P1_BLOCK_LINES = {input_text}'
    invoke.run(cmd)

if not os.environ["P1_BLOCK_WORDS"]: 
    print("P1_BLOCK_WORDS not defined.")
    print("Description: Blockwords  for main.\n  Type:List")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set P1_BLOCK_WORDS = {input_text}'
    invoke.run(cmd)

if not os.environ["P2_BLOCK_WORDS"]: 
    print("P2_BLOCK_WORDS not defined.")
    print("Description: Blockwords  for #2.\n  Type:List")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set P2_BLOCK_WORDS = {input_text}'
    invoke.run(cmd)

if not os.environ["BOT_NAME"]: 
    print("BOT_NAME not defined.")
    print("Description: Bot name")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set BOT_NAME = {input_text}'
    invoke.run(cmd)

if not os.environ["BOT_TKN"]: 
    print("BOT_TKN not defined.")
    print("Description: Bot token ")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set BOT_TKN = {input_text}'
    invoke.run(cmd)

if not os.environ["FQG_TEXT"]: 
    print("FQG_TEXT not defined.")
    print("Description: quiz match text")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set FQG_TEXT = {input_text}'
    invoke.run(cmd)

if not os.environ["H1_CHAT"]: 
    print("H1_CHAT not defined.")
    print("Description: Username of 1st channel ")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set H1_CHAT = {input_text}'
    invoke.run(cmd)

if not os.environ["H2_CHAT"]: 
    print("H2_CHAT not defined.")
    print("Description: Username of 2nd channel")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set H2_CHAT = {input_text}'
    invoke.run(cmd)

if not os.environ["PHONE_NUMBER"]: 
    print("PHONE_NUMBER not defined.")
    print("Description: Phone number")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set PHONE_NUMBER = {input_text}'
    invoke.run(cmd)

if not os.environ["R_CHAT"]: 
    print("R_CHAT not defined.")
    print("Description: Your channel username")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set R_CHAT = {input_text}'
    invoke.run(cmd)

if not os.environ["EK_DOMAINS"]: 
    print("EK_DOMAINS not defined.")
    print("Description: Earn karo domains \n type: list")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set EK_DOMAINS = {input_text}'
    invoke.run(cmd)

if not os.environ["SHORTURL_DOMAINS"]: 
    print("SHORTURL_DOMAINS not defined.")
    print("Description: Short url domains \n type: list")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set SHORTURL_DOMAINS = {input_text}'
    invoke.run(cmd)

if not os.environ["FLIPKART_DOMAINS"]: 
    print("FLIPKART_DOMAINS not defined.")
    print("Description: Flipkart domains \n type: list")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set FLIPKART_DOMAINS = {input_text}'
    invoke.run(cmd)

if not os.environ["AMAZON_DOMAINS"]: 
    print("AMAZON_DOMAINS not defined.")
    print("Description: Amazon domains \n type: list")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set AMAZON_DOMAINS = {input_text}'
    invoke.run(cmd)

if not os.environ["EK_COOKIES"]: 
    print("EK_COOKIES not defined.")
    print("Description: Earn Karo cookies \n type: Dict")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set EK_COOKIES = {input_text}'
    invoke.run(cmd)

if not os.environ["AMAZON_COOKIES"]: 
    print("AMAZON_COOKIES not defined.")
    print("Description: Amazon cookies \n type: Dict")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set AMAZON_COOKIES = {input_text}'
    invoke.run(cmd)

if not os.environ["AMAZON_MARKETPLACE_ID"]: 
    print("AMAZON_MARKETPLACE_ID not defined.")
    print("Description: Amazon marketplace ID \n type: number")
    input_text = input("Enter a value:")
    cmd = F'heroku config:set AMAZON_MARKETPLACE_ID = {input_text}'
    invoke.run(cmd)

print("All Env variables are defined..")

# *********************

print("Checking for session strings...")

print("Checking session string for self...")

if not os.environ["SELF_STRING"]:

    print("Session string for self not yet generated...")
    print("Generating session string for self...")

    api_id = os.environ["API_ID"]
    api_hash = os.environ["API_HASH"]
    phone_number = os.environ["PHONE_NUMBER"]

    self = Client("my_account", api_id, api_hash,phone_number =phone_number)

    with self:
        self_string = self.export_session_string()
        print("SELF SESSION STRING",self_string)

        print("SELF SESSION STRING - saving to env..")

        cmd = F'heroku config:set SELF_STRING = {self_string}'
        invoke.run(cmd)
        print("SELF SESSION STRING - saved successfully..")


print("Checking session string for bot...")

if not os.environ["BOT_STRING"]:

    bot_token = os.environ["BOT_TOKEN"]
    bot_name = os.environ["BOT_NAME"]

    print("Session string for bot not yet generated...")
    print("Generating session string for bot...")

    bot = Client(bot_name,api_id,api_hash,bot_token=bot_token)

    with bot:
        bot_string = bot.export_session_string()
        print("BOT SESSION STRING",bot_string)

        print("BOT SESSION STRING - saving to env..")

        cmd = F'heroku config:set BOT_STRING = {bot_string}'
        invoke.run(cmd)
        print("BOT SESSION STRING - saved successfully..")