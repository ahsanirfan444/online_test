from django.db import models
from django.contrib.auth.models import User

USER_TYPE = [('A', 'Admin'), ('N', 'Normal')]

class Profile(models.Model):
    i_user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(choices=USER_TYPE,max_length=2,default='N')
    class Meta:
        db_table = 'profile'