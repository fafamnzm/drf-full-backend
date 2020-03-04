from django.db import models
from django.contrib.auth.models import AbstractUser #, User
#from django.contrib.auth import get_user_model

# Create your models here.


### for custom user use

class User(AbstractUser):
    phone_number = models.IntegerField(null=True)
    
    def __str__(self):
        return self.username

#User = get_user_model()

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
