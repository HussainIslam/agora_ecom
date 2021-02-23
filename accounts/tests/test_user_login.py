from django.test import TestCase
from django.urls import reverse, resolve

class LoginTestClass(TestCase):

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
        cls.resolver = resolve('/users/login/')
    
    def setUp(self):
        self.response = self.client.post(path=self.reg_url, data=self.userobject, content_type="application/json")

    def test_user_login_url(self):
        self.assertEqual(self.login_url, '/users/login/')

    def test_user_login_url_name(self):
        self.assertEqual(self.resolver.url_name, 'login')

    def test_get_wrong_status_code(self):
        response = self.client.get(path=self.login_url)
        self.assertNotEqual(response.status_code, 200)
    
    def test_get_correct_status_code(self):
        response = self.client.get(path=self.login_url)
        self.assertEqual(response.status_code, 405)
    
    def test_post_correct_status_code(self):
        req_data = {
            'email': self.email, 
            'password': self.password
        }
        login_response = self.client.post(path=self.login_url, data=req_data, content_type='application/json')
        self.assertEqual(login_response.status_code, 200)