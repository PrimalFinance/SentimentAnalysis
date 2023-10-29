# Operating system imports
import os
from dotenv import load_dotenv
load_dotenv()

# Web requests
import requests

# Pandas imports  
import pandas as pd 

# Import graphing 
import Graphing.graphs

# Import price ranges scraper
import Scrapers.price_ranges
import Scrapers.fiscal_dates_scraper

# Yahoo imports 
import yfinance as yf

import datetime as dt

# Import database
import Database.data_base_manager

# Get the Finanacial Modeling Prep api key. 
fmp_key = os.getenv("fmp_key")

# Paths to csv 
cwd = os.getcwd()
test_dir = cwd


class FmpScraper:
    def __init__(self, ticker: str ):
        
        self.ticker = ticker.upper()
        
        self.root_url = "https://financialmodelingprep.com/api/v3/{}/{}?limit={}&apikey={}"
        
        
        # Class variables to hold statements. 
        self.income_statement = pd.DataFrame()
        self.balance_sheet = pd.DataFrame()
        self.cash_flow = pd.DataFrame()
        
        # Create database object. 
        self.db = Database.data_base_manager.DatabaseManager()
        
        
        # Possible parameters used throughout functions. 
        self.annual_params = ["Annual", "annual", "A", "a"]
        self.quarterly_params = ["Quarter", "quarter", "Quarterly", "quarterly", "Q", "q"]
        
        
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    # ---------------------------------- Financial Statements - Setters & Getters ----------------------------------
    '''-----------------------------------'''
    def set_income_statement(self, years: int, include_stock_prices: bool = True):
        """
        :param years: The number of fiscal years to collect. 
        :include_stock_prices: A boolean that determines if stock prices are included in the final dataframe.  
        
        :returns: Returns a dataframe with data from the income statement, for the specified number of 'years'. 
        """
        # If there is not connection to a database file. 
        if not self.db.is_connected():
            self.db.connect_to_database(ticker=self.ticker)
        
        # Boolean to track if updates are needed. 
        update_needed = False
        update_database = False
        
        
        df = self.db.read_from_database(table_name="income_statement")
        
        print(f"DF Read: {df}")

        # Logic to determine if an update is needed. 
        if df.empty:
            print(f"Empty Tag")
            update_needed = True
            # If the dataframe is empty we do not need to update, we need to write/create new tables. 
            update_database = False
        else:
            print(f"Non-Empty Tag")
            # If the dataframe *is* empty, check if it is outdated.  
            outdated = self.is_outdated(df, considered_outdated=13)
            print(f"OUTDATED: {outdated}")
            # If the dataframe *is not* empty, but it is outdated we want to update the database.  
            if outdated:
                update_needed = True
                update_database = True
            else:   
                print(f"[Set Income Statement] Data retrieved from database.")
        
        if update_needed:
            endpoint = "income-statement"
            
            # Query the income statement for the company. 
            income_statement = requests.get(self.root_url.format(endpoint, self.ticker, years, fmp_key))
            income_statement = income_statement.json()
            
            df = pd.DataFrame(income_statement)
            # Transpose the dataframe to swap the rows with the columns. 
            df = df.T
            # Reverse the columns so the newest data is on the right side. 
            df = df[df.columns[::-1]]
            # Remove unwanted rows. 
            rows_to_remove = ["symbol","reportedCurrency", "acceptedDate", "period"]
            df = df.drop(labels=rows_to_remove, axis=0)
            
            # Set the column titles as the date row, and drop the remaining date row. 
            df.columns = df.loc["date"]
            df = df.drop("date")
            df.to_csv(f"{test_dir}\\test.csv")
            # Add stock prices to the dataframe. 
            if include_stock_prices:
                df = self.add_stock_prices(df)
            
            # Determine if the database should be updated, or written to, possibly overwriting contents. 
            if update_database:
                print(f"[Set Income Statement] - Updating outdated database: {self.db.get_file_connection()}, table: income_statement")
                self.db.update_database(update_df=df, table_name="income_statement")
            else:
                print(f"[Set Income Statement] - Writing to database: {self.db.get_file_connection()}, table: income_statement")
                self.db.write_to_database(df=df, table_name="income_statement")
            
            print(f"[Set Income Statement] Data retrieved from FMP Scraper.")
            
        self.income_statement = df
            
        
    '''-----------------------------------'''
    def set_balance_sheet(self, years: int, include_stock_prices: bool = True):
        """
        :param years: The number of fiscal years to collect. 
        :include_stock_prices: A boolean that determines if stock prices are included in the final dataframe.  
        
        :returns: Returns a dataframe with data from the income statement, for the specified number of 'years'. 
        """
        
        balance_sheet_table = "balance_sheet"
        set_statement = "Set Balance Sheet"
        
        # If there is not connection to a database file. 
        if not self.db.is_connected():
            self.db.connect_to_database(ticker=self.ticker)
        
        # Boolean to track if updates are needed. 
        update_needed = False
        update_database = False
        
        
        df = self.db.read_from_database(table_name=balance_sheet_table)

        # Logic to determine if an update is needed. 
        if df.empty:
            update_needed = True
            # If the dataframe is empty we do not need to update, we need to write/create new tables. 
            update_database = False
        else:
            # If the dataframe *is* empty, check if it is outdated.  
            outdated = self.is_outdated(df, considered_outdated=13)
            # If the dataframe *is not* empty, but it is outdated we want to update the database.  
            if outdated:
                update_needed = True
                update_database = True
            else:   
                print(f"[{set_statement}] Data retrieved from database.")
        
        if update_needed:
            endpoint = "balance-sheet-statement"
            
            # Query the income statement for the company. 
            balance_sheet = requests.get(self.root_url.format(endpoint, self.ticker, years, fmp_key))
            balance_sheet = balance_sheet.json()
            df = pd.DataFrame(balance_sheet)
            # Transpose the dataframe to swap the rows with the columns. 
            df = df.T
            # Reverse the columns so the newest data is on the right side. 
            df = df[df.columns[::-1]]
            
            # Remove unwanted rows. 
            rows_to_remove = ["symbol","reportedCurrency", "acceptedDate",]
            df = df.drop(labels=rows_to_remove, axis=0)
            
            # Set the column titles as the date row, and drop the remaining date row. 
            df.columns = df.loc["date"]
            df = df.drop("date")
            # Add stock prices to the dataframe. 
            if include_stock_prices:
                df = self.add_stock_prices(df)
            
            # Determine if the database should be updated, or written to, possibly overwriting contents. 
            if update_database:
                print(f"[{set_statement}] - Updating outdated database: {self.db.get_file_connection()}, table: balance_sheet")
                self.db.update_database(update_df=df, table_name=balance_sheet_table)
            else:
                print(f"[{set_statement}] - Writing to database: {self.db.get_file_connection()}, table: balance_sheet")
                self.db.write_to_database(df=df, table_name=balance_sheet_table)
            
            print(f"[{set_statement}] Data retrieved from FMP Scraper.")
        print(f"Update needed: {update_needed}   Update Database: {update_database}")    
        self.balance_sheet = df
    '''-----------------------------------'''
    def set_cash_flow(self, years: int, include_stock_prices: bool = True):
        """
        :param years: The number of fiscal years to collect. 
        :include_stock_prices: A boolean that determines if stock prices are included in the final dataframe.  
        
        :returns: Returns a dataframe with data from the income statement, for the specified number of 'years'. 
        """
        
        cash_flow_table = "cash_flow"
        set_statement = "Set Cash Flow"
        
        # If there is not connection to a database file. 
        if not self.db.is_connected():
            self.db.connect_to_database(ticker=self.ticker)
        
        # Boolean to track if updates are needed. 
        update_needed = False
        update_database = False
        
        
        df = self.db.read_from_database(table_name=cash_flow_table)

        # Logic to determine if an update is needed. 
        if df.empty:
            update_needed = True
            # If the dataframe is empty we do not need to update, we need to write/create new tables. 
            update_database = False
        else:
            # If the dataframe *is* empty, check if it is outdated.  
            outdated = self.is_outdated(df, considered_outdated=13)
            # If the dataframe *is not* empty, but it is outdated we want to update the database.  
            if outdated:
                update_needed = True
                update_database = True
            else:   
                print(f"[{set_statement}] Data retrieved from database.")
        
        if update_needed:
            endpoint = "cash-flow-statement"
            
            # Query the income statement for the company. 
            cash_flow = requests.get(self.root_url.format(endpoint, self.ticker, years, fmp_key))
            cash_flow = cash_flow.json()
            df = pd.DataFrame(cash_flow)
            # Transpose the dataframe to swap the rows with the columns. 
            df = df.T
            # Reverse the columns so the newest data is on the right side. 
            df = df[df.columns[::-1]]
            
            # Remove unwanted rows. 
            rows_to_remove = ["symbol","reportedCurrency", "acceptedDate",]
            df = df.drop(labels=rows_to_remove, axis=0)
            
            # Set the column titles as the date row, and drop the remaining date row. 
            df.columns = df.loc["date"]
            df = df.drop("date")
            # Add stock prices to the dataframe. 
            if include_stock_prices:
                df = self.add_stock_prices(df)
            
            # Determine if the database should be updated, or written to, possibly overwriting contents. 
            if update_database:
                print(f"[{set_statement}] - Updating outdated database: {self.db.get_file_connection()}, table: {cash_flow_table}")
                self.db.update_database(update_df=df, table_name=cash_flow_table)
            else:
                print(f"[{set_statement}] - Writing to database: {self.db.get_file_connection()}, table: {cash_flow_table}")
                self.db.write_to_database(df=df, table_name=cash_flow_table)
            
            print(f"[{set_statement}] Data retrieved from FMP Scraper.")
        print(f"Update needed: {update_needed}   Update Database: {update_database}")    
        self.cash_flow  = df
    
    # ---------------------------------- Financial Statements - Setters & Getters ----------------------------------
    '''-----------------------------------'''
    def add_stock_prices(self, df: pd.DataFrame, period: str = "annual"):
        """
        :param df: Dataframe to add stock prices to. 
        
        :returns: The same dataframe passed in, but with new rows for the stock price. 
        """
        
        # Get the first year from the dataframe. 
        date_data_points = df.columns
        
        start_date = date_data_points[0]
        end_date = date_data_points[-1]
        
        # Parse the dates 
        start_year, start_month, start_day = start_date.split("-")
        end_year, end_month, end_day = end_date.split("-")
        
        
        index = 0
        annual_prices_collected = [] 
        for i in range(int(start_year), int(end_year)+1):
            annual_prices = {}
            # Skip the first index. Since this is the first column in our dataframe, there is no previous column to reference. 
            if index < len(date_data_points):
                if index == 0:
                    # When index is 0, we are working with our first column. Meaning we have not dates before this. 
                    # So we use the columns date as the end date, subtract one year from it, and use that as the start date. 
                    index_end_date = date_data_points[index]
                    index_end_year, index_end_month, index_end_day = index_end_date.split("-")
                    index_start_year = int(index_end_year) - 1
                    index_start_date = f"{index_start_year}-{index_end_month}-{index_end_day}"
                    period = f"{index_start_date} - {index_end_date}"
                else:
                    
                    index_start_date = date_data_points[index-1]
                    index_end_date = date_data_points[index]
                    
                    period = f"{index_start_date} - {index_end_date}" 
                
                
                annual_data = yf.download(self.ticker, start=index_start_date, end=index_end_date)
                
                # Parse the annual data. 
                annual_prices["date"] = index_end_date
                annual_prices["startPeriod"] = index_start_date
                annual_prices["endPeriod"] = index_end_date
                annual_prices["high"] = round(annual_data["High"].max(), 2)
                annual_prices["low"] = round(annual_data["Low"].min(), 2)
                try:
                    annual_prices["average"] = round(annual_data["Close"].mean(), 2)
                except ValueError:
                    annual_prices["average"] = "N\A"
                
                
                annual_prices_collected.append(annual_prices)
            else:
                pass    
                
            index += 1
            
        prices_df = pd.DataFrame(annual_prices_collected)
        # Transpose the dataframe (swap the rows with the columns). 
        prices_df = prices_df.T
        # Set the columns as the values of the date row. 
        prices_df.columns = prices_df.loc["date"]
        # Drop the date row that is left over. 
        prices_df = prices_df.drop("date")
        # Concat the dataframes, to add the prices_df dataframe to the dataframe passed in the parameter of the function. 
        result = pd.concat([df, prices_df])
        
        return result
                 
                
            
        
        
    '''-----------------------------------'''
    def is_outdated(self, df: pd.DataFrame, considered_outdated: int = 12, warning_message: bool = True):
        """
        :param df: Dataframe with columns of financial data. 
        :param warning_message: Determine if warning readouts should be displayed. 
        
        Description: Check the dates in the columns of the dataframe. 
        """
        # Get the different dates from the dataframe. 
        earnings_dates = df.columns
        filing_dates = list(df.loc["fillingDate"])
        # Get the current date. 
        current_date = dt.datetime.now()
        # Create datetime object for filing date. 
        recent_filing_obj = dt.datetime.strptime(filing_dates[-1], "%Y-%m-%d")
        
        # Calculate the difference between dates. 
        delta_years = current_date.year - recent_filing_obj.year
        delta_months = current_date.month - recent_filing_obj.month
        total_months = delta_years * 12 + delta_months
        
        if total_months >= considered_outdated:
           return True
        else: 
           return False
        
       
        
        
        
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''