
from django.db import models
from django.urls import reverse

from common.models import TimeStampModel


class Application(TimeStampModel):


    class ApplicationChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        ACCEPTED = 'accepted', 'Accepted'
        REJECTED = 'rejected', 'Rejected'

    job = models.ForeignKey(
        'jobs.Job',
        on_delete=models.CASCADE,
        related_name='applications'
    )
    contractor = models.ForeignKey(
        'contractors.Contractor',
        on_delete=models.CASCADE,
        related_name='applications'
    )
    message = models.TextField()
    price_quote = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    status = models.CharField(
        max_length=10,
        choices=ApplicationChoices.choices,
        default=ApplicationChoices.PENDING,
    )

    class Meta:
        ordering = ('-created_at',)
        constraints = [
            models.UniqueConstraint(
                fields=['job', 'contractor'],
                name='unique_job_contractor'
            )
        ]

    def get_absolute_url(self):
        return reverse('jobs:detail', kwargs={'pk': self.job.pk})

    def __str__(self):
        return f'Application by {self.contractor.name} for {self.job.title}'
