from config import PREMIUM_USERS

def is_premium(user_id):
    return user_id in PREMIUM_USERS


import json
import os

FILE = "premium_users.json"

def load_premium():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def add_premium(user_id):
    users = load_premium()
    if user_id not in users:
        users.append(user_id)
        with open(FILE, "w") as f:
            json.dump(users, f)

def is_premium(user_id):
    return user_id in load_premium()
