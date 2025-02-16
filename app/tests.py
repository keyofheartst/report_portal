# -*- encoding: utf-8 -*-


from django.test import TestCase
from django.db import connections
from django.db.utils import OperationalError
from django.http import JsonResponse
from django.template.context_processors import request
from app import file_extract
from app.fetch_data import get_summary_revenue_data


def check_db_connection(request):
    db_conn = connections['default']
    try:
        c = db_conn.cursor()
        c.execute("SELECT 1+1")
        return JsonResponse({'status': 'success', 'message': 'Database connection successful.'})
    except OperationalError as e:
        return JsonResponse({'status': 'error', 'message': 'Database connection failed.', 'error': str(e)})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': 'An error occurred.', 'error': str(e)})

def testReadDataFromFile(request):
    file_path = r'E:\STUDY\DATA_ENGINEER\Dataset\5b_data.xlsx'
    table_name = 'T_CLAIM_SUMMARY'
    process_data.processDataFromFile(file_path, table_name)

def test_get_data(request):
    get_summary_revenue_data()