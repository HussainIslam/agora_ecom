from django.test import TestCase

from django.urls import reverse, resolve

class ChangePasswordTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.email = "testuser@gmail.com"
        cls.password = "Password123!"
        cls.reg_url = reverse("accounts:registration")
        cls.login_url = reverse("accounts:login")
        cls.change_pass_url = reverse("accounts:change_password")
        cls.resolver = resolve('/users/change-password/')

    def setUp(self):
        userobject = {
            "email": self.email,
            "password": self.password
        }
        self.client.post(path=self.reg_url, data=userobject, content_type="application/json")
        self.login_resp = self.client.post(path=self.login_url, data=userobject, content_type="application/json")
    
    def change_pass_request(self, old_password="Password123!", new_password="Updated123!"):
        request_data = {
            "old_password": old_password,
            "new_password": new_password
        }
        header = {
            "HTTP_AUTHORIZATION": self.login_resp.data['access']
        }
        return self.client.put(path=self.change_pass_url, data=request_data, content_type="application/json", **header)

    def test_change_password_url(self):
        self.assertEqual(self.change_pass_url, '/users/change-password/')
    
    def test_change_password_url_name(self):
        self.assertEqual(self.resolver.url_name, 'change_password')

    def test_get_wrong_status_code(self):
        response = self.client.get(path=self.change_pass_url)
        self.assertNotEqual(response.status_code, 200)

    def test_get_correct_status_code(self):
        response = self.client.get(path=self.change_pass_url)
        self.assertEqual(response.status_code, 405)

    def test_post_correct_pass_status_code(self):
        response = self.change_pass_request()
        self.assertEqual(response.status_code, 204)
    
    def test_post_wrong_pass_status_code(self):
        response = self.change_pass_request(old_password="Wrong123!")
        self.assertEqual(response.status_code, 403)
        self.assertNotEqual(response.status_code, 204)
    
    def test_post_invalid_pass_status_code(self):
        response = self.change_pass_request(new_password="ABCD")
        self.assertEqual(response.status_code, 400)
        self.assertNotEqual(response.status_code, 200)
