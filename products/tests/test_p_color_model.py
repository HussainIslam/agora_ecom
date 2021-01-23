from django.test import TestCase

from products.models import P_Color

class ColorModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''
        Setup Test Data for Color model
        '''
        cls.color = P_Color.objects.create(
            color_name = "white",
            color_code_hex = "FFFFFF"
        )

    def get_label(self, field_name):
        '''
        Method to extract verbose name of field name
        '''
        return self.color._meta.get_field(field_name).verbose_name
    
    def test_color_name_label(self):
        '''
        Testing label of color name
        '''
        self.assertEqual(self.get_label("color_name"), "color name")
        
    def test_color_code_hex(self):
        '''
        Testing label of color code hex
        '''
        self.assertEqual(self.get_label("color_code_hex"), "color code hex")