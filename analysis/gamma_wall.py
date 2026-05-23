def detect_gamma_walls(option_chain):

    if option_chain is None:
        return None

    data = option_chain["records"]["data"]

    call_oi = {}
    put_oi = {}

    for item in data:

        strike = item["strikePrice"]

        if "CE" in item:
            call_oi[strike] = item["CE"].get("openInterest", 0)

        if "PE" in item:
            put_oi[strike] = item["PE"].get("openInterest", 0)

    call_wall = max(call_oi, key=call_oi.get)
    put_wall = max(put_oi, key=put_oi.get)

    return {
        "call_wall": call_wall,
        "put_wall": put_wall
    }