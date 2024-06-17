from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=20, default="member")
    admin = models.BooleanField(default=False)

class ItemType(models.Model):
    name = models.CharField(max_length=120, null=False)
    attributes = models.CharField(max_length=1000, null=False) #<name:>

class Item(models.Model):
    