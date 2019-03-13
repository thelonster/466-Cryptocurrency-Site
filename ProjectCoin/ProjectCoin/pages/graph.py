import requests
import pandas as pd
import json
from datetime import datetime, timezone

def get_df(from_date, to_date, coin, datatype):
    """ Get historical price data between two dates. """
    date = to_date
    holder = []
    if datatype == "day":
        # While the earliest date returned is later than the earliest date requested, keep on querying the API
        # and adding the results to a list.
        while date > from_date:
            data = get_daily_data(date, coin)
            holder.append(pd.DataFrame(data['Data']))
            date = data['TimeFrom']
    elif datatype == "hour":
        # Hourly data for the last 24 hours
        data = get_hourly_data(coin)
        holder.append(pd.DataFrame(data['Data']))
        date = data['TimeFrom']
    elif datatype == "minute":
        # Minute data from the last 60 minutes
        data = get_minute_data(coin)
        holder.append(pd.DataFrame(data['Data']))
        date = data['TimeFrom']
    # Join together all of the API queries in the list.
    df = pd.concat(holder, axis = 0)
    # Remove data points from before from_date
    df = df[df['time']>=from_date]
    # Convert to timestamp to readable date format
    df['time'] = pd.to_datetime(df['time'], unit='s')
    # Make the DataFrame index the time
    df.set_index('time', inplace=True)
    # And sort it so its in time order
    df.sort_index(ascending=True, inplace=True)
    df = df.to_json(orient='split', date_unit='s', date_format='iso')
    return df


def get_daily_data(date, coin):
    """ Query the API for 2000 days historical price data starting from "date". """
    url = "https://min-api.cryptocompare.com/data/histoday?fsym=" + coin + "&tsym=USD&limit=2000&toTs={}".format(date)
    r = requests.get(url)
    ipdata = r.json()
    return ipdata

def get_hourly_data(coin):
    url = "https://min-api.cryptocompare.com/data/histohour?fsym=" + coin + "&tsym=USD&limit=24"
    r = requests.get(url)
    ipdata = r.json()
    return ipdata

def get_minute_data(coin):
    url = "https://min-api.cryptocompare.com/data/histominute?fsym=" + coin + "&tsym=USD&limit=60"
    r = requests.get(url)
    ipdata = r.json()
    return ipdata

"""
today = datetime.today()
timestamp = today.timestamp()
timestamp = int(timestamp)
yesterday = timestamp - 86400
to_date = 1514700000#1514764800
#to_date = pd.to_datetime(to_date, unit='s')
from_date = 1560000000
btcdf = get_df(yesterday, timestamp, "BTC", "hour")
#print(test)
print(btcdf)
#print(len(test['data']))
"""
