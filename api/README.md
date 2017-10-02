example of using [django] in a sub dir with [traefik]

# Requirements

- [python] `v3.6+`
- [virtualenv]
- [docker] `v1.13+`

# Quick start

## local run

```bash
# first time
virtualenv .python-libs
pip install -r requirements.txt
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | python manage.py shell

# run django
python manage.py runserver 0.0.0.0:8000

```

## docker run

With a traefik server running in the background

```bash
# starts a django server in the background
docker-compose up -d

# run a bash in django container to exec python commands, eg migrate, create admin user
docker-compose exec django bash
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | python manage.py shell

```

## docker production run

Similar to development except using gunicorn with whitenoise to serve assets and no debug info

With a traefik server running in the background

```bash
# set env vars
export COMPOSE_PROJECT_NAME=exampleDjangoTraefik_prod
export COMPOSE_FILE=docker-compose.production.yml

# starts a django server in the background
docker-compose up -d

# run a bash in django container to exec python commands, eg migrate, create admin user
docker-compose exec django bash
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | python manage.py shell

```

generate a secret_key - https://gist.github.com/geoffalday/2021517#gistcomment-1496439
```python
import binascii
binascii.hexlify(os.urandom(24))

```

# TODO

- ssl certs
- secure according to django best practices
- set hostname in production (vs localhost)

---

[python]: https://www.python.org/
[virtualenv]: https://virtualenv.pypa.io/
[docker]: https://www.docker.com/
[traefik]: https://traefik.io/
[django]: https://www.djangoproject.com/
