from nsepython import option_chain


def fetch_option_chain():

    try:

        data = option_chain("NIFTY")

        if not data or len(data.keys()) == 0:
            print("Using mock option chain (weekend/testing)")
            return mock_option_chain()

        return data

    except Exception:

        print("Using mock option chain (error)")
        return mock_option_chain()

def mock_option_chain():

    return {
        "records": {
            "data": [
                {
                    "strikePrice": 23900,
                    "CE": {"lastPrice": 150, "openInterest": 120000},
                    "PE": {"lastPrice": 45, "openInterest": 80000}
                },
                {
                    "strikePrice": 23950,
                    "CE": {"lastPrice": 120, "openInterest": 100000},
                    "PE": {"lastPrice": 55, "openInterest": 90000}
                },
                {
                    "strikePrice": 24000,
                    "CE": {"lastPrice": 95, "openInterest": 140000},
                    "PE": {"lastPrice": 70, "openInterest": 110000}
                },
                {
                    "strikePrice": 24050,
                    "CE": {"lastPrice": 72, "openInterest": 90000},
                    "PE": {"lastPrice": 92, "openInterest": 130000}
                },
                {
                    "strikePrice": 24100,
                    "CE": {"lastPrice": 50, "openInterest": 150000},
                    "PE": {"lastPrice": 120, "openInterest": 100000}
                }
            ]
        }
    }

def get_option_premium(option_chain_data, strike, signal):

    if option_chain_data is None:
        print("No option chain data")
        return None

    if "records" not in option_chain_data:
        print("Unexpected option chain format:", option_chain_data.keys())
        return None

    records = option_chain_data["records"]["data"]

    for item in records:

        if item["strikePrice"] == strike:

            if signal == "CALL" and "CE" in item:
                return item["CE"]["lastPrice"]

            if signal == "PUT" and "PE" in item:
                return item["PE"]["lastPrice"]

    return None