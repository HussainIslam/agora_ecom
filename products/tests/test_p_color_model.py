from django.test import TestCase

from products.models import P_Color

class ColorModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.color = P_Color.objects.create(
            color_name = "white",
            color_code_hex = "FFFFFF"
        )
    
    def test_color_name_label(self):
        name_label = self.color._meta.get_field("color_name").verbose_name
        self.assertEqual(name_label, "color name")
        
    def test_color_code_hex(self):
        code_label = self.color._meta.get_field("color_code_hex").verbose_name
        self.assertEqual(code_label, "color code hex")