
from django.contrib.auth import get_user_model, login
from django.test import TestCase
from django.urls import reverse

User = get_user_model()

class AuthTests(TestCase):

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'test',
            'email': 'email@email.com',
            'password1': 'test12345',
            'password2': 'test12345',
            'is_contractor': 'False',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)

    def test_login(self):
        User.objects.create_user(username='test', password='1234')

        response = self.client.post(reverse('login'), {
            'username': 'test',
            'password': '1234',
        })

        self.assertEqual(response.status_code, 302)