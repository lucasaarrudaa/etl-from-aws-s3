import pandas as pd
import numpy as np

class Transformer:    
        
    def table_maker(self, df):
        '''
        Changing types of columns in DF.        
        '''
        dt=pd.DataFrame(df)
        dtypes ={'campaign_date':'datetime64',
                 'campaign_name':'object',
                 'impressions':'int32',
                 'clicks':'int32',
                 'cost':'float64',
                 'advertising':'object',
                 'ip':'object',
                 'device_id':'object',
                 'campaign_link':'object',
                 'data_click':'datetime64',
                 'lead_id':'object',
                 'registered_at':'datetime64',
                 'credit_decision':'object',
                 'credit_decision_at':'datetime64',
                 'signed_at':'datetime64',
                 'revenue':'float16'}
        dt=dt.astype(dtype=dtypes)
        
        return dt
        
    def extract_string(self, table, column, regex):
        '''
        Extracting a string using REGEX.
        
        Parameters:
                column: name of column 
                regex: regex code
                new_col_name: name of the new column.
                
        Returns:
                Return what do you want to extract.
        '''
        extracted = table[f'{column}'].str.extract('({})'.format(regex))
        
        return extracted

    def delete_col(self, df, column):
        '''
        Deleting a column from DF.
        
        Parameters: 
                df(string): dataframe
                column: column to delete
        NOTE: you need to assign to a df. 
        '''
        deleted = df.loc[:, ~df.columns.isin([f'{column}'])]
        
        return deleted
    
    def rename(self, df, column1, new_name):
        df = df.rename(columns = {f'{column1}':f'{new_name}'}, inplace = True)
        
        return df
        '''
        Renaming a column from a DF.
        '''

    def concat(self, df1, df2, ignore_index=True):
        '''
        Concat dfs.
        '''
        concatenated = pd.concat([df1, df2], ignore_index = ignore_index)
        
        return concatenated

        
    def join(self, new_df, df1, df2):
        '''
        Join columns and attribute to new DF.
        '''
        new_df = df1.join(df2, rsuffix='_r', lsuffix='_l')
        
        return new_df
    
    def drop_duplicates(self, df, col):
        '''
        Delete duplicates in a specific column of a DF.
        
        Parameters:
                df: df you want to modify
                col (string): column name you want to drop
        Returns:
                df without specified column
        '''
        dt = df.drop_duplicates([f'{col}'])
        
        return dt
    
    def fill(self, df, rows, value):
        '''
        Generate values to insert in the rows of a specific column of DF.
        
        Parameters:
                df = name of df
                rows (int): number of rows
                value (type): value what do you want to insert (str, int, float...)
                name_column: name of new column to append in df
        Returns: 
                return a new df with new values in a column
        '''
        self.rows = np.full(rows, value)
        new_df = df.assign(advertising=value) #NOTE: you need to change 'advertising' to your preferenced name column
        
        return new_df
