from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blogs(models.Model):
    Image=models.ImageField(null=True,blank=True)
    title=models.CharField(max_length=200,null=False, blank=False)
    description=models.TextField(null=True)
    date=models.DateField(auto_now_add=True,null=True)
    likes=models.ManyToManyField(User, related_name='likes', blank=True) 

def total_likes(self):
    return self.likes.count()