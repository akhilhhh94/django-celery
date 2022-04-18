

## Start redis server
```shell
docker run -p 8888:6379 --name some-redis -d redis redis-server --save 60 1 --loglevel warning
```

## Start beat
```shell
celery -A django_celery_example beat -l info
```

## Start worker
```shell
 celery -A django_celery_example worker -l info
```