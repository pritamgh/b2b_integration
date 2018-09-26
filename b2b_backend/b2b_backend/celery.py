import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'b2b_backend.settings')

app = Celery('b2b_backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
