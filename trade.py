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
import oandapyV20.endpoints.positions as positions
import loging
import calcrate
import long
import short
import week_day



accountID = "101-009-12442824-001"
access_token = '0b5e9a483d41290d2f4bce8fe189cf60-b997a98f78c139397b4f87d24775ff31'





api = API(access_token = access_token)
params = {
  "count": 2300,
  "granularity": "S10"
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
rate.to_csv('test.csv')



#グラフ表示はじまり
xdata = []
ydata = []
data = pd.read_csv('test.csv', header = None, names=['o','h','i','c'])
yd = data['c']

for i in range(len(yd)-1):
  ydata.append(data['c'][i])
  xdata.append(i+1)
y = ydata
x = xdata
line, = plt.plot(x, y)

plt.xlim([2280,2310])
plt.ylim([-300,300])
plt.yticks( [0, 200, 20] )
plt.pause(.01)

#グラフ表示終わり



value = 1

print("       初期データ読み込み完了")
st_per = 'NULL';
i = 1;
running = 1;
while running == 1:

  weekday = week_day.day()

  if weekday == 'Saturday' or weekday == 'Sunday'
    print("本日は相場がお休みです")
  else
    print("[STEP" + str(i) + "]")
    dt_now = datetime.datetime.now()
    print(dt_now)
    if st_per == 'NULL':
      print("       売買判断開始")
      st_per = calcrate.cal()
      print("       売買判断終了")
      time.sleep(10)
    elif st_per == "long_position":
      print("       現在longポジションを持っています")
      order_long = orders.OrdersPending(accountID)
      api.request(order_long)
      if len(order_long.response['orders']) <= 1:
        print("    決済されました")
        print("       もう一方の予約注文をキャンセルします")
        e_id = order_long.response['orders'][0]['id']
        l = orders.OrderCancel(accountID=accountID, orderID=e_id)
        api.request(l)
        st_per = 'NULL'
      time.sleep(10)
    elif st_per == "short_position":
      print("       現在shortポジションを持っています")
      order = orders.OrdersPending(accountID)
      api.request(order)
      if len(order.response['orders']) <= 1:
        print("    決済されました")
        print("       もう一方の予約注文をキャンセルします")
        e_id = order.response['orders'][0]['id']
        l = orders.OrderCancel(accountID=accountID, orderID=e_id)
        api.request(l)
        st_per = 'NULL'
      time.sleep(10)
    

    last_data = loging.update()

    xcount = 2300 + i
    y.append(last_data)
    x.append(xcount)

    print(len(y))
    print(len(x))
    line.set_data(x,y)
    plt.xlim([2280 + i,2310 + i])
    plt.ylim([-300,300])
    plt.yticks( [0, 200, 20] )
    plt.pause(.01)
    
    i = i+1;
  


  