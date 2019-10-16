import pandas as pd
import matplotlib.pyplot as plt
import mpl_finance as mpf
from matplotlib import ticker
import datetime
import matplotlib.dates as mdates
from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import candle
import time


accountID = "py701079"
access_token = '0b5e9a483d41290d2f4bce8fe189cf60-b997a98f78c139397b4f87d24775ff31'

api = API(access_token = access_token)


def update():
  params = {
    "count": 1,
    "granularity": "M1"
  }

  r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
  api.request(r)

  r.response['candles'][0]

  print(r.response['candles'][0]['mid']['o'])

  rate2 = pd.DataFrame.from_dict({r.response['candles'][i]['time']: r.response['candles'][i]['mid']
                            for i in range(0,len(r.response['candles']))
                            for j in r.response['candles'][i]['mid'].keys()},
                        orient='index',
                        )
  rate2.index = pd.to_datetime(rate2.index)
  
  rate.head()

  with open('test.csv', 'a') as f:
    print(r.response['candles'][0]['time'] + ",", r.response['candles'][0]['mid']['o'] + "," , r.response['candles'][0]['mid']['h'] + "," , r.response['candles'][0]['mid']['l'] + ",", r.response['candles'][0]['mid']['c'] + "," , file=f)
    f.close()

  #rate.to_csv('test.csv')
  #candle.candlechart(rate)