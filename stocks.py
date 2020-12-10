import yfinance as yf
import matplotlib.pyplot as plt
import Tkinter
from collections import defaultdict

msft = yf.Ticker("AAPL")
info = msft.info

history = msft.history(period="max")

dates = []
prices = []
for key, value in history.items():
	if key == "Open":
		dd = defaultdict(list)
		arr = value.to_dict(dd)

		for k, v in arr.items():
			k = str(k)[0:10]
			dates.append(k)
			prices.append(v)

plt.plot(dates, prices)
plt.ylabel('numbers')
plt.show()


