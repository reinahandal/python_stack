from django.db import models
from datetime import datetime
import re

class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$")
        NAME_REGEX = re.compile('^[A-Za-z]{2,}$')

        # if len(postData['fname']) < 2 or not postData['fname'].isalpha():
        #     errors["fname"] = "First name should contain letters only and be at least 2 characters" 

        # if len(postData['lname']) < 2 or not postData['lname'].isalpha():
        #     errors["lname"] = "Last name should contain letters only and be at least 2 characters"

        if not NAME_REGEX.match(postData['fname']):
            errors["fname"] = "First name should contain letters only and be at least 2 characters"
        if not NAME_REGEX.match(postData['lname']):
            errors["lname"] = "Last name should contain letters only and be at least 2 characters" 
        
        if not postData['email']:
            errors["email"] = "Email is required"
        elif not EMAIL_REGEX.match(postData['email']): 
            errors['email'] = "Invalid email address"
        elif User.objects.filter(email=postData['email']):
            errors['email'] = "Email already exists"

        if not postData['birthday']:
            errors['birthday'] = "Date of birth is required"
        elif datetime.strptime(postData['birthday'],'%Y-%m-%d') > datetime.today():
                errors["birthday"] = "Date of birth should be in the past"

        if not PASSWORD_REGEX.match(postData['pw']):
            errors["password"] = "Password should be at least 8 characters, and contain at least one uppercase, one lowercase, one digit and one special character"
        if not postData['confirm_pw']:
            errors["confirm_password"] = "Please confirm password"
        elif postData['pw'] != postData['confirm_pw']:
            errors["password_match"] = "Passwords don't match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
