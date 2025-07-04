from kiteconnect import KiteConnect
import os

def get_kite_with_token():
    api_key = os.getenv("API_KEY")
    kite = KiteConnect(api_key=api_key)

    try:
        # Read access_token from file
        with open("access_token.txt", "r") as f:
            access_token = f.read().strip()
        kite.set_access_token(access_token)
        return kite
    except FileNotFoundError:
        raise Exception("Access token not found. Please login first.")