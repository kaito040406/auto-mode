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
  o_c_raw = float(data2['o'][-1]) - float(data2['c'][-1])
  o_c = round(o_c_raw, 3)
  print("  現在値は" + str(now))
  print("  変化量は" + str(o_c))
  under = 0
  upper = 0
  under_cal = 0
  upper_cal = 0
  sum_x = 0
  sum_y = 0

  for i in range(1,31):
    sum_x = sum_x + i
    sum_y = sum_y + float(data2['c'][-i])

  ave_x = sum_x / 30
  ave_y = sum_y / 30

  for i in range(1,31):
    under_cal = ((-i) - ave_x) * ((-i) - ave_x)
    upper_cal = ((-i) - ave_x) * (float(data2['c'][-i]) - ave_y)
    under = under + under_cal
    upper = upper + upper_cal
    under_cal = 0
    upper_cal = 0

  coefficient = upper / under 
  
  print("   係数は:" + str(coefficient))

  #スキャルピング?モードはじまり 
  if float(o_c) >= 0.02 or float(o_c) <= -0.02:
    if float(o_c) >= 0.02:
      profit_trans = (0.052/0.036) * o_c * 0.8
      losscut_trans = 0.005
      print("    売ります")
      short.order(now, profit_trans, losscut_trans)
      position_sta = "short_position"
      return position_sta

    elif float(o_c) <= -0.02:
      profit_trans = (0.052/0.036) * o_c * 0.8
      losscut_trans = 0.005
      print("    買います")
      long.order(now, profit_trans, losscut_trans)
      position_sta = "long_position"
      return position_sta
  #スキャルピング?モード終わり

  #順張りモードはじまり
  else:
    min_val = now
    max_val = now
    for j in range(2,40):
      if float(min_val) > float(data2['c'][-j-1]):
        min_val = float(data2['c'][-j-1])
      if float(max_val) < float(data2['c'][-j-1]):
        max_val = float(data2['c'][-j-1])
    
    #print("  最大値は" + str(max_val))
    #print("  最小値は" + str(min_val))
    #print("  現在値は" + now)
    if coefficient > 0:
      print("現在上昇トレンドです")
      if float(now) >= float(max_val):
        print("    買います")
        pr = 0.010
        lo = 0.008
        long.order(now, pr, lo)
        position_sta = "long_position"
        return position_sta
    elif coefficient < 0:
      print("現在下降トレンドです")
      if float(now) <= float(min_val):
        print("    売ります")
        pr = 0.010
        lo = 0.008
        short.order(now, pr, lo)
        position_sta = "short_position"
        return position_sta

  print("    今は売買しません")
  val = 'NULL'
  return val

    

  #if float(now) >= float(max_val):
    #print("    買います")
    #long.order(now)
    #position_sta = "long_position"
    #return position_sta
  #elif float(now) <= float(min_val):
    #print("    売ります")
    #short.order(now)
    #position_sta = "short_position"
    #return position_sta
  #print("    変化なし")
  #val = 'NULL'
  #return val

  #最小最大値理論おわり


 

    

