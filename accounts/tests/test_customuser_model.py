from uuid import UUID
from datetime import date, datetime
from django.test import TestCase


from accounts.models import CustomUser, Address

class CustomUserTestClass(TestCase): 

    @classmethod
    def setUpTestData(cls):
        cls.billing_address = Address.objects.create(
            street_address= "30 Denton Avenue",
            city= "Toronto",
            province= "ON",
            postal_code= "M1L 4P2",
            country= "Canada"
        )

        cls.shipping_address = Address.objects.create(
            street_address= "10 Teesdale Place",
            city= "Scarborough",
            province= "ON",
            postal_code= "M1P 4E3",
            country= "Canada"
        )

        cls.customer = CustomUser.objects.create_user(
            first_name= "User",
            last_name= "One",
            username= "user1",
            date_of_birth= "2012-09-15",
            billing_address=cls.billing_address,
            shipping_address=cls.shipping_address,
            phone= "444-555-6666",
            email= "user1@gmail.com",
            password= "123456",
            gender= "Male",
            registered_on= "2012-09-15T22:17:44+00:00",
            last_modified= "2012-09-15T22:17:44+00:00",
            is_active= True,
            is_staff= False
        )

    def get_label(self, field_name):
        return self.customer._meta.get_field(field_name).verbose_name

    def test_user_id_label(self):
        self.assertEqual(self.get_label('user_id'), 'user id')

    def test_first_name_label(self):
        self.assertEqual(self.get_label('first_name'), 'first name')

    def test_last_name_label(self):
        self.assertEqual(self.get_label('last_name'), 'last name')

    def test_username_label (self):
        self.assertEqual(self.get_label('username'), 'username')
    
    def test_billing_address_label(self):
        self.assertEqual(self.get_label('billing_address'), 'billing address')

    def test_shipping_address_label(self):
        self.assertEqual(self.get_label('shipping_address'), 'shipping address')

    def test_dob_label(self):
        self.assertEqual(self.get_label('date_of_birth'), 'date of birth')

    def test_phone_label(self):
        self.assertEqual(self.get_label('phone'), 'phone')

    def test_email_label(self):
        self.assertEqual(self.get_label('email'), 'email')

    def test_password_label(self):
        self.assertEqual(self.get_label('password'), 'password')

    def test_gender_label(self):
        self.assertEqual(self.get_label('gender'), 'gender')

    def test_registered_on_label(self):
        self.assertEqual(self.get_label('registered_on'), 'registered on')

    def test_last_modified_label(self):
        self.assertEqual(self.get_label('last_modified'), 'last modified')
    
    def test_is_active_label(self):
        self.assertEqual(self.get_label('is_active'), 'is active')

    def test_is_staff_label(self):
        self.assertEqual(self.get_label('is_staff'), 'is staff')
    
    def test_user_id_type(self):
        self.assertIsInstance(self.customer.user_id, UUID)
    
    def test_first_name_type(self):
        self.assertIsInstance(self.customer.first_name, str)
    
    def test_last_name_type(self):
        self.assertIsInstance(self.customer.last_name, str)

    def test_username_type(self):
        self.assertIsInstance(self.customer.username, str)

    def test_billing_address_type(self):
        self.assertIsInstance(self.customer.billing_address, Address)
    
    def test_shipping_address_type(self):
        self.assertIsInstance(self.customer.shipping_address, Address)

    def test_dob_type(self):
        self.assertIsInstance(self.customer.date_of_birth, date)

    def test_phone_type(self):
        self.assertIsInstance(self.customer.phone, str)

    def test_gender_type(self):
        self.assertIsInstance(self.customer.gender, str)

    def test_registered_on_type(self):
        self.assertIsInstance(self.customer.registered_on, datetime)

    def test_last_modified_type(self):
        self.assertIsInstance(self.customer.last_modified, datetime)

    def test_is_active(self):
        self.assertIsInstance(self.customer.is_active, bool)

    def test_is_staff(self):
        self.assertIsInstance(self.customer.is_staff, bool)