Sample of django as an api server with JWT token auth and a create-react-app of the ever popular todo app

# Requirements

- [python] `v3+`
- [django] `v1.11+`
- [node] `v8+`
- [yarn]

# Quick start

```bash
# from project root

#
# first time
#

# install libraries
cd api && pip install -r requirements.txt && cd .. && \
cd frontend && yarn start && cd ..

# create admin user with username:admin password:adminadmin
cd api && python manage.py createsuperuser

# run migrations
cd api && python manage.py migrate

#
# every time - one shell per command
#

# start api server
cd api && python manage.py runserver

# start frontend
cd frontend && npm run develop

```

# TODO

- Split instructions between docker and local runs
- figure out better way to handle networking (everything in docker containers?)
- learn/apply best practices

[python]: https://www.python.org/
[django]: https://www.djangoproject.com/
[node]: https://nodejs.org/
[yarn]: https://yarnpkg.com/
