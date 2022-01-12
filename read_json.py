import json

tag_json = open("./ble_tag.json", "r")
tag_list = json.load(tag_json)


def check_tag_number(mac_address):
    for address in tag_list:
        if address["mac_address"] == mac_address:
            return address["number"]
