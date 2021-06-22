from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)