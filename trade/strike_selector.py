def get_atm_strike(spot):

    return round(spot / 50) * 50


def select_strikes(signal, price):

    # Round to nearest 50 (ATM)
    atm = round(price / 50) * 50

    if signal == "CALL":
        return {
            "safe": f"{atm} CE",            # ATM
            "aggressive": f"{atm + 50} CE", # OTM
            "conservative": f"{atm - 50} CE" # ITM
        }

    elif signal == "PUT":
        return {
            "safe": f"{atm} PE",            # ATM
            "aggressive": f"{atm - 50} PE", # OTM
            "conservative": f"{atm + 50} PE" # ITM
        }

    return None