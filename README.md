# Django CRUD API

## Docs

- https://docs.djangoproject.com
- https://django-environ.readthedocs.io/
- https://www.django-rest-framework.org/
- https://drf-spectacular.readthedocs.io/en/latest/index.html
- https://bootswatch.com/

## URLS

- http://localhost:8000/
- http://localhost:8000/admin/
- http://localhost:8000/api/schema/
- http://localhost:8000/api/schema/swagger-ui/
- http://localhost:8000/api/schema/redoc/

## TODO

- Static Files
- Authentication
- User Creation
- Testing
- Versioning
- Caching
- Throttling
- Errors
- CSRF
- CORS
- Deployment
    - Docker
    - NGINX
    - Multiple Instances
    - Postgres DB - use neon?

## Docker

### Build

```shell
docker build -t api .
```

### Run

```shell
docker run --detach --publish 8000:8000 --name api --env SECRET_KEY=secret --env DATABASE_URL=sqlite:///db.sqlite3 api
```

## Exec

### Shell

```shell
docker exec -it api bash
```

### Migrate

```shell
docker exec -it api python manage.py migrate
```

### Collect Static

```shell
docker exec -it api python manage.py collectstatic --noinput
```

### Create Super User

```shell
docker exec -it api python manage.py createsuperuser --username user --email user@email.com
```
