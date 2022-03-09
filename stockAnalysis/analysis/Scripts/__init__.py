import os 
import yfinance as yf
import pandas as pd


PROJECT_HOME=os.environ['ProjectHome']
DATA_HOME=PROJECT_HOME+'\\datab'
ANALYTICS_HOME=PROJECT_HOME+'\\analysis'
LIBRARY_HOME=PROJECT_HOME+'\\library'

ENV_HOME=os.environ['EnvHome']

def download_price_history(tickerstrng,period='8y',interval='1d'):
    '''
    This function downloads history from yahoo finance
    
    Arguments: 
    tickerstrng : Ticker symbol
    period : The period for which historical price will be downloaded for the ticker, default = 10y
    interval: The interval of price data, default = 1d
    '''
    tickobj = yf.Ticker(tickerstrng)
    tickhist = tickobj.history(period=period, interval=interval)
    return tickhist



    


