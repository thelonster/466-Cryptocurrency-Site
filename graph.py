import requests
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def get_df(from_date, to_date, coin):
    """ Get historical price data between two dates. """
    date = to_date
    holder = []
    # While the earliest date returned is later than the earliest date requested, keep on querying the API
    # and adding the results to a list.
    while date > from_date:
        data = get_data(date, coin)
        holder.append(pd.DataFrame(data['Data']))
        date = data['TimeFrom']
    # Join together all of the API queries in the list.
    df = pd.concat(holder, axis = 0)
    # Remove data points from before from_date
    df = df[df['time']>from_date]
    # Convert to timestamp to readable date format
    df['time'] = pd.to_datetime(df['time'], unit='s')
    # Make the DataFrame index the time
    df.set_index('time', inplace=True)
    # And sort it so its in time order
    df.sort_index(ascending=False, inplace=True)
    return df


def get_data(date, coin):
    """ Query the API for 2000 days historical price data starting from "date". """
    url = "https://min-api.cryptocompare.com/data/histoday?fsym=" + coin + "&tsym=USD&limit=2000&toTs={}".format(date)
    r = requests.get(url)
    ipdata = r.json()
    return ipdata


to_date = 1514764800
from_date = 1560000000
df = get_df(to_date, from_date, "BTC")
fig, ax = plt.subplots(figsize=(15, 10))
ax.plot(df[['low', 'close', 'high']])
ax.set_ylabel('BTC Price (USD)')
ax.set_xlabel('Date')
ax.legend(['Low', 'Close', 'High']);
plt.show()

ethdf = get_df(to_date, from_date, "ETH")
fig2, ax2 = plt.subplots(figsize=(15, 10))
ax2.plot(ethdf[['low', 'close', 'high']])
ax2.set_ylabel('ETH Price (USD)')
ax2.set_xlabel('Date')
ax2.legend(['Low', 'Close', 'High']);
plt.show()

litedf = get_df(to_date, from_date, "LTC")
fig3, ax3 = plt.subplots(figsize=(15, 10))
ax3.plot(litedf[['low', 'close', 'high']])
ax3.set_ylabel('LTC Price (USD)')
ax3.set_xlabel('Date')
ax3.legend(['Low', 'Close', 'High']);
plt.show()
