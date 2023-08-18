from .celery import app


@app.task
def update_schedule():
    pass
