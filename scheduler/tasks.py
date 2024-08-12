from celery import shared_task
from datetime import datetime, timedelta
from .models import Job
from django.utils import timezone

@shared_task
def execute_jobs(job_id):
    jobs = Job.objects.filter(is_active=True)
    for job in jobs:
        if job.next_run and job.next_run <= timezone.now():
            #job logic (eg- sending an email)
            print(f"Executing job: {job.name}")
            job.last_run = timezone.now()
            job.next_run = job.last_run + timezone.timedelta(days=7)  #next run on next Monday
            job.save()

@shared_task
def send_email_notification():
    # Dummy job logic: Simulate sending an email
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Sending email notification to users...")
    # Add any additional logic here, like connecting to an SMTP server, etc.
    return "Email notification sent successfully."            