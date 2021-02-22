from pyrogram import Client
import os

api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")   

self = Client("my_account", api_id, api_hash)

with self:
    print("self",self.export_session_string())
