from tkinter.constants import CASCADE

from django.conf import settings
from django.db import models
from django.db.models import Avg
from django.urls import reverse

from common.models import TimeStampModel


class Skill(models.Model):
    name = models.CharField(
        max_length=100
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Contractor(TimeStampModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='contractor',
        null=True,
        blank=True,
    )

    name = models.CharField(
        max_length=100
    )
    description = models.TextField()
    city = models.ForeignKey(
        'jobs.City',
        on_delete=models.CASCADE,
        related_name='contractors'
    )
    skills = models.ManyToManyField(
        'contractors.Skill',
        related_name='contractors',
        blank=True,
    )
    years_experience = models.PositiveIntegerField()

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('contractors:detail', kwargs={'pk': self.pk})

    @property
    def average_rating(self):
        return self.reviews.aggregate(avg=Avg('rating'))['avg']

    def __str__(self):
        return self.name






