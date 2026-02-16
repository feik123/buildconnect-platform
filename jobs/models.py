from django.db import models

from common.choices import CategoryChoices
from common.models import TimeStampModel


class City(models.Model):
    name = models.CharField(
        max_length=60,
        unique=True,
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=60,
        unique=True,
        choices=CategoryChoices.choices,
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Job(TimeStampModel):
    class StatusChoices(models.TextChoices):
        OPEN = 'open', 'Open'
        CLOSE = 'closed', 'Closed'

    title = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    category = models.ForeignKey(
        'jobs.Category',
        on_delete=models.CASCADE,
        related_name='jobs',
    )

    city = models.ForeignKey(
        'jobs.City',
        on_delete=models.CASCADE,
        related_name='jobs',
    )

    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.OPEN,
    )

    class Meta:
        ordering = ('-created_at',)

    def is_open(self):
        return self.status == self.StatusChoices.OPEN

    def __str__(self):
        return self.title

