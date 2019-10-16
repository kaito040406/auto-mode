from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import pandas as pd
import time
import matplotlib.pyplot as plt
import mpl_finance as mpf
from matplotlib import ticker
import datetime
import oandapyV20.endpoints.orders as orders
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.accounts as accounts
import moniter
import oandapyV20.endpoints.positions as positions
import loging
import calcrate
import long
import short



accountID = "py701079"
access_token = '0b5e9a483d41290d2f4bce8fe189cf60-b997a98f78c139397b4f87d24775ff31'
api = API(access_token = access_token)
params = {
  "count": 500,
  "granularity": "M1"
}
r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
api.request(r)

r.response['candles'][0]

rate = pd.DataFrame.from_dict({r.response['candles'][i]['time']: r.response['candles'][i]['mid']
                           for i in range(0,len(r.response['candles']))
                           for j in r.response['candles'][i]['mid'].keys()},
                       orient='index',
                      )

rate.index = pd.to_datetime(rate.index)
rate.head()
#candle.candlechart(rate)
rate.to_csv('test.csv')
value = 1


st_per = NULL;
i = 0;
running = 1;
while running == 1:
  if st_per == NULL:
    st_par = calcrate.()
    print(st_par)
    time.sleep(60)
  elif st_per == "long_position":
    order = orders.OrdersPending(accountID)
    api.request(order)
    if len(order.response['orders']) == 1:
      e_id = r.response['lastTransactionID']
      r = orders.OrderCancel(accountID=accountID, orderID=e_id)
      api.request(r)
    time.sleep(60)
  elif st_per == "short_position":
    order = orders.OrdersPending(accountID)
    api.request(order)
    if len(order.response['orders']) == 1:
      e_id = r.response['lastTransactionID']
      r = orders.OrderCancel(accountID=accountID, orderID=e_id)
      api.request(r)
    time.sleep(60)
  else:
    pass
  i = i+1;