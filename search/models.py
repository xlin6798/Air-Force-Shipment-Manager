from django.db import models

class Product(models.Model):
    product_un = models.CharField(max_length=200)
    product_psn = models.CharField(max_length=200)
    product_haz_class = models.CharField(max_length=200)
    product_sub_class = models.CharField(max_length=200)
    product_pg = models.CharField(max_length=200)
    product_sp = models.CharField(max_length=200)
    product_paragraph = models.CharField(max_length=200)