# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from app import views
from app import tests
urlpatterns = [
    # Matches any html file 
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('check-db/', tests.testReadDataFromFile, name='check_db_connection'),
path('get-data/', tests.test_get_data, name='test_get_data'),
]
