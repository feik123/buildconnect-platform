from django.contrib.auth import get_user_model
from django.test import TestCase

from contractors.models import Contractor
from jobs.models import City
from reviews.models import Review

class ReviewTests(TestCase):

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