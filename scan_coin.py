# https://github.com/brian-the-dev/python-tradingview-ta
# https://tradingview.brianthe.dev/
# https://tvdb.brianthe.dev/

from tradingview_ta import TA_Handler, Interval, Exchange
import re
import time
import os
#######################################################

# https://www.binance.com/en/markets/futures-perpetual

coin_top1_list = [
# 'SOLUSDT',
# 'XRPUSDT',

'NEARUSDT',
'XLMUSDT',
'ARBUSDT',

'TRXUSDT',
'LTCUSDT',
'HBARUSDT',
'DOTUSDT',

'APTUSDT',
'AAVEUSDT',
'PEPEUSDT',
'UNIUSDT',

'OMUSDT',
'SHIBUSDT',
'TONUSDT',
'LINKUSDT',


]


# For futute
coin_top2_list = [

'VETUSDT',
'SUSDT',
'ALGOUSDT',
'OPUSDT',
'ATOMUSDT',
'NEOUSDT',
'FLOWUSDT',


# Launchpool 
# 'SUIUSDT',

'SEIUSDT',
'MOVEUSDT',
# 'BERAUSDT',

# DeFi


# 'DEXEUSDT',
'ENAUSDT',
# 'CRVUSDT',

# Monitoring 
# 'JASMYUSDT',

# Liquid Staking
'LDOUSDT',


# Infrastructure 

'TIAUSDT',
'ENSUSDT',
'QNTUSDT',
# 'KAITOUSDT',

# BNB Ecosystem
# 'BNBUSDT',
'CAKEUSDT',

# Meme coin
# 'DOGEUSDT',


'MEMEUSDT',
'TRUMPUSDT',
'WIFUSDT',

# RWA tokens
'AVAXUSDT',

'MKRUSDT',
'ICPUSDT',

# NFT
'IMXUSDT',
'GALAUSDT',
'APEUSDT',

# Solana Ecosystem Tokens
'JUPUSDT',
'RENDERUSDT',
'RAYUSDT',
'PYTHUSDT',
'JTOUSDT',

## AI
'TAOUSDT',
'WLDUSDT',
'FETUSDT',
'INJUSDT',
'THETAUSDT',
'GRTUSDT',


## Metaverse
'AXSUSDT',
'SANDUSDT',
'MANAUSDT',

# Launchpad Tokens
'POLUSDT',
'EGLDUSDT',


# Storage
'FILUSDT',
'STXUSDT',


#### Other coins

'DYDXUSDT',
'RUNEUSDT',

'TRBUSDT',
'BLURUSDT',
'SYNUSDT',
'CFXUSDT',
'MINAUSDT',
'MAGICUSDT',
'SUPERUSDT',



]

# INTERVAL_30_MINUTES, INTERVAL_1_HOUR, INTERVAL_4_HOURS, INTERVAL_1_DAY
# TIME_FRAME = Interval.INTERVAL_30_MINUTES
TIME_FRAME = Interval.INTERVAL_1_DAY

if TIME_FRAME == Interval.INTERVAL_4_HOURS or TIME_FRAME == Interval.INTERVAL_1_DAY:
    BIEN_DUOI = 0.96
    BIEN_TREN = 1.05

if TIME_FRAME == Interval.INTERVAL_30_MINUTES:
    BIEN_DUOI = 0.98
    BIEN_TREN = 1.02

#############################################

def got_sideway(indictors_data):

    # Get Bollinger Bands values
    upper_band = indictors_data.indicators["BB.upper"]
    lower_band = indictors_data.indicators["BB.lower"]
    close_price = indictors_data.indicators["close"]

    # Define the criteria for sideways market
    band_width = (upper_band - lower_band) / close_price

    # Check if the Bollinger Bands width is below a certain threshold (e.g., 0.05)
    if band_width < 0.05:
        return True


def macd_top1():
    for coin in coin_top1_list:
        # print("===>" + coin)
        time.sleep(1)
        handler = TA_Handler(
            symbol=coin,
            screener="CRYPTO",
            exchange="BINANCE",
            interval=TIME_FRAME,
        )
        indictors_data = handler.get_analysis()

        # EMA data
        ema34_price = float(indictors_data.indicators["EMA30"])
        ema89_price = float(indictors_data.indicators["EMA100"])
        ema200_price = float(indictors_data.indicators["EMA200"])

        # Nếu 3 đường EMA 34, 89, 200 tụ lại
        if (BIEN_DUOI < (ema34_price / ema89_price) < BIEN_TREN) and (BIEN_DUOI < (ema34_price / ema200_price) < BIEN_TREN):
            print("\n*** 3 EMA tu lai: " + str(coin) + " " + str(ema34_price / ema200_price))
            
            continue

        # Nếu 2 đường EMA 34, 89 tụ lại
        if (BIEN_DUOI < (ema34_price / ema89_price) < (BIEN_TREN + 0.01)):
            print("Follow: " + str(coin) + " " + str(ema34_price / ema89_price))
            

        ###### Check sideway
        if (got_sideway(indictors_data)):
            print("Sideway: " + str(coin) + "\n")           



def macd_top2():
    print("\n======================================")
    print("\n========= Altcoin need check 30p, 4h chart =========")
    print("\n========= Altcoin need have Big Vol =========\n")
    for coin in coin_top2_list:
        if os.environ.get('DEBUG_MODE') == "true":
            print("===>" + coin)
        time.sleep(1)
        handler = TA_Handler(
            symbol=coin,
            screener="CRYPTO",
            exchange="BINANCE",
            interval=TIME_FRAME,
        )
        indictors_data = handler.get_analysis() 

        # EMA data
        ema34_price = float(indictors_data.indicators["EMA30"])
        ema89_price = float(indictors_data.indicators["EMA100"])
        ema200_price = float(indictors_data.indicators["EMA200"])

        # Nếu 3 đường EMA 34, 89, 200 tụ lại
        if (BIEN_DUOI < (ema34_price / ema89_price) < BIEN_TREN) and (BIEN_DUOI < (ema34_price / ema200_price) < BIEN_TREN):
            print("\n*** 3 EMA tu lai: " + str(coin) + " " + str(ema34_price / ema200_price) + "\n")
            
            continue

        # Nếu 2 đường EMA 34, 89 tụ lại
        if (BIEN_DUOI < (ema34_price / ema89_price) < (BIEN_TREN + 0.01)):
            print("Follow: " + str(coin) + " " + str(ema34_price / ema89_price))
            

        ###### Check sideway
        if (got_sideway(indictors_data)):
            print("Sideway: " + str(coin) + "\n")

#################################################################################

def main():
    macd_top1()
    macd_top2()

if __name__ == '__main__':
    main()
