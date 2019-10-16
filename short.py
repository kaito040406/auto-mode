from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.positions as positions

accountID = "101-009-12442824-001"
access_token = '0b5e9a483d41290d2f4bce8fe189cf60-b997a98f78c139397b4f87d24775ff31'

def order(now_price, sta):
  profit = float('{:.2g}'.format(now_price)) - 0.7
  losscut = float('{:.2g}'.format(now_price)) + 0.7
  api = API(access_token=access_token, environment="practice")
  params = { "instruments": "EUR_USD,EUR_JPY,USD_JPY" }
  r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
  api.request(r)

  data =  {
      "order": {
        "instrument": "USD_JPY",
        "units": "-5000",
        "type": "MARKET",
        "positionFill": "DEFAULT"
      }
  }
  r = orders.OrderCreate(accountID, data=data)
  api.request(r)

  data = {
    "order": {
      "price" : profit,
      "instrument": "USD_JPY",
      "units": "+5000",
      "type": "LIMIT",
      "positionFill": "DEFAULT"
    }
  }
  r = orders.OrderCreate(accountID, data=data)
  api.request(r)

  data = {
    "order": {
      "price" : losscut,
      "instrument": "USD_JPY",
      "units": "+5000",
      "type": "LIMIT",
      "positionFill": "DEFAULT"
    }
  }
  r = orders.OrderCreate(accountID, data=data)
  api.request(r)

  sta = short_position