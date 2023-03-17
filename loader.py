from connection import Connection
import pandas as pd

class Loader:

    def load_to_db(self, schema, table_name, df):

        dt=pd.DataFrame()
        dt=df
        try:
            conn=Connection()
            engine=conn.sql_engine()
            dt.to_sql(
                name=table_name,
                 con=engine,
                 schema=schema,
                 if_exists='append',
                 index=False
                 )

        except Exception as e:
            raise(e)
