import pandas as pd
import matplotlib.pyplot as plt
import mpl_finance as mpf
from matplotlib import ticker
import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

xdata = []
data = pd.read_csv('test.csv', header = None, names=['o','h','i','c'])


y = data['c']

for i in range(len(y)):
  xdata.append(i+1)

x = xdata


plt.plot(x, y)
plt.show()