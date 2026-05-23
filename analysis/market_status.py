from datetime import datetime
import requests


def is_weekend():

    today = datetime.today().weekday()

    if today >= 5:
        return True

    return False


def is_market_hours():

    now = datetime.now()

    start = now.replace(hour=9, minute=15, second=0)
    end = now.replace(hour=15, minute=30, second=0)

    return start <= now <= end


def is_nse_holiday():

    url = "https://www.nseindia.com/api/holiday-master?type=trading"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:

        r = requests.get(url, headers=headers)

        holidays = r.json()["CM"]

        today = datetime.today().strftime("%d-%b-%Y")

        for h in holidays:

            if h["tradingDate"] == today:
                return True

        return False

    except:
        return False
    
def market_is_open():

    if is_weekend():
        return False, "Weekend"

    if is_nse_holiday():
        return False, "Holiday"

    if not is_market_hours():
        return False, "Outside trading hours"

    return True, "Market Open"