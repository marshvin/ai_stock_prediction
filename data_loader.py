# data_loader.py
import yfinance as yf
from pandas_datareader import data as pdr
from datetime import datetime

def load_stock_data():
    tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
    end = datetime.now()
    start = datetime(end.year - 1, end.month, end.day)

    company_list = [yf.download(stock, start, end) for stock in tech_list]

    company_name = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON"]
    for company, com_name in zip(company_list, company_name):
        company["company_name"] = com_name
    df = pd.concat(company_list, axis=0)
    return df
