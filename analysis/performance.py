import pandas as pd
import os


def analyze_performance():

    if not os.path.exists("trades.csv"):
        print("No trades logged yet.")
        return

    df = pd.read_csv("trades.csv")

    total_trades = len(df)

    print("Total Trades:", total_trades)

    print("\nSignals Distribution:")
    print(df["signal"].value_counts())

    print("\nBreakout signals:")
    print(df["breakout"].value_counts())

    print("\nRegime distribution:")
    print(df["regime"].value_counts())