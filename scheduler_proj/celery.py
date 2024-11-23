# scheduler_proj/celery.py

from __future__ import absolute_import, unicode_literals
import os                       #way of using operating system dependent functionality
from celery import Celery       #imports 'Celery' class from 'celery' module 

#sets an environment variable to 'scheduler_proj.settings' , This is necessary because Celery 
#Celery needs to know where to find the Django project's settings.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scheduler_proj.settings') 

#creates a new Celery application instance, passing the name of the project ('scheduler_proj') to it                                                                           #needs to know where to find the Django project's settings.
app = Celery('scheduler_proj')      
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
