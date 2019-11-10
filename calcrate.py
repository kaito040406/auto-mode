import pandas as pd
import matplotlib.pyplot as plt
import mpl_finance as mpf
from matplotlib import ticker
import datetime
import matplotlib.dates as mdates
from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import csv
import math
import long
import short

def cal():
  data2 = pd.read_csv('test.csv', header = None, names=['o','h','i','c'])
  now = data2['c'][-1]
  now_f = float(now)
  o_c_raw = float(data2['o'][-1]) - float(data2['c'][-1])
  o_c = round(o_c_raw, 3)
  print("  現在値は" + str(now))
  print("  変化量は" + str(o_c))



  #短期傾き算出はじまり
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

  coefficient_short = upper / under 
  
  print("   短期係数は:" + str(coefficient_short))
  #短期傾き算出おわり



  #中期傾き算出はじまり
  under = 0
  upper = 0
  under_cal = 0
  upper_cal = 0
  sum_x = 0
  sum_y = 0

  for i in range(1,801):
    sum_x = sum_x + i
    sum_y = sum_y + float(data2['c'][-i])

  ave_x = sum_x / 800
  ave_y = sum_y / 800

  for i in range(1,801):
    under_cal = ((-i) - ave_x) * ((-i) - ave_x)
    upper_cal = ((-i) - ave_x) * (float(data2['c'][-i]) - ave_y)
    under = under + under_cal
    upper = upper + upper_cal
    under_cal = 0
    upper_cal = 0

  coefficient_mid = upper / under 
  
  print("   中期係数は:" + str(coefficient_mid))
  #中期傾き算出おわり



  #長期傾き算出はじまり 単純移動平均も算出
  under = 0
  upper = 0
  under_cal = 0
  upper_cal = 0
  sum_x = 0
  sum_y = 0

  s_right = 0

  for i in range(1,2002):
    sum_x = sum_x + i
    sum_y = sum_y + float(data2['c'][-i])
    s_right = s_right + float(data2['c'][-i])

  ave_x = sum_x / 2001
  ave_y = sum_y / 2001

  for i in range(1,2002):
    under_cal = ((-i) - ave_x) * ((-i) - ave_x)
    upper_cal = ((-i) - ave_x) * (float(data2['c'][-i]) - ave_y)
    under = under + under_cal
    upper = upper + upper_cal
    under_cal = 0
    upper_cal = 0

  move_ave = (s_right)/2001
  coefficient_long = upper / under 
  
  print("   長期係数は:" + str(coefficient_long))
  print("   移動平均は:" + str(move_ave))
  #長期傾き算出おわり 単純移動平均も算出終わり




  #標準偏差算出始まり
  p = 0;
  m = 0;
  e = 0;
  h_p = 0;
  h_2p = 0;
  sum_pulas = 0;
  sum_mainasu = 0;
  delta = [];
  dt_sum = 0;
  right = 0;
  for i in range(0, 2200):
    h_p = i + 1;
    h_2p = i + 2;
    delta.append(float(data2['c'][-h_p])-float(data2['c'][-h_2p]))
    if delta[i] > 0:
      p = p + 1
      sum_pulas = sum_pulas + float(data2['c'][-h_p])
    
    elif delta[i] < 0:
      m = m + 1
      sum_mainasu = sum_mainasu + float(data2['c'][-h_p])
      delta[i] = delta[i] * (-1)
    dt_sum = dt_sum + delta[i];

  ave_puras = sum_pulas / p;
  ave_mainasu = sum_mainasu / m;
  ave_dt = dt_sum / 2200;

  for i in range(0,2200):
    right = right + (delta[i] - ave_dt) * (delta[i] - ave_dt)
    e = e + 1

  standard_deviation = math.sqrt(right/e)
  print("   1σ  ±" + str(standard_deviation))
  print("   2σ  ±" + str(2 * standard_deviation))
  print("   3σ  ±" + str(3 * standard_deviation))
  #標準偏差算出終わり



  #スキャルピング?モードはじまり 
  if float(o_c) >= 0.015 or float(o_c) <= -0.015:
    print("  スキャルピングモード突入")
    if float(o_c) >= 0.015:
      profit_trans = (0.052/0.036) * o_c * 0.8
      losscut_trans = 0.005
      print("    売ります")
      
      short.order(now_f, profit_trans, losscut_trans)
      position_sta = "short_position"
      return position_sta

    elif float(o_c) <= -0.015:
      profit_trans = (0.052/0.036) * o_c * 0.8
      losscut_trans = 0.005
      print("    買います")
      long.order(now_f, profit_trans, losscut_trans)
      position_sta = "long_position"
      return position_sta
  #スキャルピング?モード終わり




  #順張りモードはじまり
  else:
    #min_val = now
    #max_val = now
    #for j in range(2,20):
      #if float(min_val) > float(data2['c'][-j-1]):
        #min_val = float(data2['c'][-j-1])
      #if float(max_val) < float(data2['c'][-j-1]):
        #max_val = float(data2['c'][-j-1])
    #print("  最大値は" + str(max_val))
    #print("  最小値は" + str(min_val))
    #print("  現在値は" + now)
    if coefficient_short > 0 and coefficient_mid > 0 and coefficient_long > 0 and float(now) > float(move_ave):
      print("現在上昇トレンドです")
      #if float(now) >= float(max_val):
      if float(o_c) >= 0.001:
        print("    順張り購入")
        pr = 0.013
        lo = 0.010
        long.order(now_f, pr, lo)
        position_sta = "long_position"
        return position_sta

      else:
        print("    トレードを見送ります")
        val = 'NULL'
        return val
        #val = 'NULL'
        #return val
      #elif float(o_c) <= -0.003:
        #print("    順張り売却")
        #pr = 0.008
        #lo = 0.008
        #short.order(now, pr, lo)
        #position_sta = "short_position"
        #return position_sta
        
    elif coefficient_short < 0 and coefficient_mid < 0 and coefficient_long < 0 and float(now) < float(move_ave):
      print("   現在下降トレンドです")
      #if float(now) <= float(min_val):
      if float(o_c) <= -0.001:
        print("    順張り売却")
        pr = 0.013
        lo = 0.010
        short.order(now_f, pr, lo)
        position_sta = "short_position"
        return position_sta
        #val = 'NULL'
        #return val
      #elif float(o_c) <= -0.003:
        #print("    買います")
        #pr = 0.008
        #lo = 0.008
        #long.order(now, pr, lo)
        #position_sta = "long_position"
        #return position_sta
        #val = 'NULL'
        #return val
      else:
        print("    トレードを見送ります")
        val = 'NULL'
        return val

    else:
      if float(o_c) >= 3 * float(standard_deviation):
        print("    買います")
        pr = 0.010
        lo = 0.015
        long.order(now_f, pr, lo)
        position_sta = "long_position"
        return position_sta

      elif float(o_c) <= -3 * float(standard_deviation):
        print("    売ります")
        pr = 0.010
        lo = 0.015
        short.order(now_f, pr, lo)
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


 

    

