import sys
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.fetch_data import get_summary_revenue_data
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    # 'start_date': datetime(2024, 2, 1),
    'start_date': datetime(2025, 2, 17, 4, 25),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'fetch_data_from_db',
    default_args=default_args,
    description='DAG to fetch data from MySQL database automatically',
    #schedule_interval='@daily',
    schedule_interval=None,  #  Không chạy tự động vào airflow bấm trigger chạy manual để test
    catchup=False,
)

def fetch_data():
    get_summary_revenue_data()

fetch_task = PythonOperator(
    task_id='fetch_data_from_db',
    python_callable=fetch_data,
    dag=dag,
)

fetch_task
