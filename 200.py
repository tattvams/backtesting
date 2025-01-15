from ast import Try
from itertools import count
from backtesting.test import SMA
import pandas as pd
from backtesting.lib import SignalStrategy, TrailingStrategy, resample_apply
import csv
from backtesting import Strategy, Backtest

from backtesting.test import GOOG
import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(
    #//
)
count_error=0


ticker = ['ACC']
print(len(ticker))
kp=[]
kn=[]
kd=[]
low_1=[]
price_tracker1 = []
price_tracker2 = []
price_tracker3 = []
price_tracker4 = []
ticker_tracker=[]

for i in ticker:
    g ='SELECT date, Open,High,Low,Close,Volume FROM nifty_a_z.nifty_a_z where ticker ="%s"'%(i)
    df2 = pd.read_sql(g, con=mydb)
    ticker_name = i


    df2 = df2.rename(columns={'open_price': 'Open', 'high_price': 'High', 'low_price' : 'Low', 'close_price' : 'Close'})
   
    df2['date'] = pd.to_datetime(df2['date'], format = '%m/%d/%Y')
    df2.index = pd.DatetimeIndex(df2['date'])
    
    print(ticker_name)    
    low_3=[]
    low_2 = []
    low_523=[]
    def low_52():
      
       
        for j in range(200,len(df2['date'])):
            k = df2['Close'][j-200:j].mean()
            price_tracker1.append(k)
            price_tracker2.append(df2['date'][j])
            
            




           
                       
                   

                                                                       
                                                       
                                                   
                                                   
    #print(low_1)


    low_52()
    #print(low_1)    
    #print(len(low_523))

       



    #print(low_1)


    #low_52()

           
   
                               
    #backtest = Backtest(df2, System)                        
    #al =backtest.run()
    #backtest.plot()
    #k = al._trades['EntryPrice']
    #l = al._trades
    #print(l)
    #print(k)

    #for i in k:
    #   kp.append(i)
    #for i in range(len(l['EntryTime'])):
    #  kd.append(l['EntryTime'][i])    
       

                                                   
#print(len(kp))                                                    
#print(len(kd))                                                      
#print(low_1)  
#print(kd)  
#print(kp)                                                  
#print(price_tracker1)                                                    
#print(price_tracker2)
#print(price_tracker3)
#print(price_tracker4)
#print(ticker_tracker)
                                                     
#print(low_523)                                                    

csv_frame = pd.DataFrame({
       
       'Average': price_tracker1,
       'Date':price_tracker2,
       })
writer = pd.ExcelWriter('output.xlsx')
# write dataframe to excel

print(count_error)
print(csv_frame)

#print(csv_frame)
csv_frame.to_excel(writer)
writer.save()

