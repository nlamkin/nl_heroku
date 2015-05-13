from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
     text = models.CharField(max_length=160)
     author = models.ForeignKey(User, related_name="entry_creators")
     creation_time = models.DateTimeField()
