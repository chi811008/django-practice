from django.db import models
from django.conf import settings
# Create your models here.
from rest_framework import serializers
from datetime import datetime
# from user.models import User

class Comment(models.Model):
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user_name = models.ForeignKey(User, on_delete=models.CASCAD
    content = models.CharField(max_length=200)
    created = models.DateTimeField()