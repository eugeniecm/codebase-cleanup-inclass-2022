

print("STOCKS REPORT...")

import os
from dotenv import load_dotenv
from pandas import read_csv
from alphavantage_service.py import fetch_stocks_data
from app.utils import to_usd

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"
fetch_stocks_data(symbol)

