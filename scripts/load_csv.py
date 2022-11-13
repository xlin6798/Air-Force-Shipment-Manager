import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")

from search.models import Product, SpCode, HazClass
import csv

with open('scripts/ProductList.csv') as file:
    reader = csv.reader(file)
    next(reader)  # Advance past the header

    Product.objects.all().delete()

    for row in reader:
        print(row)
        product = Product()
        product.product_un=row[0]
        product.product_psn=row[1]
        product.product_haz_class=row[2]
        product.product_sub_class=row[3]
        product.product_pg=row[4]
        product.product_sp=row[5]
        product.product_paragraph=row[6]
        product.save()

with open('scripts/SpCode.csv') as file:
    reader = csv.reader(file)
    next(reader)  # Advance past the header

    SpCode.objects.all().delete()

    for row in reader:
        print(row)
        spcode = SpCode()
        spcode.sp_code=row[0]
        spcode.sp_desc=row[1]
        spcode.save()

with open('scripts/HazClass.csv') as file:
    reader = csv.reader(file)
    next(reader)  # Advance past the header

    HazClass.objects.all().delete()

    for row in reader:
        print(row)
        hazclass = HazClass()
        hazclass.haz_num =row[0]
        hazclass.haz_name =row[1]
        hazclass.save()