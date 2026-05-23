def calculate_confidence(regime, breakout, vix_regime, order_flow, inst_pos):

    score = 0

    # Trend
    if regime == "BULLISH":
        score += 20

    if regime == "BEARISH":
        score += 20

    # Breakout
    if breakout == "BREAKOUT":
        score += 20

    # Volatility
    if vix_regime == "HIGH_VOL":
        score += 15

    if vix_regime == "NORMAL_VOL":
        score += 10

    # Order flow
    if order_flow > 0:
        score += 15

    # Institutional positioning
    if inst_pos == "BULLISH_POSITIONING":
        score += 15

    if inst_pos == "BEARISH_POSITIONING":
        score += 15

    return score