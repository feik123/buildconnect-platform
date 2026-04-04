from celery import shared_task


@shared_task
def notify_application_accepted(contractor_name, job_title):
    print(f'Notification: {contractor_name} accepted for {job_title}')