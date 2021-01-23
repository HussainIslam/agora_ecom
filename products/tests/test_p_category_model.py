from django.test import TestCase

from products.models import P_Category

class CategoryModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category = P_Category.objects.create(
            category_name = "Men",
            category_description = "Everything a man needs",
            parent_category = None
        )

    def get_label(self, field_name):
        return self.category._meta.get_field(field_name).verbose_name

    def test_category_name_label(self):
        self.assertEqual(self.get_label('category_name'), 'category name')
    
    def test_category_description_label(self):
        self.assertEqual(self.get_label('category_description'), 'category description')

    def test_parent_cateogory_label(self):
        self.assertEqual(self.get_label('parent_category'), 'parent category')

    def test_query_with_uuid(self):
        category_fetched = P_Category.objects.get(category_id = self.category.category_id)
        self.assertEqual(self.category, category_fetched)

    def test_query_with_wrong_uuid(self):
        wrong_category = P_Category.objects.create(
            category_name = "Women",
            category_description = "Everything a woman needs",
            parent_category = None
        )
        category_fetched = P_Category.objects.get(category_id = self.category.category_id)
        self.assertNotEqual(category_fetched.category_id, wrong_category.category_id)
        self.assertNotEqual(category_fetched, wrong_category)

    