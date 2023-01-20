import nsepy
from datetime import date
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
# Set the start and end dates for the historical data

end_date = date.today()
start_date = date(end_date.year - 10, 1, 1)
# Set the symbol for the stock you want to download data for
symbol = "INFY"

# Use the get_history function to download the data
data = nsepy.get_history(symbol=symbol,
                         start=start_date,
                         end=end_date)

# Print the data
print(data)

df = data.copy(deep=True)
df.reset_index(inplace=True)
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

fig.show()