from django.db import models

class Job(models.Model):
    INTERVAL_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('custom', 'Custom'),
    ]
    name = models.CharField(max_length=255)
    interval = models.CharField(max_length=10, choices=INTERVAL_CHOICES, default='weekly') # eg - 'daily', 'weekly'
    last_run_at = models.DateTimeField(null=True, blank=True)
    next_run_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
