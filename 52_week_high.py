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
    host = "xx",
    user ="xx",
    password ="xx",
    #database = "nifty_schema"
)
count_error=0


ticker = [


'YESBANK'



]
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
        skipper=0
        min3 =max(df2['High'][0:250], default=-1)
       
        for j in range(250,len(df2['date'])-10):
            if skipper>0:
                skipper=skipper-1
                continue
           
            count = 0
            for i in df2['High'][j-250:j]:
                if i>min3:
                    min3 = i
                    count = count+1
            #print(min3,low_1[j],count)        
            if count == 0:
                min3=max(df2['High'][j-250:j-1])
            #print(low_1[j],min3,min(low_1[j+1],low_1[j+2],low_1[j+3]))
            if df2['High'][j] >= min3 :
                low_523.append(df2['Open'][j+1])
                low_2.append(df2['Volume'][j+1])                                                    
                low_3.append(df2['High'][j+1])                                                      
                for k in range(j,j+10):
                    checker_1 = 0
                    if k==j+9 :
                        low_1.append(df2['date'][k])
                        price_tracker1.append(df2['Open'][j+1])
                        price_tracker2.append(df2['Open'][j+11])
                        price_tracker3.append(df2['date'][j+1])
                        price_tracker4.append(df2['date'][j+11])
                        ticker_tracker.append(ticker_name)
                        checker_1=checker_1+1
                        skipper=22
                        break
                   

                                                                       
                                                       
                                                   
                                                   
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
       'ticker': ticker_tracker,
       'buy_p': price_tracker1,
       'sell_p':price_tracker2,
       'buy_date':price_tracker3,
       'sell_date':price_tracker4})
writer = pd.ExcelWriter('output.xlsx')
# write dataframe to excel

print(count_error)
print(csv_frame)
csv_frame['percentage'] = (csv_frame['sell_p']-csv_frame['buy_p'])*100/csv_frame['buy_p']
csv_frame['days'] = csv_frame['sell_date']-csv_frame['buy_date']
print(csv_frame)
csv_frame.to_excel(writer)
writer.save()
win_trades=[]
los_trades=[]
losing = (csv_frame['percentage']<0).sum().sum()
winning = (csv_frame['percentage']>0).sum().sum()
total_t=losing+winning
prob_win=winning*100/total_t
prob_loss=losing*100/total_t
for z in csv_frame['percentage']:
    if z<0:
        los_trades.append(z)
    else:
        win_trades.append(z)    
avg_profit=sum(win_trades)/winning
avg_loss=sum(los_trades)/losing
print("losing trades: ",losing)
print("winning trades: ",winning)
print("total trades: ",total_t)
print("Average profit: ",avg_profit)
print("Average losing trades: ",avg_loss)
print("probablity of winning: ",prob_win)
print("probablity of losing: ",prob_loss)
print("Max drawdown: ",min(los_trades))
print("Max profit:",max(win_trades))
print("Expectancy: ",(avg_profit*prob_win)+(avg_loss*prob_loss))

print(sum(win_trades))