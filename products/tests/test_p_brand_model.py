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

    def test_brand_name_label(self):
        '''
        Testing the label of brand_name
        '''
        name_label = self.brand._meta.get_field("brand_name").verbose_name
        self.assertEqual(name_label, 'brand name')

    def test_brand_description_label(self):
        '''
        Testing the label of brand_description
        '''
        description_label = self.brand._meta.get_field("brand_description").verbose_name
        self.assertEqual(description_label, 'brand description')

    def test_brand_logo_label(self):
        '''
        Testing the label of brand_logo
        '''
        logo_label = self.brand._meta.get_field("brand_logo").verbose_name
        self.assertEqual(logo_label, 'brand logo')

    def test_brand_website_label(self):
        '''
        Testing the label of website
        '''
        website_label = self.brand._meta.get_field("brand_website").verbose_name
        self.assertEqual(website_label, 'brand website')

    