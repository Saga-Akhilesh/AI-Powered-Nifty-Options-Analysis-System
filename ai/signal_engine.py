def generate_signal(regime, breakout, sentiment):

    if regime == "SIDEWAYS":
        return "NO_TRADE"

    if regime == "BULLISH" and breakout == "BREAKOUT":
        return "CALL"

    if regime == "BEARISH" and breakout == "BREAKDOWN":
        return "PUT"

    return "NO_TRADE"