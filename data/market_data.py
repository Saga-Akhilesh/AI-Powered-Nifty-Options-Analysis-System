# import requests
# from config.constants import NIFTY_PRICE_URL

# headers = {"User-Agent": "Mozilla/5.0"}

# def get_nifty_price():

#     r = requests.get(NIFTY_PRICE_URL, headers=headers)

#     data = r.json()

#     return data["data"][0]["lastPrice"]

import yfinance as yf


def get_nifty_price():

    try:

        ticker = yf.Ticker("^NSEI")

        price = ticker.fast_info["last_price"]

        return round(price, 2)

    except Exception as e:

        print("Error fetching Nifty price:", e)

        return None



def get_nifty_candles():

    try:

        ticker = yf.Ticker("^NSEI")

        df = ticker.history(period="5d", interval="5m")

        if df.empty:
            print("No candle data")
            return None

        df = df.rename(columns={
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close"
        })

        return df

    except Exception as e:

        print("Error fetching candles:", e)

        return None

def get_vix():

    vix = yf.Ticker("^INDIAVIX")

    data = vix.history(period="1d")

    return data["Close"].iloc[-1]