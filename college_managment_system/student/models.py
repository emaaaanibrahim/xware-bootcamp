import email
from unicodedata import name
from django.db import models
from subject.models import Subject


class Student (models.Model):
    name = models.CharField(max_length=200,primary_key=False,unique=False,null=False)
    address= models.CharField(null=False,max_length=200)
    age=models.IntegerField(null=False)
    email=models.CharField(null=False, max_length=200)
    image=models.ImageField(null=True)
    ssn=models.CharField(null=False,max_length=200)

class Links (models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    email=models.EmailField(max_length=100)
    facebook=models.URLField(null=True)
    twitter=models.URLField(null=True)
    instagram=models.URLField(null=True)



class phones (models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    phone=models.CharField(null=False, max_length=200)
 


class Subject_enrollment (models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE )
    student=models.ForeignKey(Student,on_delete=models.CASCADE)




# Create your models here.
