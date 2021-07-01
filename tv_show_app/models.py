from django.db import models
from datetime import datetime
# import re

# Create your models here.
class ShowManager(models.Manager):

    def basic_validator(self, postData):
        errors = {}
        today=datetime.now().strftime('%Y-%m-%d')


        if Show.objects.filter(title=postData['title']):
            errors['title'] = "This show already exists"
        if len(postData['title']) < 2:
            errors['title'] = "Title must have at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network must have at least 3 characters"
        if postData['date'] == '':
            errors['date'] = "Date is required"
        if postData['date'] > today:
            errors['date'] = "Date is not valid"
        if len(postData['desc']) > 0 and len(postData['desc'])< 10:
            errors['desc'] = "Description must have at least 10 characters"

        return errors

class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()