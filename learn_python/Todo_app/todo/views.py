from asyncio import Task
from distutils.command import clean
from distutils.log import error
from email.mime import image
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest,HttpResponseRedirect,HttpResponseForbidden
# from .models import User
from .forms import create_user as create_user_form
from .forms import create_todo as create_todo_form
from django.views.decorators.http import require_http_methods , require_GET , require_POST
from django.views import View
from django.contrib.auth.models import User
from .forms import Create_Users_Models_Form
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def create_todo(request):
    if request.method=='GET':
        return render(request,'todo/create_todo.html')
    else:
        forms=create_todo_form(request.POST)
        if forms.is_valid():
            task = Task(
            user=forms.cleaned_data['user_name'],
            name=forms.cleaned_data['task_name'],
            description=forms.cleaned_data['task_description'],
            created_date=forms.cleaned_data['task_created_date'],
            finished_date=forms.cleaned_data['task_Finished_date'],
            task_notes=forms.cleaned_data['task_notes'],
             )
           
            task.save()
            
            return render(request,'todo/create_todo.html', {
                'result':'valid',
                'validation_task_user':task.user,
                'validation_task_name':task.name,
                'validation_task_description':task.description,  
                'validation_task_created_date':task.created_date,                
                'validation_task_finished_date':task.finished_date,                
                'validation_task_task_notes':task.task_notes,                
                               

            
            })

        else:
            print(forms.errors)
            return render(request,'todo/create_todo.html',{'result':'not valid', 'errors':forms.errors,})
    
            
    

def update_todo(request):
    
    return HttpResponse('updated')
  
def delete_todo(request):

    return HttpResponse('deleted')
    
def retrieve_todo(request: HttpRequest):
    
    return HttpResponse('retrieved')

def check_todo(request):
    return HttpResponse('check')




class Createuserview(View):
    def get (self, request):
        form=Create_Users_Models_Form()
        return render(request,'todo/create_user.html',{
            'form':form 
        })
        # else :
        #         print('fdsfdsfds')
        #         return HttpResponseRedirect('http://127.0.0.1:8000/login/')


    def post (self,request) :

            form=Create_Users_Models_Form(request.POST)
            if form.is_valid():
                user=form.save()
                # user = User.objects.create_user(
                # username=form.cleaned_data['user_name'],
                # email=form.cleaned_data['user_email'],
                # password=form.cleaned_data['password']
                # )
                
                # return HttpResponse('created')
                return render(request,'todo/create_user.html', {
                    'result':'valid',
                    # 'validation_user_name':user.username,
                    # 'validation_user_email':user.email,
                    # 'password':user.password,
                    'user':user,
                    'form':form
                
                
                })

            else:
                return render(request,'todo/create_user.html',{'result':'not valid',
                    'error':form.errors ,   
                    'form' :form            
                }
                
                )
        

class Listuserview(View) :

    def get(self,request : HttpRequest):           
        if not request.user.is_authenticated :
            return HttpResponseForbidden('you are not allowed listing users')
        first_time=None
        if 'horry' in request.COOKIES :
            first_time=False
        else:
            first_time=True

        users=User.objects.all()
        user_list =[]
        for user in users:
            user_list.append(
                {
                    'user_name' : user.username ,
                    'user_email' : user.email,  
                    # 'password' : user.password,
                }

            )
        response= render(request,'todo/list_user.html', {
            
                'users':user_list,
                'first_time':first_time,
        
        })
        response.set_cookie('horry','hello')
        print(first_time)
        return response

def update_user(request):

    try:
        user = User.objects.get(id=request.GET['id'])
        if 'username' in request.GET:
            user.username = request.GET['username']
        if 'email' in request.GET:
            user.email = request.GET['email']
        if 'password' in request.GET:
            user.password = request.GET['password']
        
        user.save()
        return render(request,'todo/update_user.html',{
            'result':'user updated'

        })
    except:
        return render(request,'todo/update_user.html',{
            'result':'user not found '

        })
    # return HttpResponse('updated')
  
class Deleteuserview (View):

    def get (self,request):
        try :

            user =User.objects.get(id=request.GET['id'])
            user.delete()
            return render(request,'todo/delete_user.html', {
                'result' : 'user deleted' ,})    
        except Exception as e:
            print(e)
            return render(request,'todo/delete_user.html', {
                'result' : 'user not found' ,})   
class Retrieveuserview (View):        
    def get(self,request):
        if not request.user.is_authenticated :
            return HttpResponseForbidden('you are not allowed listing users')
        try :
            user =User.objects.get(id=request.GET['id'])
            return render(request,'todo/retrieve_user.html', {
                'is_user_found' : True,
                'user':user,
            
            })
        except Exception as e:
            print(e)
            return render(request,'todo/retrieve_user.html', {
                'is_user_found' : False ,})


class Loginview(View):
# request.session['user_name']
# request.session['password']
   
   
    def post (self,request):
        
        user = authenticate(
        username=request.POST['user_name'],
        password=request.POST['password'],
        )
        if user is not None :
            login(request,user)
            return render (request,'todo/login.html',{'logged':True})
        
        return render (request,'todo/login.html',{'error':'username or password not valid'})

    def get (self,request):
        return render (request,'todo/login.html')

class Logoutview(View):

    def get (self,request):
        # del request.session['user_name']
        # del request.session['password']
        logout(request)
        return HttpResponse('DELETED')


       

    




    # return HttpResponse('retrieved')