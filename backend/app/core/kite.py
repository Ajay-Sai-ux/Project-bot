from kiteconnect import KiteConnect, KiteTicker
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

kite = KiteConnect(api_key=api_key)

with open("access_token.txt", "r") as f:
    access_token = f.read().strip()

kws = KiteTicker(api_key, access_token)