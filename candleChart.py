import yfinance as yf
from datetime import datetime
from dateutil import relativedelta
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
# Current date
current_date = datetime.now() + relativedelta.relativedelta(days=-1)

# Calculate 90 days ago from the current date
ninety_days_ago = current_date + relativedelta.relativedelta(days=-90)

print(ninety_days_ago)
# list of stocks in NIFTY 50 index
stock_list = ["RELIANCE.NS"]#,"HDFCBANK.NS"]#,"TCS.NS","SUNPHARMA.NS","HINDUNILVR.NS",
              #"HDFC.NS","KOTAKBANK.NS","ITC.NS","L&TFH.NS","ICICIBANK.NS"]

# Download historical data for each stock in the list
nifty50_data = {}
for stock in stock_list:
    nifty50_data[stock] = yf.download(stock, start=ninety_days_ago, end=current_date)

# Resample nifty50_data to monthly, weekly, and daily intervals
for stock in stock_list:
    nifty50_data[stock+'_monthly'] = nifty50_data[stock].resample('M').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'})
    nifty50_data[stock+'_weekly'] = nifty50_data[stock].resample('W').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'})
    nifty50_data[stock+'_daily'] = nifty50_data[stock]

# Plot the monthly candle chart using Matplotlib
# Plot the daily candlestick chart for each stock
for stock, data in nifty50_data.items():
    fig, ax = plt.subplots(figsize =(10,5))
    candlestick_ohlc(ax, zip(mdates.date2num(data.index.to_pydatetime()), data['Open'], data['High'], data['Low'], data['Close']), width=.6, colorup='green', colordown='red')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.set_title(f'{stock} Candlestick Chart')
    plt.show()
