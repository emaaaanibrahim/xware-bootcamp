from django.db import models

from professor.models import Professor


class Department (models.Model):
    name = models.CharField(max_length=200,primary_key=False,unique=False,null=False)
    professor=models.ForeignKey(Professor,on_delete=models.CASCADE ,null=True)


    



# Create your models here.
