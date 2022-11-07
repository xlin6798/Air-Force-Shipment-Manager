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
    def haz_as_list(self):
        if len(self.product_haz_class) == 0:
            return False
        return self.product_haz_class.split(',')
    def sub_as_list(self):
        if len(self.product_sub_class) == 0:
            return False
        return self.product_sub_class.split(',')
    def pg_as_list(self):
        if len(self.product_pg) == 0:
            return False
        return self.product_pg.split(',')
    def sp_as_list(self):
        if len(self.product_sp) == 0:
            return False
        return self.product_sp.split(',')
    def paragraph_as_list(self):
        if len(self.product_paragraph) == 0:
            return False
        return self.product_paragraph.split(',')

class SpCode(models.Model):
    sp_code = models.CharField(max_length=200)
    sp_desc = models.CharField(max_length=200)

class HazClass(models.Model):
    haz_num = models.CharField(max_length=200)
    haz_name = models.CharField(max_length=200)
