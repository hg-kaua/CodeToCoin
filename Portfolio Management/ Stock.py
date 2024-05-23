import pandas as pd
import yfinance as yf
import datetime as dt

class Stock():

    def __init__(self, ticker, start = dt.datetime(2020,1,1), end = dt.datetime.now()):
        self.ticker = ticker 
        self.start = start
        self.end = end
        self.data = None
        self.stock = None
    
        self.negative = 0
    def fetch_data(self):
        self.data = yf.download(self.ticker, self.start, self.end)
        return self.data
    
    def moving_average(self, rolling_days):
        self.data[f'Moving_average_{rolling_days}'] = self.data['Adj Close'].rolling(window=rolling_days).mean()
        return self.data
    
    def rsi(self):
        self.delta = self.data['Adj Close'].diff(1)
        
        self.positive = self.delta.copy()
        self.negative = self.delta.copy()
        
        self.positive[self.positive < 0] = 0
        self.negative[self.negative > 0] = 0
        
        self.average_gain = self.positive.rolling(window=15).mean()
        self.average_loss = abs(self.negative.rolling(window=15).mean())
        
        self.relative_strengh = self.average_gain/self.average_loss
        
        self.data['RSI'] = 100.0 - (1.0 + self.relative_strengh)
        
        return self.data
    
    def get_pe_ratio(self):
        self.stock = yf.Ticker(self.ticker)
        self.market_price = self.stock.history(period="1d")['Close'].iloc[-1]
        self.eps = self.stock.info['trailingEps']
        self.pe_ratio = self.market_price / self.eps
        
        return self.pe_ratio
    
    def get_roe(self):
        self.net_income = self.stock.financials.loc['Net Income'].iloc[0]
        self.total_equity = self.stock.balance_sheet.loc['Total Equity Gross Minority Interest'].iloc[0]
        self.roe = self.net_income / self.total_equity
        
        return self.roe

    def get_debt_to_equity(self):
        self.total_liabilities = self.stock.balance_sheet.loc['Total Liabilities Net Minority Interest'].iloc[0]
        self.total_equity = self.stock.balance_sheet.loc['Total Equity Gross Minority Interest'].iloc[0]
        self.debt_to_equity = self.total_liabilities / self.total_equity
        
        return self.debt_to_equity
    
    def get_data(self):
        print(self.stock.history())
        




apple = Stock('AAPL')


print(f'{apple.ticker} P/E: {apple.get_pe_ratio()}')
print(f'{apple.ticker} ROE: {apple.get_roe()}')
print(f'{apple.ticker} Debt to Equity: {apple.get_debt_to_equity()}')





    





    
    