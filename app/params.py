import os

eklist= ["ekaro.in"]
headers = {
'content-type':'application/x-www-form-urlencoded',
'Cookie': 'hash=44f08c67e1a21f92d023d985cbf6d976; uid=415; ek_id=226926; PHPSESSID=ea30f1d054b894eb5e2137c2c9334d8c',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
post_url = 'https://ek.dealsunlimited.in/hitter.php'
f_aff={"affid":"habibmy21"}
az_aff={"tag":"trickyloots-21"}
flipkart=["dl.flipkart.com","fkrt.it","www.flipkart.com"]
amazon=["www.amazon.in","amzn.to"]
shorturl=["bit.ly"]
blockmessages = os.environ.get("BLOCK_MESSAGES")
blocklines= os.environ.get("BLOCK_LINES")
blockwords = os.environ.get("BLOCK_WORDS")
h_chat = os.environ.get("H_CHAT")
r_chat = os.environ.get("R_CHAT")
admins = os.environ.get("ADMINS")
bot_name = os.environ.get("BOT_NAME")
bot_token = os.environ.get("BOT_TKN")
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
self_name = "my_account"
phone_number = "+919956763804"
self_string = os.environ.get("SELF_STRING",None)
bot_string = os.environ.get("BOT_STRING",None)
