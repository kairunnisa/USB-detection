import json

CONFIG_FILE = "config/authorized_devices.json"

def is_authorized(device_name):
    with open(CONFIG_FILE, "r") as file:
        data = json.load(file)

    authorized = data["authorized_devices"]

    return device_name in authorized
