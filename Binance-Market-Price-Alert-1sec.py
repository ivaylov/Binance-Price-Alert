import os
import sched, time
import beepy as beep
from datetime import datetime,timezone
from binance.client import Client
from unicorn_binance_rest_api.manager import BinanceRestApiManager

s = sched.scheduler(time.time, time.sleep)
def refresh(sc):
    os.system('clear')
    print("1 seconds passed..."+" - "+str(datetime.now(timezone.utc)))
    ubra = BinanceRestApiManager(exchange="binance.com")
    tickers = ubra.get_ticker()
    for ticker in tickers:
        if ticker['symbol'][-4:] == "USDT" and float(ticker['priceChangePercent']) > 0:
            if ticker['lastPrice'] == ticker['highPrice']:
                if ticker['symbol'] == "BUSDUSDT":
                    print(ticker['symbol']+" - "+"Banned symbol")
                else:
                    print(ticker['symbol']+" - "+ticker['lastPrice'])
                    beep.beep('coin')

    sc.enter(1, 1, refresh, (sc,))

s.enter(1, 1, refresh, (s,))
s.run()
