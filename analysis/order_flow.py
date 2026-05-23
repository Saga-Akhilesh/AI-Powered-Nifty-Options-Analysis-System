def order_flow_imbalance(option_chain):

    if option_chain is None:
        return 0

    data = option_chain["records"]["data"]

    call_volume = 0
    put_volume = 0

    for item in data:

        if "CE" in item:
            call_volume += item["CE"].get("totalTradedVolume", 0)

        if "PE" in item:
            put_volume += item["PE"].get("totalTradedVolume", 0)

    imbalance = call_volume - put_volume

    return imbalance