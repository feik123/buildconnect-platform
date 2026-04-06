
from django.test import TestCase
from django.urls import reverse

from accounts.tests.utils import create_user
from jobs.models import Job


class JobTests(TestCase):

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