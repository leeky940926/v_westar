import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE","v_westar.settings")
django.setup()

from products.models import *

CSV_PATH_PRODUCTS = 'products/starbucks.csv'

with open(CSV_PATH_PRODUCTS) as in_file :
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader :
        if row[0]  :
            menu_name = row[0]
            Menu.objects.create(name=menu_name)
