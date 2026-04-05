
from django.test import TestCase
from django.urls import reverse


class APITests(TestCase):

    def test_job_list_api(self):
        response = self.client.get('/api/jobs/')

        self.assertEqual(response.status_code, 200)