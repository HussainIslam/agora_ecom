from django.test import TestCase

from products.models import P_Category

class CategoryModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("Testing Category model")
        cls.category = P_Category.objects.create(
            category_name = "Men",
            category_description = "Everything a man needs",
            parent_category = None
        )

    def test_category_name_label(self):
        name_label = self.category._meta.get_field('category_name').verbose_name
        self.assertEqual(name_label, 'category name')
    
    def test_category_description_label(self):
        description_label = self.category._meta.get_field('category_description').verbose_name
        self.assertEqual(description_label, 'category description')

    def test_parent_cateogory_label(self):
        parent_cat_label = self.category._meta.get_field('parent_category').verbose_name
        self.assertEqual(parent_cat_label, 'parent category')

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

    