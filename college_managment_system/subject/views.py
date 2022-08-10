from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
import subject
from .models import Subject
# Create your views here.
def create_subject(request):
    new_subject = Subject(
        name='pre_math',
        code=60,
    )
    new_subject.save()
    return HttpResponse("""<p>Created</p>""")
def list_subject(request):
    subjects = []
    for subject in Subject.objects.all():
        subjects.append({
            'name': subject.name,
            'age': subject.age,
        })
    return HttpResponse(subjects)
def update_subject(request):
    try:
        subject = Subject.objects.get(id=request.GET['id'])
        if 'name' in request.GET:
            subject.name = request.GET['name']
        if 'code' in request.GET:
            subject.address = request.GET['address']
        
        subject.save()
        return HttpResponse('SUBJECTS Hase Been Update Succesfully!!')
    except:
        return HttpResponse('subject Not Found')
def delete_subject(request):
    try:
        subject = Subject.objects.get(id=request.GET['id'])
        subject.delete()
        return HttpResponse('Subjects Hase Been Deleted Succesfully!!')
    except:
        return HttpResponse('Subject Not Found')
def retrieve_subject(request: HttpRequest):
    try:
        suject = Subject.objects.get(id=request.GET['id'])
        return HttpResponse(f"""
            <p>name: {subject.name}</p>
            <p>age: {subject.code}</p>
            
        """)
    except:
        return HttpResponseNotFound('subject Not Found')