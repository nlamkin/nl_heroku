from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Performance(models.Model):
    date          = models.DateTimeField()
    time          = models.CharField(max_length=8, blank=True)
    production    = models.ForeignKey('Production')

    
class Production(models.Model):
    opens         = models.CharField(null=True, max_length=10)
    closes        = models.CharField(null=True, max_length=10)
    show_name     = models.CharField(max_length=80)
    theater       = models.ForeignKey('Theater')
    creation_time = models.DateTimeField(blank=True)
    update_time   = models.DateTimeField(null=True)
    
    
class Theater(models.Model):
    name          = models.CharField(max_length=60)
    admin         = models.ForeignKey(User, blank=True, related_name="theater_admin", null=True)
    address       = models.CharField(blank=True, max_length=20)
    city          = models.CharField(blank=True, max_length=20)
    state         = models.CharField(blank=True, max_length=20)
    zip_code      = models.CharField(blank=True, max_length=10)
    phone         = models.CharField(blank=True, max_length=10)
    update_time   = models.DateTimeField(blank=True, null=True)

    
