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
  data2 = pd.read_csv('test.csv', header = None, names=['o','h','i','c'])
  now = data2['c'][-1]
  min_val = now
  max_val = now
  for i in range(50):
    if float(min_val) > float(data2['c'][-i-1]):
      min_val = float(data2['c'][-i-1])
    if float(max_val) < float(data2['c'][-i-1]):
      max_val = float(data2['c'][-i-1])
  i = 0;
      

  print("  最大値は" + str(max_val))
  print("  最小値は" + str(min_val))
  print("  現在値は" + str(now))
  #print("  現在値は" + now)

  if float(now) >= float(max_val):
    print("    買います")
    long.order(now)
    position_sta = "long_position"
    return position_sta
  elif float(now) <= float(min_val):
    print("    売ります")
    short.order(now)
    position_sta = "short_position"
    return position_sta
  print("    変化なし")
  val = 'NULL'
  return val

    

