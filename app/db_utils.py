import json
import pymysql
import os

def get_db_config():
    # Get the absolute path of the current file's directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to the db_config.json file
    config_path = os.path.join(current_dir, 'db_config.json')
    with open(config_path, 'r') as file:
        return json.load(file)

def connect_to_db(db_config):
    try:
        print("Đang kết nối đến cơ sở dữ liệu...")
        connection = pymysql.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database'],
            charset=db_config['charset']
        )
        print("Kết nối thành công.")
        return connection
    except Exception as e:
        print(f"Lỗi khi kết nối đến cơ sở dữ liệu: {type(e).__name__} - {str(e)}")
        return None