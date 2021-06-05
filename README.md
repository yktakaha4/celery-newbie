# celery-newbie

https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html

## Prerequirements

- poetry
- docker-compose

## Development

```
$ make dev

# 実行
$ curl -s 'http://localhost:8000/task/execute/?name=count_divisible_three&number=100' | jq
{
  "task_name": "count_divisible_three",
  "task_id": "6328ede8-00ed-4f5e-b9b3-563abe005d31"
}

# 結果取得
$ curl -s 'http://localhost:8000/task/result/?id=6328ede8-00ed-4f5e-b9b3-563abe005d31' | jq
{
  "task_id": "6328ede8-00ed-4f5e-b9b3-563abe005d31",
  "status": "STARTED",
  "result": null
}

$ curl -s 'http://localhost:8000/task/result/?id=d68eadc7-5551-43b6-a240-d67c47c59b5d' | jq | head
{
  "task_id": "d68eadc7-5551-43b6-a240-d67c47c59b5d",
  "status": "SUCCESS",
  "result": {
    "start": 1,
    "end": 100,
    "results": [
      3,
      6,
      9,
```
