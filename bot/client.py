import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BASE_URL = os.getenv("BASE_URL")

def get_client():
    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = BASE_URL
    return client