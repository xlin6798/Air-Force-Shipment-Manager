import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")

from search.models import Product, SpCode, HazClass, HazSubstance
import csv

with open('scripts/ProductList.csv') as file:
    reader = csv.reader(file)
    next(reader)  # Advance past the header

    Product.objects.all().delete()

    for row in reader:
        print(row)
        product = Product()
        product.un=row[0]
        product.psn=row[1]
        product.hazard=row[2]
        product.subrisk=row[3]
        product.pg=row[4]
        product.sp=row[5]
        product.paragraph=row[6]
        product.save()

with open('scripts/SpCode.csv') as file:
    reader = csv.reader(file)
    next(reader)  # Advance past the header

    SpCode.objects.all().delete()

    for row in reader:
        print(row)
        spcode = SpCode()
        spcode.code=row[0]
        spcode.desc=row[1]
        spcode.save()

with open('scripts/HazClass.csv') as file:
    reader = csv.reader(file)
    next(reader)  # Advance past the header

    HazClass.objects.all().delete()

    for row in reader:
        print(row)
        hazclass = HazClass()
        hazclass.code =row[0]
        hazclass.desc =row[1]
        hazclass.save()

with open('scripts/HazSubstanceUpdate.csv') as file:
    reader = csv.reader(file)
    next(reader)  # Advance past the header

    HazSubstance.objects.all().delete()

    for row in reader:
        print(row)
        hazsubstance = HazSubstance()
        hazsubstance.psn =row[0]
        hazsubstance.weight_lbs =row[1]
        hazsubstance.weight_kgs =row[2]
        hazsubstance.save()
