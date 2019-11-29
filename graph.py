import pandas as pd
import matplotlib.pyplot as plt
import mpl_finance as mpf
import matplotlib.ticker as ticker
import datetime
import matplotlib.dates as mdates


xdata = []
data = pd.read_csv('test.csv', header = None, names=['o','h','i','c'])


y = data['c']

for i in range(len(y)):
  xdata.append(i+1)

x = xdata
plt.plot(x, y)

plt.xlim([2000,2350])
plt.ylim([-300,300])
plt.yticks( [0, 200, 20] )

plt.show()
