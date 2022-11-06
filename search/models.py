from distutils.spawn import spawn
from django.db import models

class Product(models.Model):
    product_un = models.CharField(max_length=200)
    product_psn = models.CharField(max_length=200)
    product_haz_class = models.CharField(max_length=200)
    product_sub_class = models.CharField(max_length=200)
    product_pg = models.CharField(max_length=200)
    product_sp = models.CharField(max_length=200)
    product_paragraph = models.CharField(max_length=200)

class SpCode(models.Model):
    sp_code = models.CharField(max_length=200)
    sp_desc = models.CharField(max_length=200)

class HazClass(models.Model):
    haz_num = models.CharField(max_length=200)
    haz_name = models.CharField(max_length=200)
