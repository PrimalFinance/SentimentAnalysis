# Operating system imports. 
import os
cwd = os.getcwd()


# Database imports
import sqlite3

# Pandas imports
import pandas as pd
from pandas.errors import DatabaseError



class DatabaseManager:
    def __init__(self):
        
        # Create connection variable. 
        self.conn = None
        self.database_paths = {
            "annualData": "{}\\Database\\AnnualData\\{}.db"
        }
        
        # Different param types. 
        self.annual_params = ["Annual", "annual", "A", "a"]
        
        # List of nammes for tables, to check if the user is passing a valid table name. 
        self.financial_statement_tables = ["income_statement", "balance_sheet", "cash_flow"]
        
        self.not_connected_error_prompt = f"\n=====================\n[Database Not Connected Error]\nYou must connect to a .db file before continuing."
        self.not_valid_table_error_prompt = "\n=====================\n[Database {} Error] Tablename is not valid ({}). \nThese are the valid tables: {}"
        
    '''----------------------------------- Database Utilities -----------------------------------'''    
    '''-----------------------------------'''
    def connect_to_database(self, ticker: str, connection_type: str = "annual"):
        # When accessing annual data. 
        if connection_type in self.annual_params:
            path_to_db = self.database_paths["annualData"].format(cwd, ticker)
            self.conn = sqlite3.connect(path_to_db)
            self.cur = self.conn.cursor()
            print(f"====== Database Connection Established ======\nFile Path: {path_to_db}")
        
    '''-----------------------------------'''
    def is_connected(self) -> bool:
        """
        Description: Returns a boolean on the state of the current connection to a database file. 
                     If there is a connection it will return True. If not it will return False. 
        """
        if self.conn is None:
            return False
        else:
            return True    
        
        
    '''-----------------------------------'''
    def write_to_database(self, df: pd.DataFrame, table_name: str, replace: bool = True):
        """
        :param df: Dataframe to write to database. 
        :param table_name: The table to write the data to. 
        :param replace: A boolean, that if true, will replace any previous data with new data. 
        
        :returns: None.        
        """
        
        
        if self.is_connected():
            # check if the table name is valid. 
            if table_name in self.financial_statement_tables:
                # Check if pre-existing data should be replaced. 
                if replace:
                    df.to_sql(name=table_name, con=self.conn, if_exists="replace", index=True) # In this case we want to include the index because it includes our row labels. 
            else:
                print(self.not_valid_table_error_prompt.format("Write", table_name, self.financial_statement_tables))
                
        else:
            print(self.not_connected_error_prompt)
    '''-----------------------------------'''
    def read_from_database(self, table_name: str) -> pd.DataFrame:
        """
        :param table_name: The table to read data from. 
        
        :returns: Data from the table in the form of a pandas dataframe. 
        """
        # If the database is connected. 
        if self.is_connected():
            # If the table name is valid. 
            if table_name in self.financial_statement_tables:          
                # Query to database table. 
                try:
                    sql_query = f"SELECT * FROM {table_name}"
                
                    # Read the data into a pandas dataframe. 
                    df = pd.read_sql(sql=sql_query, con=self.conn)
                    return df
                # Occurs if an accepted table name is passed, but it has either not been created yet, or there it is empty. So we return an empty dataframe. 
                except DatabaseError:
                    return pd.DataFrame()
            else:
                print(self.not_valid_table_error_prompt.format("Read", table_name, self.financial_statement_tables))
        else:
            print(self.not_connected_error_prompt)
    
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''