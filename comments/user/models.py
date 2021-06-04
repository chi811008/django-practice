from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)

    username = None
    email = models.EmailField('email', unique=True)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
