#%% 
# Getting data from a stock API 

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
ts = TimeSeries(key='Q2AJO6LYW66V9B0J',output_format='pandas')
data, meta_data = ts.get_intraday(symbol='^DJI', interval='1min', outputsize='compact')
print(data)
#data is in reversed order data2 corrects this 
# # data imported is inverse then latest data is on top. 
data2 = data.iloc[::-1]
data2['4. close'].plot()

plt.title('Intraday TimeSeries Dow jones')
plt.show()

#%% 
# Check the current date matches with data 
#def time_checker() :
   # from datetime import datetime
    # check if first date in dataframe is equal to current date 
     #   if data.index.values[0] != datetime.now().strftime('%Y-%m-%d %H:%M:00') 
   # data, meta_data = ts.get_intraday(symbol='^DJI', interval='1min', outputsize='compact')
    #else 
   ## return null 

#%% Testloop for iteration and countin a continuous difference between updated closing price vs former closing price

former_value = 0
count = 0
for i in data2.index: 
    current_value = data2.iloc[count, [3]]
    if (count == 0): 
        difference_initation = current_value - current_value
        print("diff init", difference_initation)
        former_value = current_value
        count +=1
    else:
        difference = difference_initation + (current_value - former_value)
        print("diff \n", difference)
        count +=1



#%% Find out how to write in gui 

import plotly as py
import plotly.graph_objs as go 

trace = {'x': [1,2], 'y': [1,2]}
data = [trace]
layout = {} 
fig = go.Figure( 
  data = data, layout = layout)

fig.show()

#%%
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.show()


#%%


