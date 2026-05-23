import pandas as pd
import ta


def detect_regime(df):

    if df is None or len(df) < 50:
        return "UNKNOWN"

    # EMA trend
    df["ema20"] = ta.trend.ema_indicator(df["close"], window=20)
    df["ema50"] = ta.trend.ema_indicator(df["close"], window=50)

    # ADX (trend strength)
    df["adx"] = ta.trend.adx(df["high"], df["low"], df["close"], window=14)

    last = df.iloc[-1]

    # Strong trend
    if last["ema20"] > last["ema50"] and last["adx"] > 25:
        return "BULLISH"

    if last["ema20"] < last["ema50"] and last["adx"] > 25:
        return "BEARISH"

    # Sideways
    if last["adx"] < 20:
        return "SIDEWAYS"

    return "NEUTRAL"