

## Start beat
```shell
celery -A django_celery_example beat -l info
```

## Start worker
```shell
 celery -A django_celery_example worker -l info
```