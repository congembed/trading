import requests
import pandas as pd
import pandas_ta as ta

# Fetch BTC/USDT 1h klines (last 100 candles)
url = "https://api.binance.com/api/v3/klines"
params = {
    "symbol": "BTCUSDT",
    "interval": "1h",
    "limit": 100
}
response = requests.get(url, params=params)
data = response.json()

# Convert to DataFrame
columns = [
    "open_time", "open", "high", "low", "close", "volume",
    "close_time", "quote_asset_volume", "number_of_trades",
    "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
]
df = pd.DataFrame(data, columns=columns)
df["close"] = df["close"].astype(float)

# Calculate EMA34
df["EMA34"] = ta.ema(df["close"], length=34)

# Get the latest EMA34 value
latest_ema34 = df["EMA34"].iloc[-1]
print("Latest EMA34 value:", latest_ema34)