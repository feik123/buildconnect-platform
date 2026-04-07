from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from contractors.models import Contractor, Skill
from jobs.models import City, Category, Job
from reviews.models import Review

User = get_user_model()

class ReviewTests(TestCase):

    def setUp(self):
        self.owner = User.objects.create_user(
            username='owner',
            password='1234'
        )

        self.skill = Skill.objects.create(name='Painting')

        self.contractor_user = User.objects.create_user(
            username='contractor',
            password='1234'
        )

        self.contractor_user.profile.is_contractor = True
        self.contractor_user.profile.save()

        self.city, _ = City.objects.get_or_create(name='Sofia')
        self.category, _ = Category.objects.get_or_create(name='PAINTING')

        self.contractor = Contractor.objects.create(
            user=self.contractor_user,
            name='Test Contractor',
            description='desc',
            city=self.city,
            years_experience=5
        )

        self.job = Job.objects.create(
            title='Test Job',
            description='desc',
            budget=100,
            city=self.city,
            category=self.category,
            owner=self.owner
        )


    def test_create_review(self):
        User = get_user_model()

        user = User.objects.create_user(
            username='test',
            password='1234'
        )

        city, _ = City.objects.get_or_create(name="Sofia")

        contractor = Contractor.objects.create(
            user=user,
            name="Test",
            description="Test",
            city=city,
            years_experience=1,
        )

        review = Review.objects.create(
            contractor=contractor,
            user=user,
            rating=5,
            comment="Great"


        )

        self.assertEqual(Review.objects.count(), 1)

    def test_duplicate_review(self):
        self.client.login(username='owner', password='1234')

        Review.objects.create(
            contractor=self.contractor,
            user=self.owner,
            rating=5,
            comment='Good'
        )

        url = reverse('reviews:create', kwargs={'pk': self.contractor.pk})

        response = self.client.post(url, {
            'rating': 5,
            'comment': 'Again'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Review.objects.count(), 1)

    def test_create_contractor_profile(self):
        user = User.objects.create_user(username='new', password='1234')

        user.profile.is_contractor = True
        user.profile.save()

        self.client.login(username='new', password='1234')

        url = reverse('contractors:create')

        response = self.client.post(url, {
            'name': 'Test',
            'description': 'desc',
            'city': self.city.id,
            'years_experience': 2,
            'skills': [self.skill.id]
        })

        self.assertEqual(response.status_code, 302)