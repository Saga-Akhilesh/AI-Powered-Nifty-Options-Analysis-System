import yfinance as yf


def get_india_vix():

    try:

        vix = yf.Ticker("^INDIAVIX")

        data = vix.history(period="1d")

        if data.empty:
            return None

        return float(data["Close"].iloc[-1])

    except Exception as e:

        print("Error fetching VIX:", e)

        return None


def vix_regime(vix):

    if vix is None:
        return "UNKNOWN"

    if vix < 12:
        return "LOW_VOL"

    if vix < 18:
        return "NORMAL_VOL"

    return "HIGH_VOL"