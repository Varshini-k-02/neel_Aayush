from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    is_user = models.BooleanField('Is user',default=False)
    is_employee = models.BooleanField('Is employee',default=False)
    is_admin = models.BooleanField('Is admin',default=False)
    
    # def __str__(self):
    #     return self.name

class Complaint(models.Model):
    ticketid = models.CharField(primary_key=True,max_length=20)
    complainant = models.ForeignKey(User, on_delete = models.SET_NULL,null=True)
    type = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    docLink = models.CharField(max_length=1000)
    handler = models.CharField(max_length=30)
    status = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ticketid

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    ticketid = models.ForeignKey(Complaint,on_delete=models.CASCADE)
    body = models.TextField(max_length=400,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']


class ProgressBar(models.Model):
    commentee = models.ForeignKey(User, on_delete=models.CASCADE)
    tid = models.ForeignKey(Complaint,on_delete=models.CASCADE)
    bar = models.TextField(max_length=3,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)