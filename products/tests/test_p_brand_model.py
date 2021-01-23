import uuid
from django.test import TestCase

from products.models import P_Brand

class BrandModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''
        Setup Test Data for Brand's model
        '''
        print("Testing Brand model")
        cls.brand = P_Brand.objects.create(
            brand_name="Gucci",
            brand_description="Luxary brand",
            brand_website="http://example.com/"
        )

    def get_label(self, field_name):
        return self.brand._meta.get_field(field_name).verbose_name

    def test_brand_name_label(self):
        '''
        Testing the label of brand_name
        '''
        self.assertEqual(self.get_label('brand_name'), 'brand name')

    def test_brand_description_label(self):
        '''
        Testing the label of brand_description
        '''
        self.assertEqual(self.get_label("brand_description"), 'brand description')

    def test_brand_logo_label(self):
        '''
        Testing the label of brand_logo
        '''
        self.assertEqual(self.get_label("brand_logo"), 'brand logo')

    def test_brand_website_label(self):
        '''
        Testing the label of website
        '''
        self.assertEqual(self.get_label("brand_website"), 'brand website')

    