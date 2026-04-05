from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from jobs.models import Job, City, Category
from contractors.models import Contractor
from applications.models import Application

User = get_user_model()


class ApplicationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            password='1234'
        )

        self.user.profile.is_contractor = True
        self.user.profile.save()

        self.city, _ = City.objects.get_or_create(name='Sofia')
        self.category, _ = Category.objects.get_or_create(name='PAINTING')

        self.contractor = Contractor.objects.create(
            user=self.user,
            name='Test Contractor',
            description='desc',
            city=self.city,
            years_experience=5
        )

        self.owner = User.objects.create_user(
            username='owner',
            password='1234'
        )

        self.job = Job.objects.create(
            title='Test Job',
            description='desc',
            budget=100,
            city=self.city,
            category=self.category,
            owner=self.owner
        )

    def test_duplicate_application(self):
        self.client.login(username='test', password='1234')

        url = reverse('applications:create', kwargs={'pk': self.job.pk})

        data = {
            'message': 'Test message',
            'price_quote': 100,
        }

        response1 = self.client.post(url, data)
        self.assertEqual(response1.status_code, 302)

        response2 = self.client.post(url, data)
        self.assertEqual(response2.status_code, 200)

        self.assertEqual(Application.objects.count(), 1)

    def test_non_owner_cannot_accept(self):
        self.client.force_login(self.user)

        application = Application.objects.create(
            job=self.job,
            contractor=self.contractor,
            message='Test',
            price_quote=100
        )

        url = reverse('applications:accept', kwargs={'pk': application.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)

    def test_non_contractor_cannot_apply(self):
        non_contractor = User.objects.create_user(
            username='user2',
            password='1234'
        )

        self.client.force_login(non_contractor)

        url = reverse('applications:create', kwargs={'pk': self.job.pk})

        response = self.client.post(url, {
            'message': 'Test',
            'price_quote': 100,
        })

        self.assertEqual(response.status_code, 403)

    @patch('applications.views.notify_application_accepted.delay')
    def test_async_called(self, mock_task):
        self.client.login(username='owner', password='1234')

        application = Application.objects.create(
            job=self.job,
            contractor=self.contractor,
            message='Test',
            price_quote=100
        )

        url = reverse('applications:accept', kwargs={'pk': application.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

        mock_task.assert_called_once()