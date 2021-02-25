from django.test import TestCase
from django.urls import reverse, resolve

from accounts.models import CustomUser

class UserLogoutTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.email = "testuser@gmail.com"
        cls.password = "Password123!"
        cls.userobject = {
            "email": cls.email,
            "password": cls.password
        }
        cls.reg_url = reverse('accounts:registration')
        cls.login_url = reverse('accounts:login')
        cls.logout_url = reverse('accounts:logout')
        cls.resolver = resolve('/users/logout/')

    def register_login(self):
        self.client.post(path=self.reg_url, data=self.userobject, content_type="application/json")
        self.login_response = self.client.post(path=self.login_url, data=self.userobject, content_type="application/json")

    def register_login_logout(self):
        self.register_login()
        self.response = self.client.post(path=self.logout_url, data=self.login_response.data, content_type="application/json")

    def test_user_logout_url(self):
        self.assertEqual(self.logout_url, '/users/logout/')

    def test_user_logout_url_name(self):
        self.assertEqual(self.resolver.url_name, 'logout')
        
    def test_get_wrong_status_code(self):
        response = self.client.get(path=self.logout_url)
        self.assertNotEqual(response.status_code, 205)

    def test_get_correct_status_code(self):
        response = self.client.get(path=self.logout_url)
        self.assertEqual(response.status_code, 405)

    def test_post_correct_status_code(self):
        self.register_login_logout()
        self.assertEqual(self.response.status_code, 205)
    
    def test_post_wrong_status_code(self):
        self.register_login_logout()
        self.assertNotEqual(self.response.status_code, 400)
    
    def test_post_response_contains_message(self):
        self.register_login_logout()
        self.assertIn('message', self.response.data)
    
    def test_post_response_contains_content_type(self):
        self.register_login_logout()
        self.assertIn('content-type', self.response)
    
    def test_post_response_content_type_value(self):
        self.register_login_logout()
        self.assertEqual(self.response['content-type'], 'application/json')
