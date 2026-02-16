from django.db import models

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

    def __str__(self):
        return self.name



