from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    address = models.TextField()
    email=models.EmailField(max_length=50,unique=True)
    username=None
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    session_token = models.CharField(max_length=10,default="t")



class Blog(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=250,blank=True,null=True)
    description = models.CharField(max_length=500,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)