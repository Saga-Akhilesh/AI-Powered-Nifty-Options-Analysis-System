def institutional_positioning(option_chain):

    if option_chain is None:
        return "UNKNOWN"

    data = option_chain["records"]["data"]

    call_oi = 0
    put_oi = 0

    for item in data:

        if "CE" in item:
            call_oi += item["CE"].get("openInterest", 0)

        if "PE" in item:
            put_oi += item["PE"].get("openInterest", 0)

    if put_oi > call_oi:
        return "BULLISH_POSITIONING"

    if call_oi > put_oi:
        return "BEARISH_POSITIONING"

    return "NEUTRAL"