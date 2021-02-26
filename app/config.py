import os , json

# General config

self_string = os.environ.get("SELF_STRING",None)
bot_string = os.environ.get("BOT_STRING",None)


bot_token = os.environ.get("BOT_TKN")
bot_name = os.environ.get("BOT_NAME")

api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
phone_number = os.environ.get("PHONE_NUMBER")

f_aff= json.loads(os.environ.get("F_AFF"))
az_aff= json.loads(os.environ.get("AZ_AFF"))


h1_chat = os.environ.get("H1_CHAT")
h2_chat = os.environ.get("H2_CHAT")
r_chat = os.environ.get("R_CHAT")
admins = json.loads(os.environ.get("ADMINS"))


# P1 Processor config
class p1_config:
    ek_domains= ["ekaro.in"]
    ek_headers = {
    'content-type':'application/x-www-form-urlencoded',
    'Cookie': 'hash=44f08c67e1a21f92d023d985cbf6d976; uid=415; ek_id=226926; PHPSESSID=ea30f1d054b894eb5e2137c2c9334d8c',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    ek_post_url = 'https://ek.dealsunlimited.in/hitter.php'

    flipkart_domains=["dl.flipkart.com","fkrt.it","www.flipkart.com"]
    amazon_domains=["www.amazon.in","amzn.to"]
    shorturl_domains=["bit.ly"]

    blockmessages = json.loads(os.environ.get("P1_BLOCK_MESSAGES"))
    blocklines= json.loads(os.environ.get("P1_BLOCK_LINES"))
    blockwords = json.loads(os.environ.get("P2_BLOCK_WORDS"))


# P2 Processor config
class p2_config:
    fqg_text= "Flipkart Video Quiz Games Answers"
    blockwords = ["play here"]








