import os
import sched
import time
import beepy as beep
from termcolor import colored
from datetime import datetime
from unicorn_binance_rest_api.manager import BinanceRestApiManager

s = sched.scheduler(time.time, time.sleep)


def refresh(sc):
    beep.beep('ready')
    while True:
        try:
            ubra = BinanceRestApiManager(exchange="binance.com")
            tickers = ubra.get_ticker()
        except Exception as e:
            os.system('clear')
            print(colored("API Error. Restarting...", "red"))
            continue
        for printtick in tickers:  # only for print
            if printtick['symbol'] == "BTCUSDT" and float(printtick['priceChangePercent']) < -1:
                os.system('clear')
                print(datetime.utcnow().strftime("%Y %b %d %a %H:%M:%S")+"\n")
                print("BTC 24h Change %   " +
                      '{:.2f}'.format(float(printtick['priceChangePercent'])))
                print("BTC price Change   " +
                      '{:.2f}'.format(float(printtick['priceChange'])))
                print("BTC 24h Low Price  " +
                      '{:.2f}'.format(float(printtick['lowPrice'])))
                print("BTC 24h High Price " +
                      '{:.2f}'.format(float(printtick['highPrice'])))
                print("BTC Current Price  " +
                      '{:.2f}'.format(float(printtick['lastPrice']))+"\n")

        for hightick in tickers:  # if BTC 24h getting high
            if hightick['symbol'] == "BTCUSDT" and float(hightick['priceChangePercent']) > -1:
                print(colored(datetime.utcnow().strftime("%Y %b %d %a %H:%M:%S")+" - BTC Change % "+'{:.2f}'.format(float(
                    hightick['priceChangePercent']))+" - "+'{:.2f}'.format(float(hightick['highPrice']))+" - "+'{:.2f}'.format(float(hightick['lastPrice'])), 'green'))
                if hightick['symbol'] == "BTCUSDT" and hightick['lastPrice'] == hightick['highPrice']:
                    beep.beep('coin')
                for hightick in tickers:  # high crypto alert
                    if hightick['symbol'][-4:] == "USDT" and float(hightick['priceChangePercent']) > 0:
                        if hightick['lastPrice'] == hightick['highPrice']:
                            # crypto symbol pass
                            if hightick['symbol'] == "BUSDUSDT" or hightick['symbol'] == "EURUSDT" or hightick['symbol'] == "GBPUSDT":
                                pass
                            else:
                                print(
                                    colored(hightick['symbol']+" - "+str(float(hightick['lastPrice'])), 'green'))
                                beep.beep('coin')
                                pass

        sc.enter(2, 2, refresh, (sc,))


s.enter(2, 2, refresh, (s,))
s.run()
