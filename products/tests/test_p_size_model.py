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
    
    def get_label(self, field_name):
        '''
        Method to extract verbose name from field name
        '''
        return self.size._meta.get_field(field_name).verbose_name
    
    def test_value_label(self):
        '''
        Testing label of value field
        '''
        self.assertEqual(self.get_label('value'), 'value')

    def test_size_category(self):
        '''
        Testing whether size is pointing to the correct category
        '''
        self.assertEqual(self.categ.category_id, self.size.category.category_id)
        self.assertEqual(self.categ, self.size.category)