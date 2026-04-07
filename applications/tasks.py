from celery import shared_task
from django.core.mail import send_mail


@shared_task
def notify_application_accepted(contractor_name, job_title):
    send_mail(
        subject='Application Accepted',
        message=f'{contractor_name}, your application for "{job_title}" was accepted.',
        from_email='noreply@buildconnect.com',
        recipient_list=['test@test.com'],
    )