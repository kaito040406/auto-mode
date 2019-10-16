import pandas as pd
import matplotlib.pyplot as plt
import mpl_finance as mpf
from matplotlib import ticker
import datetime
import matplotlib.dates as mdates
from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import csv
import long
import short

def cal():
  sum = 0
  data = pd.read_csv('test.csv', header = None, names=['o','h','i','c'])
  min = data['c'][-2]
  max = data['c'][-2]
  now = data['c'][-1]
  for i in range(2, 201):
    sum = sum + float(data['c'][-i])

    if min > data['c'][-i+1]:
      min = data['c'][-i+1]

    if max < data['c'][-i+1]:
      max = data['c'][-i+1]

  ave = float(sum)/199


  if now > max:
    print("買います")
    long.order(now)
    position_sta = "long_position"
    return position_sta
  elif now < min:
    print("売ります")
    short.order(now)
    position_sta = "short_position"
    return position_sta
  print("変化なし")

  return NULL

    

