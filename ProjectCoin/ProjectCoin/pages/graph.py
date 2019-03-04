import requests
import pandas as pd
import json

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
    df.sort_index(ascending=True, inplace=True)
    df = df.to_json(orient='split', date_unit='s', date_format='iso')
    return df


def get_data(date, coin):
    """ Query the API for 2000 days historical price data starting from "date". """
    url = "https://min-api.cryptocompare.com/data/histoday?fsym=" + coin + "&tsym=USD&limit=2000&toTs={}".format(date)
    r = requests.get(url)
    ipdata = r.json()
    return ipdata

to_date = 1514764800
from_date = 1560000000
btcdf = get_df(to_date, from_date, "BTC")
#test = json.loads(btcdf)
#print(test)
#print(btcdf)
#print(len(test['data']))
