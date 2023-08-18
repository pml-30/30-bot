from celery import Celery
from celery.schedules import crontab

from app.core.config import ApplicationSettings

settings = ApplicationSettings()

app = Celery(
    "tasks",
    broker=settings.broker.dsn,
    backend=str(settings.redis.dsn),
    include=["app.services.tasks"],
)


app.conf.update(
    result_expires=3600,
    beat_schedule={
        "update_schedule": {
            "task": "app.services.tasks.update_schedule",
            "schedule": crontab(minute="0", hour="0"),
        }
    },
    timezone="Europe/Moscow"
)
