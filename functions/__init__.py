
import pandas as pd 

def get_data(key = 'Q2AJO6LYW66V9B0J', symbol = '^DJI', reverse = True): 
  from alpha_vantage.timeseries import TimeSeries
  ts = TimeSeries(key= key,output_format='pandas')

  data, meta_data = ts.get_intraday(symbol='^DJI', interval='1min', outputsize='compact')
  if (reverse == True):
    data = data.loc[::-1]

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