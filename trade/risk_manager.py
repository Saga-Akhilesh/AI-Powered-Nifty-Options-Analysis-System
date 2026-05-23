def calculate_levels(entry_price):

    stoploss = entry_price * 0.75
    target = entry_price * 1.40

    return {
        "entry": entry_price,
        "stoploss": round(stoploss, 2),
        "target": round(target, 2)
    }