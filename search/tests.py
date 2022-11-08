from django.test import TestCase
from .models import Product, SpCode, HazClass

# Create your tests here.
class TestPages(TestCase):

    # Check to see if its lands to correct page
    def test_NA0331(self):
        page = self.client.get('/products/NA0331')
        self.assertEqual(page.status_code, 301)
