def analyze_oi(option_chain):

    data = option_chain["records"]["data"]

    max_call_oi = 0
    max_put_oi = 0

    call_resistance = None
    put_support = None

    for item in data:

        strike = item["strikePrice"]

        if "CE" in item:
            call_oi = item["CE"].get("openInterest", 0)

            if call_oi > max_call_oi:
                max_call_oi = call_oi
                call_resistance = strike

        if "PE" in item:
            put_oi = item["PE"].get("openInterest", 0)

            if put_oi > max_put_oi:
                max_put_oi = put_oi
                put_support = strike

    return {
        "support": put_support,
        "resistance": call_resistance
    }