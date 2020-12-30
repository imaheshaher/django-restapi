from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class CustomeUser(AbstractUser):
    
    email = models.EmailField(max_length=50,unique=True)
    first_name=models.CharField(max_length=200,blank=True)
    last_name=models.CharField(max_length=200,blank=True)
    address = models.TextField()
    username=None
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    def __str__(self):
        return str(self.email)


class Student(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.PositiveIntegerField()
    city=models.CharField(max_length=50)