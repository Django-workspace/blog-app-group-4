
from django.db import models
import uuid
# Create your models here.
class Blogs(models.Model):
    
    Image=models.ImageField(null=True,blank=True)
    title=models.CharField(max_length=200,null=False, blank=False)
    description=models.TextField(null=True)
    date=models.DateField(auto_now_add=True,null=True)
    likes=models.IntegerField(default=0)
    def __str__(self):
        return str(self.title)
 