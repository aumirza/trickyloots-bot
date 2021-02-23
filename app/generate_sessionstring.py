from pyrogram import Client
import os

api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")   

self = Client("my_account", api_id, api_hash)

s_file = "my_account.session"

with open(s_file,"w") as f:
    with self:
        print(self.export_session_string(),file=f)

