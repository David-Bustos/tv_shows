from django.db import models
# import re

# Create your models here.
class ShowManager(models.Manager):

    def basic_validator(self, postData):
        errors = {}

        if len(postData['title']) < 2:
            errors['title'] = "Title must have at least 2 characters"

        return errors

class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()