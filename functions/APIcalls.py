
import pandas as pd 
import alpha_vantage
from alpha_vantage.timeseries import TimeSeries
import json
APIKEY = 'Q2AJO6LYW66V9B0J'


def get_data_intraday(key = APIKEY, symbol = '^DJI', reverse = True, first_row = False):
  ts = TimeSeries(key= APIKEY, output_format='pandas') 
  data, meta_data = ts.get_intraday(symbol, interval='1min', outputsize='compact')
  if (reverse == True):
    data = data.loc[::-1]
  if (first_row == True): 
    return data.iloc[1,0]
  return(data)

def get_data_quote(key = APIKEY, symbol = '^DJI'):
  ts = TimeSeries(key= APIKEY)
  data = ts.get_quote_endpoint(symbol)
  data = data[0]
  return(data)

def diff_data(datalist, col = 0):
  the_list = [];
  former_value = 0
  for i, v in enumerate(datalist.iloc[:, col]): 
      current_value = datalist.iloc[i, [col]].values
      if (i == 0): 
          difference_initation = current_value - current_value
          former_value = current_value
          the_list.append(difference_initation)
      else:
          difference = current_value - former_value
          former_value = current_value
          the_list.append(difference) 
  del the_list[0]

  return the_list