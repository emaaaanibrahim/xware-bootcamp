from django.db import models
from subject.models import Subject


class Professor (models.Model):
    name = models.CharField(max_length=200,primary_key=False,unique=False,null=False)
    address= models.CharField(null=False,max_length=200)
    age=models.IntegerField(null=False)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE , null=True)

class Links (models.Model):
    professor=models.ForeignKey(Professor,on_delete=models.CASCADE)
    email=models.EmailField(max_length=100)
    facebook=models.URLField(null=True)
    



class Phones (models.Model):
    professor=models.ForeignKey(Professor,on_delete=models.CASCADE)
    phone=models.CharField(null=False, max_length=200)


# Create your models here.
