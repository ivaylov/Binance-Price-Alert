import os
import sched, time
import beepy as beep
import requests
import json
from datetime import datetime
from unicorn_binance_rest_api.manager import BinanceRestApiManager



s = sched.scheduler(time.time, time.sleep)
def refresh(sc):
    os.system('clear')
    request = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&ids=bitcoin&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h").text
    request = json.loads(request)
    btcprice = request[0]["current_price"]
    btc1hchange = request[0]["price_change_percentage_1h_in_currency"]
    market_cap = request[0]["market_cap"]
    print(datetime.utcnow().strftime("%a %b %d %H:%M:%S %Y")+" - "+"Bitcoin price is:", '{:.2f}'.format(btcprice), "1h change: %", '{:.2f}'.format(btc1hchange), "Market Cap:", '{:.2f}'.format(market_cap))
    print(f"\n")
    ubra = BinanceRestApiManager(exchange="binance.com")
    tickers = ubra.get_ticker()
    for ticker in tickers:
        if ticker['symbol'][-4:] == "USDT" and float(ticker['priceChangePercent']) > 0:
            if ticker['lastPrice'] == ticker['highPrice'] and btc1hchange > 1:
                if ticker['symbol'] == "BUSDUSDT":
                    print(ticker['symbol']+" - "+"Banned symbol")
                else:
                    print(ticker['symbol']+" - "+ticker['lastPrice'])
                    beep.beep('coin')

    sc.enter(1, 1, refresh, (sc,))

s.enter(1, 1, refresh, (s,))
s.run()
