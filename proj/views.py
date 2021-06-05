from celery.result import AsyncResult
from django.views.generic import View
from django.http import JsonResponse, HttpRequest

from proj.celery import count, count_divisible_three


class TaskExecuteView(View):
    def get(self, request: HttpRequest):
        try:
            task_name = request.GET.get('name')
            task = None

            if task_name == 'count':
                task = count.apply_async()
            elif task_name == 'count_divisible_three':
                number = int(request.GET['number'])
                task = count_divisible_three.apply_async([number])

            task_id = task.id if task else None

            return JsonResponse({
                'task_name': task_name,
                'task_id': task_id,
            })
        except Exception as e:
            return JsonResponse({
                'error': True,
                'message': str(e)
            })


class TaskResultView(View):
    def get(self, request: HttpRequest):
        try:
            task_id = request.GET['id']
            task = AsyncResult(task_id)

            status = None
            result = None
            if task:
                status = task.status
                if status == 'SUCCESS':
                    result = task.get()

            return JsonResponse({
                'task_id': task_id,
                'status': status,
                'result': result,
            })
        except Exception as e:
            return JsonResponse({
                'error': True,
                'message': str(e)
            })
