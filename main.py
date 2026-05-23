import time

from data.market_data import get_nifty_price
from data.option_chain import fetch_option_chain

from analysis.regime_detection import detect_regime
from analysis.oi_analysis import analyze_oi
from analysis.breakout import detect_breakout

from ai.signal_engine import generate_signal

from trade.strike_selector import select_strikes
from trade.risk_manager import calculate_levels

from alerts.telegram_bot import send_alert
from analysis.market_status import market_is_open
from data.market_data import get_nifty_candles
from data.option_chain import get_option_premium
from trade.trade_logger import log_trade
from analysis.gamma_wall import detect_gamma_walls
from analysis.liquidity_sweep import detect_liquidity_sweep
from analysis.order_flow import order_flow_imbalance
from analysis.institutional_flow import institutional_positioning
from analysis.vix_filter import get_india_vix, vix_regime
from ai.confidence_score import calculate_confidence


def run_bot():

    status, reason = market_is_open()

    if not status:
        print(f"Market closed: {reason}")
        return

    print("Running Nifty AI...")

    price = get_nifty_price()
    print("Nifty Price:", price)

    # VIX
    vix = get_india_vix()
    regime_vix = vix_regime(vix)

    print("India VIX:", vix)
    print("Volatility Regime:", regime_vix)

    # OPTION CHAIN
    option_chain = fetch_option_chain()

    oi_data = analyze_oi(option_chain)

    print("Support:", oi_data["support"])
    print("Resistance:", oi_data["resistance"])

    # CANDLES
    candles = get_nifty_candles()

    if candles is None:
        print("No candle data available")
        return

    # MARKET REGIME
    regime = detect_regime(candles)
    print("Market Regime:", regime)

    # BREAKOUT
    breakout = detect_breakout(candles)
    if breakout is None:
        breakout = "NO_SIGNAL"

    print("Breakout Signal:", breakout)

    # SMART MONEY
    gamma = detect_gamma_walls(option_chain)
    print("Gamma Walls:", gamma)

    sweep = detect_liquidity_sweep(candles)
    print("Liquidity Sweep:", sweep)

    flow = order_flow_imbalance(option_chain)
    print("Order Flow:", flow)

    inst = institutional_positioning(option_chain)
    print("Institutional Positioning:", inst)

    # CONFIDENCE (AFTER EVERYTHING)
    confidence = calculate_confidence(regime, breakout, regime_vix, flow, inst)
    print("Confidence Score:", confidence)

    # SIGNAL (generate early)
    sentiment = 0
    signal = generate_signal(regime, breakout, sentiment)

    print("Generated Signal:", signal)

# STRIKE (always calculate)
    strike = select_strikes(signal, price)
    print("Suggested Strike:", strike)

# CONFIDENCE CHECK
    if confidence < 60:
      print("Low confidence trade → Avoid")
      return

    # SIGNAL
    sentiment = 0
    signal = generate_signal(regime, breakout, sentiment)

    print("Generated Signal:", signal)

    if signal == "NO_TRADE":
        print("No trade signal")
        return

    # STRIKE
    strikes = select_strikes(signal, price)

    print("Strike Suggestions:")
    print("Safe (ATM):", strikes["safe"])
    print("Aggressive (OTM):", strikes["aggressive"])
    print("Conservative (ITM):", strikes["conservative"])

    # PREMIUM
    safe_strike_value = int(strikes["safe"].split()[0])

    entry = get_option_premium(option_chain, safe_strike_value, signal)

    if entry is None:
        print("Could not fetch option premium")
        return

    # RISK
    levels = calculate_levels(entry)

    message = f"""
NIFTY AI SIGNAL

Direction: {signal}

Strikes:
Safe (ATM): {strikes['safe']}
Aggressive (OTM): {strikes['aggressive']}
Conservative (ITM): {strikes['conservative']}

Entry: {levels['entry']}
Stoploss: {levels['stoploss']}
Target: {levels['target']}

Confidence: {confidence}%

Regime: {regime}
Breakout: {breakout}
VIX: {regime_vix}
"""

    send_alert(message)

    log_trade(
        signal,
        strike,
        levels["entry"],
        levels["stoploss"],
        levels["target"],
        regime,
        breakout
    )

    print(message)


while True:

    run_bot()

    time.sleep(300)