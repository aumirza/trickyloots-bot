from pyrogram import Client
from params import self_name,api_id,api_hash 

self = Client(self_name, api_id, api_hash,phone_number =phone_number)

with self:
    print(self.export_session_string(),file=f)

