import pandas as pd
import matplotlib.pyplot as plt
import mpl_finance as mpf
from matplotlib import ticker
import datetime
import matplotlib.dates as mdates
from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments


accountID = "101-009-12442824-001"
access_token = '0b5e9a483d41290d2f4bce8fe189cf60-b997a98f78c139397b4f87d24775ff31'
api = API(access_token = access_token)
def update():
  print("  データ更新中")
  params = {
    "count": 1,
    "granularity": "S10"
  }

  print("ok1")
  r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
  api.request(r)
  print(api.request(r))
  r.response['candles'][0]

  rate = pd.DataFrame.from_dict({r.response['candles'][i]['time']: r.response['candles'][i]['mid']
                            for i in range(0,len(r.response['candles']))
                            for j in r.response['candles'][i]['mid'].keys()},
                        orient='index',
                        )
  rate.index = pd.to_datetime(rate.index)
  
  rate.head()
  with open('test.csv', 'a') as f:
    print(r.response['candles'][0]['time'] + ",", r.response['candles'][0]['mid']['o'] + "," , r.response['candles'][0]['mid']['h'] + "," , r.response['candles'][0]['mid']['l'] + ",", r.response['candles'][0]['mid']['c'] + "," , file=f)
    f.close()

  return r.response['candles'][0]['mid']['c']
  #rate.to_csv('test.csv')
  #candle.candlechart(rate)