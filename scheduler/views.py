from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
from .tasks import execute_jobs
from datetime import datetime, timedelta

class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        job = serializer.save()
        # schedule job based on interval
        if job.interval == 'weekly':
            execute_jobs.apply_async((job.id,), countdown=60 * 60 * 24 * 7)
        elif job.interval == 'daily':
            execute_jobs.apply_async((job.id,), countdown=60 * 60 * 24)
        # we can add other intervals if needed like monthly or custom
        job.next_run_at = datetime.now() + timedelta(days=7)  # this is an example for weekly (monday)
        job.save()

class JobDetailView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
