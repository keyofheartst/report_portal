import sys
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
from app.db_utils import get_db_config, connect_to_db
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.file_extract import process_data

# Cấu hình DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'process_excel_to_db',
    default_args=default_args,
    description='DAG to process Excel file and insert data into MySQL',
    schedule_interval=None,  # Có thể đặt lịch chạy hàng ngày hoặc mỗi giờ nếu cần
    catchup=False,
)

# Định nghĩa task xử lý dữ liệu
def process_excel():
    file_path = "/path/to/your/file.xlsx"  # Đường dẫn tới file Excel
    table_name = "your_table_name"  # Tên bảng trong database
    process_data(file_path, table_name)

process_task = PythonOperator(
    task_id='process_excel_file',
    python_callable=process_excel,
    dag=dag,
)

process_task
