from django.db import models

# Create your models here.
class Todo(models.Model):
    done = models.BooleanField(default=False)
    description = models.CharField(max_length=120)
