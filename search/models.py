from distutils.spawn import spawn
from django.db import models

class Product(models.Model):
    un = models.CharField(max_length=200)
    psn = models.CharField(max_length=200)
    hazard = models.CharField(max_length=200)
    subrisk = models.CharField(max_length=200)
    pg = models.CharField(max_length=200)
    sp = models.CharField(max_length=200)
    paragraph = models.CharField(max_length=200)
    def haz_as_list(self):
        if len(self.hazard) == 0:
            return False
        return self.harzard.split(',')
    def sub_as_list(self):
        if len(self.subrisk) == 0:
            return False
        return self.subrisk.split(',')
    def pg_as_list(self):
        if len(self.pg) == 0:
            return False
        return self.pg.split(',')
    def sp_as_list(self):
        if len(self.sp) == 0:
            return False
        return self.sp.split(',')
    def paragraph_as_list(self):
        if len(self.paragraph) == 0:
            return False
        return self.paragraph.split(',')

class SpCode(models.Model):
    code = models.CharField(max_length=200)
    desc = models.TextField()

class HazClass(models.Model):
    code = models.CharField(max_length=200)
    desc = models.TextField()

class HazSubstance(models.Model):
    haz_psn = models.CharField(max_length=200)
    haz_weight_pounds = models.CharField(max_length=200)
    haz_weight_kilograms = models.CharField(max_length=200)
