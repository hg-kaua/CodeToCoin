import pandas as pd
import yfinance as yf
import datetime as dt

class Stock():
    
    def __init__(self, ticker, start = dt.datetime(2020,1,1), end = dt.datetime.now()):
        self.ticker = ticker 
        self.start = start
        self.end = end
        self.data = None
    
    def fetch_data(self):
        self.data = yf.download(self.ticker, self.start, self.end)
        return self.data
    
    def moving_average(self, rolling_days):
        self.data[f'Moving_average_{rolling_days}'] = self.data['Adj Close'].rolling(window=rolling_days).mean()
        return self.data




apple = Stock('AAPL')

print(apple.ticker)
print(apple.start)
print(apple.end)

apple.fetch_data()
print(apple.data)
apple.moving_average(200)
print(apple.data)





    
    
    