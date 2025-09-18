import requests
import pandas as pd
import pandas_ta as ta  # Make sure this is installed: pip install pandas_ta

def get_btc_ema34():
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": "BTCUSDT",
        "interval": "4h",
        "limit": 100
    }
    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data, columns=[
        "timestamp", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base_volume", "taker_buy_quote_volume", "ignore"
    ])
    df["close"] = pd.to_numeric(df["close"])

    # Calculate EMA34 using pandas_ta
    df["EMA34"] = ta.ema(df["close"], length=34)
    return df["EMA34"].iloc[-1]

# Example usage
ema34_value = get_btc_ema34()
print(f"Current EMA34 for BTC: {ema34_value:.2f}")
