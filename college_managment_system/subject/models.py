import code
from django.db import models

class Subject (models.Model):
    name = models.CharField(max_length=200,primary_key=False,unique=False,null=False)
    code=models.IntegerField(null=False)
    

# Create your models here.
