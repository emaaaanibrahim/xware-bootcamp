from pyexpat import model
from django import forms
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



class create_user(forms.Form):
        user_name=forms.CharField(max_length=200,required=True,min_length=1)
        user_email=forms.EmailField(max_length=200,required=True,min_length=1)
        password=forms.CharField(max_length=50,min_length=5,required=True)
   
   
class create_todo (forms.Form):   
   
    task_user=forms.IntegerField()
    task_name= forms.CharField(max_length=90)
    task_description= forms.CharField(max_length=200)
    task_created_date= forms.DateTimeField()
    task_finished_date= forms.CharField(max_length=40)
    task_notes= forms.CharField(max_length=90)


class Create_Users_Models_Form(forms.ModelForm):
   class Meta :
       model = User 
       fields= ['username','email','password']
   
   def clean(self):
        cleaned_data=super().clean()
        cleaned_data['password']= make_password(cleaned_data['password'])
        return cleaned_data