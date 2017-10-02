FROM python:3.6

WORKDIR /django/

COPY requirements.txt /django/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY ./ /django/
COPY docker/django/container/ /
RUN chmod +x /scripts/*.sh

# unbuffer python stdio so it shows up in docker logs
ENV PYTHONUNBUFFERED TRUE

ENTRYPOINT ["/scripts/entrypoint.sh"]
CMD python manage.py runserver 0.0.0.0:8000
