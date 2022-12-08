from django.test import TestCase
from .models import Product, SpCode, HazClass, HazSubstance

# Create your tests here.
class TestPages(TestCase):

    # Check to see if its lands to correct page
    # def test_NA0331(self):
    #     page = self.client.get('/products/128/')
    #     self.assertEqual(page.status_code, 301)

    def test_HazardPage(self):
        page = self.client.get('/hazard')
        self.assertEqual(page.status_code, 200)

    # def test_ShipmentHistoryPage(self):
    #     page = self.client.get('/shipmentHistory')
    #     self.assertEqual(page.status_code, 200)