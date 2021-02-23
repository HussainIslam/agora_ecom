import json
from pprint import pprint
from django.test import TestCase
from django.urls import reverse, resolve

from accounts.models import Address, CustomUser

class UserRegistrationTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('accounts:registration')
        cls.resolver = resolve('/users/')
        cls.email = "testuser@gmail.com"
        cls.password = "Password123!"
        cls.userobject = {
            "email": cls.email,
            "password": cls.password
        }

    def setUp(self):
        self.response = self.client.post(path=self.url, data=self.userobject, content_type='application/json')

    def test_user_registration_url(self):
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
        self.assertEqual(self.response.status_code, 201)
    
    def test_post_response_email(self):
        self.assertEqual(self.response.data['email'], self.userobject['email'])
    
    def test_post_response_password(self):
        self.assertNotEqual(self.response.data['password'], self.userobject['password'])

    def test_post_response_no_password(self):
        self.assertNotContains(self.response.data, 'password')

    def test_user_created(self):
        user = CustomUser.objects.get(email=self.email)
        self.assertEqual(user.email, self.email)