import pandas as pd
from app.db_utils import get_db_config, connect_to_db

def fetch_data_from_table(connection, table_name):
    query = f"SELECT * FROM {table_name}"
    try:
        df = pd.read_sql(query, connection)
        print(f"Successfully fetched data from {table_name}")
        return df
    except Exception as e:
        print(f"Error fetching data from {table_name}: {type(e).__name__} - {str(e)}")
        return None
    finally:
        connection.close()

def get_summary_revenue_data():
    db_config = get_db_config()
    connection = connect_to_db(db_config)
    if connection is not None:
        df = fetch_data_from_table(connection, 'T_SUMMARY_REVENUE')
        if df is not None:
            print(df.iloc[0])
        else:
            print("Failed to fetch data.")
    else:
        print("Failed to connect to the database.")
