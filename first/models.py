from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class BlogTable(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(max_length=5000)
    foto=models.ImageField(upload_to='images/')
    public=models.BooleanField(default=False)
    today=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

