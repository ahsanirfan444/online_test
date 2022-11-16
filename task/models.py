from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    i_user = models.OneToOneField(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    class Meta:
        db_table = 'task_db'