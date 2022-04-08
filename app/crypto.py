print("CRYPTO REPORT...")

import os
import json
from dotenv import load_dotenv
import requests
from alphavantage_service.py import fetch_crypto_data
from app.utils import to_usd

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"
parsed_response = fetch_crypto_data()
fetch_crypto_data(symbol)

tsd = parsed_response["Time Series (Digital Currency Daily)"]

dates = list(tsd.keys())
latest_date = dates[0]
latest = tsd[latest_date]
#print(latest)


print(symbol)
print(latest_date)
#print(latest['4a. close (USD)'])
print(to_usd(float(latest['4a. close (USD)'])))
#updates from to_usd 