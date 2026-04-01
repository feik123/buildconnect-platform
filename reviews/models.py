from django.conf import settings
from django.db import models

import contractors.models
from common.models import TimeStampModel


class Review(TimeStampModel):
    RATING_CHOICES = [
        (1, '1 ⭐'),
        (2, '2 ⭐'),
        (3, '3 ⭐'),
        (4, '4 ⭐'),
        (5, '5 ⭐'),
    ]

    contractor = models.ForeignKey(
        'contractors.Contractor',
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    rating = models.IntegerField(choices=RATING_CHOICES)

    comment = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['contractor', 'user'],
                name='unique_review_per_user'
            )
        ]

    def __str__(self):
        return f'{self.user} -> {self.contractor} ({self.rating})'