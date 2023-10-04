import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Main_app.settings')

app = Celery('fish_market')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.update(
    broker_connection_retry_on_startup=True
)
