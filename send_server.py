import urllib.request
import json
import os

from dotenv import load_dotenv
load_dotenv()

def send_server(mac_address):
    method = "POST"
    post_data = {
        "room_id": os.getenv('ROOM_ID'),
        "mac_address": mac_address
    }

    json_data = json.dumps(post_data).encode("utf-8")
    headers = {"Content-Type": "application/json"}

    request = urllib.request.Request(
        os.getenv('SERVER_ADDRESS'), data=json_data, headers=headers, method=method)
    with urllib.request.urlopen(request) as res:
        body = res.read()
