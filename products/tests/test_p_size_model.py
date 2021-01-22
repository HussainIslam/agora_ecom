from django.test import TestCase

from products.models import P_Size, P_Category

class SizeModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.categ = P_Category.objects.create(
            category_name = "Shirt",
            category_description = "Shirts for men",
            parent_category = None
        )
        cls.size = P_Size.objects.create(
            category = cls.categ,
            value = "Large"
        )
    
    def test_value_label(self):
        value_label = self.size._meta.get_field('value').verbose_name
        self.assertEqual(value_label, 'value')

    def test_size_category(self):
        self.assertEqual(self.categ.category_id, self.size.category.category_id)
        self.assertEqual(self.categ, self.size.category)