import os
import json
from dotenv import load_dotenv

load_dotenv()


db_host = os.getenv("DATABASE_HOST")
db_user = os.getenv("DATABASE_USER")
db_password = os.getenv("DATABASE_PASSWORD")
db_name = os.getenv("DATABASE_NAME")
db_port = os.getenv("DATABASE_PORT") if os.getenv("DATABASE_PORT") else "5432"

self_string = os.getenv("SELF_STRING")
bot_string = os.getenv("BOT_STRING")


bot_token = os.getenv("BOT_TOKEN")
bot_name = os.getenv("BOT_NAME")

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE_NUMBER")

f_aff = json.loads(os.getenv("F_AFF") if os.getenv("F_AFF") else "[]")
az_aff = json.loads(os.getenv("AZ_AFF") if os.getenv("AZ_AFF") else "[]")

h1_chat = int(os.getenv("H1_CHAT") if os.getenv("H1_CHAT") else 0)
h2_chat = os.getenv("H2_CHAT")
r_chat = os.getenv("R_CHAT")
admins = json.loads(os.getenv("ADMINS") if os.getenv("ADMINS") else "[]")


# P1 Processor config
class p1_config:

    ek_domains = json.loads(os.getenv("EK_DOMAINS") if os.getenv("EK_DOMAINS") else "[]")
    shorturl_domains = json.loads(os.getenv("SHORTURL_DOMAINS") if os.getenv("SHORTURL_DOMAINS") else "[]")
    flipkart_domains = json.loads(os.getenv("FLIPKART_DOMAINS") if os.getenv("FLIPKART_DOMAINS") else "[]")
    amazon_domains = json.loads(os.getenv("AMAZON_DOMAINS")   if os.getenv("AMAZON_DOMAINS")   else "[]")

    ek_headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    ek_cookies = json.loads(os.getenv("EK_COOKIES") if os.getenv("EK_COOKIES") else "{}")
    amazon_cookies = json.loads(os.getenv("AMAZON_COOKIES") if os.getenv("AMAZON_COOKIES") else "{}")
    amazon_marketplace_id = json.loads(os.getenv("AMAZON_MARKETPLACE_ID") if os.getenv("AMAZON_MARKETPLACE_ID") else "{}")

    amazon_shortner_api = "https://www.amazon.in/associates/sitestripe/getShortUrl"
    flipkart_shortner_api = "https://affiliate.flipkart.com/a_url_shorten"
    ek_api = 'https://ek.dealsunlimited.in/hitter.php'

    blockmessages = json.loads(os.getenv("P1_BLOCK_MESSAGES") if os.getenv("P1_BLOCK_MESSAGES") else "[]")
    blocklines = json.loads(os.getenv("P1_BLOCK_LINES") if os.getenv("P1_BLOCK_LINES") else "[]")
    blockwords = json.loads(os.getenv("P1_BLOCK_WORDS") if os.getenv("P1_BLOCK_WORDS") else "[]")


# P2 Processor config
class p2_config:
    fqg_text = os.getenv("FQG_TEXT")
    blockwords = json.loads(os.getenv("P2_BLOCK_WORDS") if os.getenv("P2_BLOCK_WORDS") else "[]")
