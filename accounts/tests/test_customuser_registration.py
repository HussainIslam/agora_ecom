import json
from pprint import pprint
from django.test import TestCase
from django.urls import reverse, resolve

from accounts.models import Address, CustomUser

class UserRegistrationTestClass(TestCase):

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
        cls.url = reverse('accounts:registration')
        cls.resolver = resolve('/users/')
        cls.userobject = {
            "email": "testuser@gmail.com",
            "password": "Password123!"
        }

    def test_user_registration(self):
        self.assertEqual(self.url, '/users/')
    
    def test_registration_url_name(self):
        self.assertEqual(self.resolver.url_name, 'registration')
        
    def test_get_wrong_status_code(self):
        response = self.client.get(self.url)
        self.assertNotEqual(response.status_code, 200)
    
    def test_get_correct_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)

    def test_post_correct_status_code(self):
        response = self.client.post(path=self.url, data=self.userobject, content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_post_response_email(self):
        response = self.client.post(path=self.url, data=self.userobject, content_type='application/json')
        self.assertEqual(response.data['email'], self.userobject['email'])
    
    def test_post_response_password(self):
        response = self.client.post(path=self.url, data=self.userobject, content_type='application/json')
        self.assertNotEqual(response.data['password'], self.userobject['password'])

    def test_post_response_no_password(self):
        response = self.client.post(path=self.url, data=self.userobject, content_type='application/json')
        self.assertNotContains(response.data, 'password')