import beepy as beep
from binance.client import Client
import sched, time
from datetime import datetime,timezone

beep.beep('ready')
s = sched.scheduler(time.time, time.sleep)

def do_something(sc):

    client = Client()
    tickers = client.futures_ticker()
    for hightick in tickers:  # if BTC 24h getting high
            if hightick['symbol'] == "BTCUSDT" and float(hightick['priceChangePercent']) > -1:
                #os.system('clear')
                print(":: "+datetime.utcnow().strftime("%Y %b %d %a %H:%M:%S")+" :: % "+'{:.2f}'.format(float(
                    hightick['priceChangePercent']))+" :: "+'{:.2f}'.format(float(hightick['highPrice']))+" :: "+'{:.2f}'.format(float(hightick['lastPrice']))+" ::")
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
                                    hightick['symbol']+" - "+str(hightick['lastPrice']))
                                #beep.beep('coin')
                                pass

    sc.enter(1, 1, do_something, (sc,))

s.enter(1, 1, do_something, (s,))
s.run()
