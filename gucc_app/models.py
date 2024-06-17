from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=20, default="member")
    admin = models.BooleanField(default=False)

class Helmet(models.Model):
    type = models