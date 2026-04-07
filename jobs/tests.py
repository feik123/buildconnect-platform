from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from accounts.tests.utils import create_user
from jobs.models import Job, City, Category

User = get_user_model()

class JobTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='owner',
            password='1234'
        )

        self.city, _ = City.objects.get_or_create(name='Sofia')
        self.category, _ = Category.objects.get_or_create(name='PAINTING')

        self.job = Job.objects.create(
            title='Test Job',
            description='desc',
            budget=100,
            city=self.city,
            category=self.category,
            owner=self.user,
            status='open'
        )

    def test_job_create_requires_login(self):
        response = self.client.get(reverse('jobs:create'))
        self.assertEqual(response.status_code, 302)

    def test_create_job_sets_owner(self):
        user = create_user()
        self.client.login(username='testuser', password='1234')

        response = self.client.post(reverse('jobs:create'), {
            'title': 'Test job',
            'description': 'Test',
            'budget': 100,
            'city': 1,
            'category': 1
        })

        job = Job.objects.first()
        self.assertEqual(job.owner, user)

    def test_owner_can_edit_job(self):
        self.client.login(username='owner', password='1234')

        url = reverse('jobs:edit', kwargs={'pk': self.job.pk})

        response = self.client.post(url, {
            'title': 'Updated',
            'description': 'Updated desc',
            'budget': 200,
            'city': self.city.id,
            'category': self.category.id,
            'status': 'open',
        })

        self.assertEqual(response.status_code, 302)

    def test_non_owner_cannot_edit_job(self):
        other_user = User.objects.create_user(
            username='other',
            password='1234'
        )

        self.client.login(username='other', password='1234')

        url = reverse('jobs:edit', kwargs={'pk': self.job.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)