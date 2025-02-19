import logging
import pandas as pd
from app.db_utils import get_db_config, connect_to_db

# Sử dụng logging của Airflow
logger = logging.getLogger("airflow.task")

def fetch_data_from_table(connection, table_name):
    query = f"SELECT * FROM {table_name}"
    try:
        df = pd.read_sql(query, connection)
        logger.info(f"✅ Successfully fetched data from {table_name}")
        return df
    except Exception as e:
        logger.error(f"❌ Error fetching data from {table_name}: {type(e).__name__} - {str(e)}", exc_info=True)
        return None
    finally:
        if connection:
            connection.close()
            logger.info("✅ Database connection closed.")

def get_summary_revenue_data():
    try:
        logger.info("🚀 Starting data fetch process...")
        db_config = get_db_config()
        connection = connect_to_db(db_config)

        if connection is not None:
            df = fetch_data_from_table(connection, 'T_SUMMARY_REVENUE')
            if df is not None:
                logger.info(f"📊 First row of data: {df.iloc[0].to_dict()}")
            else:
                logger.warning("⚠️ Failed to fetch data.")
        else:
            logger.error("❌ Failed to connect to the database.")
    except Exception as e:
        logger.critical(f"🔥 Unexpected error: {type(e).__name__} - {str(e)}", exc_info=True)
