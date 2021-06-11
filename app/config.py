import os , json

# General config

db_url = os.environ.get("DATABASE_URL")

self_string = os.environ.get("SELF_STRING")
bot_string = os.environ.get("BOT_STRING")


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

    ek_domains= json.loads(os.environ.get("EK_DOMAINS"))
    shorturl_domains= json.loads(os.environ.get("SHORTURL_DOMAINS"))
    flipkart_domains= json.loads(os.environ.get("FLIPKART_DOMAINS"))
    amazon_domains= json.loads(os.environ.get("AMAZON_DOMAINS"))
    
    ek_headers = {
    'content-type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    ek_cookies = json.loads(os.environ.get("EK_COOKIES"))
    amazon_cookies= json.loads(os.environ.get("AMAZON_COOKIES"))
    amazon_marketplace_id = json.loads(os.environ.get("AMAZON_MARKETPLACE_ID"))
    
    amazon_shortner_api = "https://www.amazon.in/associates/sitestripe/getShortUrl"
    flipkart_shortner_api = "https://affiliate.flipkart.com/a_url_shorten"
    ek_api = 'https://ek.dealsunlimited.in/hitter.php'


    blockmessages = json.loads(os.environ.get("P1_BLOCK_MESSAGES"))
    blocklines= json.loads(os.environ.get("P1_BLOCK_LINES"))
    blockwords = json.loads(os.environ.get("P1_BLOCK_WORDS"))


# P2 Processor config
class p2_config:
    fqg_text= os.environ.get("FQG_TEXT")
    blockwords = json.loads(os.environ.get("P2_BLOCK_WORDS"))
