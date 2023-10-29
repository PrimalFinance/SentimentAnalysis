# Operating system imports. 
import os
cwd = os.getcwd()


# Database imports
import sqlite3

# Pandas imports
import pandas as pd
from pandas.errors import DatabaseError



class DatabaseManager:
    def __init__(self, update_prompts: bool = True, error_prompts: bool = True):
        # Notify where data is retrieved from. When a process is complete. Updates on various tasks. 
        self.update_prompts = update_prompts
        # Notify when an error has occured with the database. Whether a connection has not been established.
        # Or a table is trying to be accessed that does not exist. 
        self.error_prompts = error_prompts
        
        
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
        self.ticker = ticker
        # When accessing annual data. 
        if connection_type in self.annual_params:
            path_to_db = self.database_paths["annualData"].format(cwd, ticker)
            self.conn = sqlite3.connect(path_to_db)
            self.cur = self.conn.cursor()
            if self.update_prompts:
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
    def get_file_connection(self) -> str:
        """
        :returns: String of database file. 
        
        Description: This function checks what database file (.db) the class is connected to. 
        """  
        if self.is_connected():
            return f"{self.ticker}.db"
        else:
            if self.error_prompts:
                print(self.not_connected_error_prompt)
        
        
    '''-----------------------------------'''
    def write_to_database(self, df: pd.DataFrame, table_name: str, replace: bool = True, update: bool = False):
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
                if self.error_prompts:
                    print(self.not_valid_table_error_prompt.format("Write", table_name, self.financial_statement_tables))
                
        else:
            if self.error_prompts:
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
                    df = df.set_index("index")
                    return df
                # Occurs if an accepted table name is passed, but it has either not been created yet, or there it is empty. So we return an empty dataframe. 
                except DatabaseError:
                    return pd.DataFrame()
            else:
                if self.error_prompts:
                    print(self.not_valid_table_error_prompt.format("Read", table_name, self.financial_statement_tables))
        else:
            if self.error_prompts:
                print(self.not_connected_error_prompt)
    
    '''-----------------------------------'''
    def update_database(self, update_df: pd.DataFrame, table_name: str):
        """
        :param update_df: Dataframe with new information to update the database with. 
        :param table_name: Table in the database to update. 
        
        :returns: None
        
        Description: This function will operate with two dataframes. 
                     One is passed in the function parameter, and is the new data to update the database with. 
                     The other is a dataframe that is created within this function, that will read what is currently
                     in the database. Then the dataframe with the previous information and the dataframe with the new information will be merged. 
                     
        """
        
        if self.is_connected():
            if table_name in self.financial_statement_tables:
                # Get data already in the database. 
                prev_df = self.read_from_database(table_name)
                # Merge the previous data with the new data. 
                combined_df = pd.concat([prev_df, update_df], axis=1)
                # Write the new merged dataframe to the database table. 
                self.write_to_database(df=combined_df, table_name=table_name)
            else:
                if self.error_prompts:
                    print(self.not_valid_table_error_prompt)
        else:
            if self.error_prompts:
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