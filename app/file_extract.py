import pandas as pd
from datetime import datetime

from app.db_utils import get_db_config, connect_to_db

def convert_to_mysql_date(date_value):
    if pd.isna(date_value):
        return None
    if isinstance(date_value, pd.Timestamp):
        return date_value.strftime("%Y-%m-%d")
    if isinstance(date_value, str):
        for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y", "%m-%d-%Y"):
            try:
                return datetime.strptime(date_value, fmt).strftime("%Y-%m-%d")
            except ValueError:
                continue
    return None

def clean_cell(value):
    if pd.isna(value) or (isinstance(value, str) and not value.strip()):
        return None
    if isinstance(value, (int, float)):
        return value
    return value

def read_excel_data(file_path, date_columns, chunksize=1000):
    print(f"Reading file in chunks: {file_path}")
    chunk_iter = pd.read_excel(file_path, engine='openpyxl', chunksize=chunksize)

    for chunk in chunk_iter:
        for col in chunk.columns:
            if col in date_columns:
                chunk[col] = chunk[col].apply(convert_to_mysql_date)

        # Chuyển các cột số sang object và thay NaN bằng None
        numeric_cols = chunk.select_dtypes(include=['float']).columns
        chunk[numeric_cols] = chunk[numeric_cols].astype(object).where(pd.notnull(chunk[numeric_cols]), None)

        # Chuyển toàn bộ DataFrame sang kiểu object (phòng trường hợp)
        chunk = chunk.applymap(lambda x: None if pd.isna(x) else x)

        yield chunk

def insert_data_to_db(connection, df, table_name):
    data = [[None if pd.isna(value) else value for value in row] for row in df.values]
    columns = list(df.columns)
    placeholders = ', '.join(['%s'] * len(columns))
    columns_str = ', '.join(columns)
    query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"

    try:
        print(f"Executing query: {query}")
        cursor = connection.cursor()
        cursor.executemany(query, data)
        connection.commit()
        print(f"Successfully inserted {len(data)} rows into {table_name}.")
    except Exception as e:
        print(f"Error executing query: {type(e).__name__} - {str(e)}")
    finally:
        cursor.close()

def process_data(file_path, table_name):
    db_config = get_db_config()
    date_columns = [
        'ACC_MONTH', 'KY_TT', 'NGAY_THANH_TOAN_PHIBH',
        'NGAY_CAPDON', 'INCEPTION_DATE', 'MATURITY_DATE'
    ]

    connection = connect_to_db(db_config)
    if connection is not None:
        try:
            for chunk in read_excel_data(file_path, date_columns):
                insert_data_to_db(connection, chunk, table_name)
        except Exception as e:
            print(f"Error: {type(e).__name__} - {str(e)}")
        finally:
            connection.close()
