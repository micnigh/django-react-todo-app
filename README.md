Sample of django as an api server with JWT token auth and a create-react-app of todo-mvc

# Requirements

- [python] `v3+`
- [django] `v1.11+`
- [node] `v8+`

# Quick start

```bash
# from project root

# first time - install libraries
cd api && pip install -r requirements.txt && cd .. && \
cd frontend && npm install && cd ..

# every time - one shell per command
# api server
cd api && python manage.py runserver

# frontend
cd frontend && npm run develop

```

# TODO

- Split instructions between docker and local runs
- figure out better way to handle networking (everything in docker containers?)
- learn/apply best practices

[python]: https://www.python.org/
[django]: https://www.djangoproject.com/
[node]: https://nodejs.org/
