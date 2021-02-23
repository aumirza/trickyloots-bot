from pyrogram import Client
from params import self_name,api_id,api_hash , phone_number
import os

self = Client(self_name, api_id, api_hash,phone_number =phone_number)

with self:
    self_string = self.export_session_string()
    os.environ["SELF_STRING"] = self_string
    print("SELF SESSION STRING",self_string)

