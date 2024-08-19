from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    # contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    desc=models.TextField(max_length=500)
    phonenumber=models.IntegerField()

    def __int__(self):
        return self.id


class NOTE(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user  = models.ForeignKey(User  , on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.id