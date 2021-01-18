from django.test import TestCase

class ProductsTestClass(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        print("Setup Test Data")
        pass

    def setUp(self):
        print("Setup")
        pass

    def test_false_is_false(self):
        print("false is false")
        self.assertFalse(False)