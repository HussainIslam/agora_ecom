import uuid
from django.test import TestCase

from products.models import P_Brand

class BrandTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        P_Brand.objects.create(
            brand_name="Test",
            brand_description="Test Description",
            brand_website="http://example.com/"
        )

    def setUp(self):
        self.brand = P_Brand.objects.get(brand_name="Test")

    def test_brand_name_label(self):
        name_label = self.brand._meta.get_field("brand_name").verbose_name
        self.assertEqual(name_label, 'brand name')

    def test_brand_description_label(self):
        description_label = self.brand._meta.get_field("brand_description").verbose_name
        self.assertEqual(description_label, 'brand description')

    def test_brand_logo_label(self):
        logo_label = self.brand._meta.get_field("brand_logo").verbose_name
        self.assertEqual(logo_label, 'brand logo')

    def test_brand_website_label(self):
        website_label = self.brand._meta.get_field("brand_website").verbose_name
        self.assertEqual(website_label, 'brand website')

    