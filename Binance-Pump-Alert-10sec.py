import beepy as beep
from binance.client import Client
import sched, time
from datetime import datetime,timezone

s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    print("10 seconds passed..."+" - "+str(datetime.now(timezone.utc)))

    client = Client()
    tickers = client.get_ticker()
    for ticker in tickers:
        if ticker['symbol'][-4:] == "USDT" and float(ticker['priceChangePercent']) > 0:
            if ticker['lastPrice'] == ticker['highPrice']:
                if ticker['symbol'] == "BUSDUSDT":
                    print("Banned symbol"+" "+ticker['symbol']) 
                else:
                    print(ticker['symbol']+" - "+ticker['lastPrice'])
                    beep.beep('coin')

    sc.enter(10, 1, do_something, (sc,))

s.enter(10, 1, do_something, (s,))
s.run()
