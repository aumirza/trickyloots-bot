import os
import json
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DATABASE_URL")

self_string = os.getenv("SELF_STRING")
bot_string = os.getenv("BOT_STRING")


bot_token = os.getenv("BOT_TOKEN")
bot_name = os.getenv("BOT_NAME")

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE_NUMBER")

f_aff = json.loads(os.getenv("F_AFF"))
az_aff = json.loads(os.getenv("AZ_AFF"))

h1_chat = int(os.getenv("H1_CHAT"))
h2_chat = os.getenv("H2_CHAT")
r_chat = os.getenv("R_CHAT")
admins = json.loads(os.getenv("ADMINS"))


# P1 Processor config
class p1_config:

    ek_domains = json.loads(os.getenv("EK_DOMAINS"))
    shorturl_domains = json.loads(os.getenv("SHORTURL_DOMAINS"))
    flipkart_domains = json.loads(os.getenv("FLIPKART_DOMAINS"))
    amazon_domains = json.loads(os.getenv("AMAZON_DOMAINS"))

    ek_headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    ek_cookies = json.loads(os.getenv("EK_COOKIES"))
    amazon_cookies = json.loads(os.getenv("AMAZON_COOKIES"))
    amazon_marketplace_id = json.loads(os.getenv("AMAZON_MARKETPLACE_ID"))

    amazon_shortner_api = "https://www.amazon.in/associates/sitestripe/getShortUrl"
    flipkart_shortner_api = "https://affiliate.flipkart.com/a_url_shorten"
    ek_api = 'https://ek.dealsunlimited.in/hitter.php'

    blockmessages = json.loads(os.getenv("P1_BLOCK_MESSAGES"))
    blocklines = json.loads(os.getenv("P1_BLOCK_LINES"))
    blockwords = json.loads(os.getenv("P1_BLOCK_WORDS"))


# P2 Processor config
class p2_config:
    fqg_text = os.getenv("FQG_TEXT")
    blockwords = json.loads(os.getenv("P2_BLOCK_WORDS"))
