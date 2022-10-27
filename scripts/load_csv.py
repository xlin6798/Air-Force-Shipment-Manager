import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")

from search.models import Product
import csv

with open('scripts/A41.csv') as file:
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
