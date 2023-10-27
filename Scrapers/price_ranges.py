# Operating System imports
import os
from dotenv import load_dotenv
load_dotenv()

# Number management related imports
import numpy as np
import pandas as pd

# Date & time imports
import time
import datetime as dt

# Yahoo Finance imports
import yfinance as yf



class PriceRanges:
    def __init__(self, ticker: str, year: str = "") -> None:
        self.ticker = ticker 
        
        self.year = year
    '''-------------------------------'''
    def get_all_quarters(self, quarters: dict = {}) -> dict:
        
        if quarters != {}:
            q1_start_month, q1_start_day = quarters["Q1_start"].split("/")
            q1_end_month, q1_end_day = quarters["Q1_end"].split("/")
            q2_start_month, q2_start_day = quarters["Q2_start"].split("/")
            q2_end_month, q2_end_day = quarters["Q2_end"].split("/")
            q3_start_month, q3_start_day = quarters["Q3_start"].split("/")  
            q3_end_month, q3_end_day = quarters["Q3_end"].split("/")
            q4_start_month, q4_start_day = quarters["Q4_start"].split("/")
            q4_end_month, q4_end_day = quarters["Q4_end"].split("/")
        else:
            q1_start_month, q1_start_day = 1, 1
            q1_end_month, q1_end_day = 3, 31
            q2_start_month, q2_start_day = 4, 1
            q2_end_month, q2_end_day = 6, 30
            q3_start_month, q3_start_day = 7, 1
            q3_end_month, q3_end_day = 9, 30
            q4_start_month, q4_start_day = 10, 1
            q4_end_month, q4_end_day = 12, 31


        q1_data = self.get_quarter_data(start_month=q1_start_month, start_day=q1_start_day, end_month=q1_end_month, end_day=q1_end_day)
        q2_data = self.get_quarter_data(start_month=q2_start_month, start_day=q2_start_day, end_month=q2_end_month, end_day=q2_end_day)
        q3_data = self.get_quarter_data(start_month=q3_start_month, start_day=q3_start_day, end_month=q3_end_month, end_day=q3_end_day)
        q4_data = self.get_quarter_data(start_month=q4_start_month, start_day=q4_start_day, end_month=q4_end_month, end_day=q4_end_day)

        quarterly_data = {"Q1": q1_data,
                          "Q2": q2_data,
                          "Q3": q3_data,
                          "Q4": q4_data}
        
        return quarterly_data




    '''-------------------------------'''
    def get_quarter_data(self, start_month:int =1, start_day: int =1, end_month: int = 3, end_day: int = 31) -> dict:
        
        quarter_data = {}

        # Turn all of the date elements into integers. 
        start_month, start_day = int(start_month), int(start_day)
        end_month, end_day = int(end_month), int(end_day)
        


        # Create start and end dates for the first quarter of the year
        start_date = dt.datetime(self.year, start_month, start_day)
        end_date = dt.datetime(self.year, end_month, end_day)

        # Fetch the stock data for the specified ticker symbol and date range
        stock_data = yf.download(self.ticker, start=start_date, end=end_date)

        # Extract the 'High' and 'Low' columns from the stock data
        quarter_data["High"] = round(stock_data["High"].max(), 2)
        quarter_data["Low"] = round(stock_data["Low"].min(), 2)
        try:
            quarter_data["Average"] = round(stock_data["Adj Close"].mean(), 2)
        except ValueError:
            quarter_data["Average"] = "N\A"
        return quarter_data
    '''-------------------------------'''
    '''-------------------------------'''
    '''-------------------------------'''
    def get_price_range_in_year(self, fiscal_data: dict = {}) -> dict:
        data = {}

        if fiscal_data != {}:
            fiscal_start_month, fiscal_start_day = fiscal_data["fiscal_start"].split("/")
            fiscal_end_month, fiscal_end_day = fiscal_data["fiscal_end"]

            fiscal_start_month, fiscal_start_day = int(fiscal_start_month), int(fiscal_start_day)
            fiscal_end_month, fiscal_end_day = int(fiscal_end_month), int(fiscal_end_day)

        else:
            fiscal_start_month, fiscal_start_day = 1, 1
            fiscal_end_month, fiscal_end_day = 12, 31

        # Create variable for first date in year, and last date in year.
        start_date = f"{self.year}-01-01"
        end_date = f"{self.year}-12-31"

        # Get the stock data within the specified year.
        stock_data = yf.download(self.ticker, start=start_date, end=end_date)

        # Extract the high, low, and adjusted close prices from the year. 
        # For the adjusted closes, we will take the average.
        data["High"] = round(stock_data["High"].max(), 2)
        data["Low"] = round(stock_data["Low"].min(), 2)
        data["Average"] = round(stock_data["Adj Close"].mean(), 2)

        return data
    '''-------------------------------'''
    def get_first_trading_year(self):
        try:
            # Create a Yahoo Finance Ticker object for the given symbol
            ticker = yf.Ticker(self.ticker)

            # Get historical data
            historical_data = ticker.history(period="max")

            # Extract the first trading year
            first_year = historical_data.index[0].year

            return first_year
        except Exception as e:
            print(f"Error: {e}")
            return None
    '''-------------------------------'''
    '''-------------------------------'''
    '''-------------------------------'''
    '''-------------------------------'''
