from django.db import models
from django.contrib.auth.models import User

class Rooms(models.Model):
    code = models.CharField(max_length=8, default='', unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Rooms'


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Posts"