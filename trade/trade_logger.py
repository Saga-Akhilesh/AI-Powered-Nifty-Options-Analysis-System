import csv
import os
from datetime import datetime

FILE_NAME = "trades.csv"


def log_trade(signal, strike, entry, stoploss, target, regime, breakout):

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "time",
                "signal",
                "strike",
                "entry",
                "stoploss",
                "target",
                "regime",
                "breakout"
            ])

        writer.writerow([
            datetime.now(),
            signal,
            strike,
            entry,
            stoploss,
            target,
            regime,
            breakout
        ])