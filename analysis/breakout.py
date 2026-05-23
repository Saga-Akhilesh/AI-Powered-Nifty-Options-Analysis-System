def detect_breakout(df):

    last_close = df["close"].iloc[-1]

    highest = df["high"].rolling(20).max().iloc[-2]
    lowest = df["low"].rolling(20).min().iloc[-2]

    if last_close > highest:
        return "BREAKOUT"

    if last_close < lowest:
        return "BREAKDOWN"

    return "NO_SIGNAL"