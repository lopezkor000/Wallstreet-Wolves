import yfinance as yf
import pandas as pd

SP_500 = pd.read_csv('S&P_500.csv')

for i, stock in SP_500.iterrows():
  symbol = stock['Symbol']
  ticker = yf.Ticker(symbol)
  history = ticker.history(period='5y', interval='1d')
  history.to_csv(f'data/{symbol}.csv')
