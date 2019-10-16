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



accountID = "py701079"
access_token = '0b5e9a483d41290d2f4bce8fe189cf60-b997a98f78c139397b4f87d24775ff31'
api = API(access_token = access_token)
params = {
  "count": 1000,
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



i = 0;
running = 1;
while running == 1:
  
  time.sleep(60)
  api = API(access_token=access_token, environment="practice")
  params = {
      "count": 1,
      "granularity": "M1"
  }
  r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
  api.request(r)
  data = []
  for raw in r.response['candles']:
      data.append([raw['time'], raw['volume'], raw['mid']['o'], raw['mid']['h'], raw['mid']['l'], raw['mid']['c']])
  df = pd.DataFrame(data)
  moniter.cal(raw['mid']['o'], raw['mid']['h'], raw['mid']['l'], raw['mid']['c'], i)
  df.columns = ['time', 'volume', 'open', 'high', 'low', 'close']
  df = df.set_index('time')
  df.index = pd.to_datetime(df.index)
  b = positions.PositionList(accountID=accountID)
  

  positions = oanda.get_positions(account_id)
  
  now_value = api.request(b)
  print(now_value ['positions'][0]['financing'])

  #print(df.tail())
  #api.request(r)
  
  i = i+1;