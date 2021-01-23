import uuid
from django.test import TestCase

from products.models import P_Brand

class BrandModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''
        Setup Test Data for Brand's model
        '''
        cls.brand = P_Brand.objects.create(
            brand_name="Gucci",
            brand_description="Luxary brand",
            brand_website="http://example.com/"
        )

    def get_label(self, field_name):
        '''
        Method to extract verbose name from field name
        '''
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

    def test_instance_of_brand(self):
        '''
        Testing whether brand is an instance of P_Brand
        '''
        self.assertTrue(isinstance(self.brand, P_Brand))

    def test_query_with_uuid(self):
        brand_fetched = P_Brand.objects.get(brand_id = self.brand.brand_id)
        self.assertEqual(self.brand, brand_fetched)

    def test_query_with_wrong_uuid(self):
        '''
        Testing feting brand with wrong uuid
        '''
        wrong_brand = P_Brand.objects.create(
            brand_name="Levi's",
            brand_description="Jeans brand",
            brand_website="http://levis.com/"    
        )
        brand_fetched = P_Brand.objects.get(brand_id = self.brand.brand_id)
        self.assertNotEqual(brand_fetched.brand_id, wrong_brand.brand_id)
        self.assertNotEqual(brand_fetched, wrong_brand)

    def test_get_str(self):
        '''
        Testing model str function
        '''
        self.assertEqual(str(self.brand), self.brand.brand_name)

    