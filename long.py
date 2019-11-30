from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.positions as positions
import os


accountID = os.environ.get("OANDA_ID")
access_token = os.environ.get("OANDA_TOKEN")

def order(now_price, profit_trans, losscut_trans):
  profit = float(now_price) + profit_trans
  losscut = float(now_price) - losscut_trans
  profit_round = round(profit, 4)
  losscut_round = round(losscut, 4)
  print("利確は" + str(profit_round))
  print("損切は" + str(losscut_round))
  api = API(access_token=access_token, environment="practice")
  params = { "instruments": "USD_JPY" }
  r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
  api.request(r)

  data =  {
      "order": {
        "instrument": "USD_JPY",
        "units": "+5000",
        "type": "MARKET",
        "positionFill": "DEFAULT"
      }
  }
  n = orders.OrderCreate(accountID, data=data)
  api.request(n)

  data = {
    "order": {
      "price" : str(profit_round),
      "instrument": "USD_JPY",
      "units": "-5000",
      "type": "LIMIT",
      "positionFill": "DEFAULT"
    }
  }
  m = orders.OrderCreate(accountID, data=data)
  api.request(m)

  data = {
    "order": {
      "price" : str(losscut_round),
      "instrument": "USD_JPY",
      "units": "-5000",
      "type": "LIMIT",
      "positionFill": "DEFAULT"
    }
  }
  v = orders.OrderCreate(accountID, data=data)
  api.request(v)