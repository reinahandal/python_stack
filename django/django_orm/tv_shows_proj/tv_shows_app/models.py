from django.db import models
from time import gmtime, strftime, localtime
from datetime import datetime
class ShowManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network name should be at least 3 characters"
        if not postData['release_date']:
            errors["release_date"] = "Release Date is required"
        if postData['desc']:
            if len(postData['desc']) < 10:
                errors["desc"] = "Description should be at least 10 characters"
        if datetime.strptime(postData['release_date'],'%Y-%m-%d') > datetime.today():
            errors["release_date"] = "Release date should be in the past"
        return errors

# validator that makes sure the title doesnt already exist in our DB, only for CREATE method 
    def title_validator(self,postData):
        title_errors = {}
        if Show.objects.filter(title=postData['title']):
            title_errors["title_exists"] = "This title already exists"
        return title_errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()


