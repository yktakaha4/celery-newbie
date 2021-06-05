import os
from abc import ABC
from time import sleep
from typing import List, Dict

from celery import Celery, Task

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")

app = Celery("proj")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


class BaseTask(Task, ABC):
    def on_success(self, retval, task_id, args, kwargs):
        print(f"success: {retval=}, {task_id=}, {args=}, {kwargs=}")

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        print(f"retry: {exc=}, {task_id=}, {args=}, {kwargs=}, {einfo=}")

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print(f"failure: {exc=}, {task_id=}, {args=}, {kwargs=}, {einfo=}")


@app.task(bind=True, base=BaseTask)
def count(self):
    COUNT = 3
    for i in range(0, COUNT):
        print(f"{COUNT - i}...")
        sleep(1)
    print("BOMB!!")


@app.task(bind=True, base=BaseTask)
def count_divisible_three(self, number: int) -> Dict[str, any]:
    if number < 1:
        raise ValueError(f"should be positive: ${number=}")

    start = 1
    end = number + 1

    results: List[int] = []
    for n in range(start, end):
        print(f"checking {n}...")
        if n % 3 == 0:
            results.append(n)
        sleep(1)

    return {"start": start, "end": number, "results": results}
