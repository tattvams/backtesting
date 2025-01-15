from backtesting.test import SMA
import pandas as pd
from backtesting.lib import SignalStrategy, TrailingStrategy, resample_apply

from backtesting import Strategy, Backtest

from backtesting.test import GOOG
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    #xx
)
df = pd.read_sql('SELECT Date, Open,High,Low,Close FROM nifty_a_z.nifty_a_z where ticker = "DBL" ', con=mydb)

df = df.rename(columns={'open_price': 'Open', 'high_price': 'High', 'low_price' : 'Low', 'close_price' : 'Close'})
df['Date'] = pd.to_datetime(df['Date'], format = '%m/%d/%Y')
df.index = pd.DatetimeIndex(df['Date'])
low_data = df['Low']
low_1 = []
low_523=[]




    

def low_52():
    min3 =min(df['Low'][0:250])
    
    for j in range(250,len(df['Date'])-3): 
        count = 0
        for i in df['Low'][range(j-250,j-1)]:
            if i<min3:
                min3 = i
                count = count+1
        #print(min3,low_1[j],count)        
        if count == 0:
            min3 = df['Low'][j-250]
        #print(low_1[j],min3,min(low_1[j+1],low_1[j+2],low_1[j+3]))
        if df['Low'][j] <= min3 and df['Low'][j]<min(df['Low'][j+1],df['Low'][j+2],df['Low'][j+3]):
            low_523.append(df['Date'][j])
            #print(low_1[j],min3,min(low_1[j+1],low_1[j+2],low_1[j+3]))
            
                 


       



#print(low_1)


low_52()
#print(low_1)    
print(low_523)
        
# class System(Strategy):

    
#     def init(self):
#       return 0
        
#     def next(self):
        

