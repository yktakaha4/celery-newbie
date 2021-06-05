from django.views.generic import View
from django.http import JsonResponse, HttpRequest

from proj.celery import count


class TaskView(View):
    def get(self, request: HttpRequest):
        task_name = request.GET.get('name')
        called = False

        if task_name == 'count':
            count.delay()
            called = True

        return JsonResponse({
            'task_name': task_name,
            'called': called
        })
