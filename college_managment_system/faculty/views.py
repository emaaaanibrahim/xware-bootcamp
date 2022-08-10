from django.http import HttpResponse, HttpRequest, HttpResponseNotFound

import faculty
from .models import Faculty
# Create your views here.
def create_faculty(request):
    new_faculty = Faculty(
        name='dsfsdf',
        address='sfsdfdsf',
       
    )
    new_faculty.save()
    return HttpResponse("""<p>Created</p>""")
def list_faculty(request):
    faculties = []
    for faculty in Faculty.objects.all():
        faculties.append({
            'name': faculty.name,
            'address': faculty.address,
            
        })
    return HttpResponse(faculties)
def update_faculty(request):
    try:
        faculty = Faculty.objects.get(id=request.GET['id'])
        if 'name' in request.GET:
            faculty.name = request.GET['name']
        if 'address' in request.GET:
            faculty.address = request.GET['address']
        
        faculty.save()
        return HttpResponse('faculty Hase Been Update Succesfully!!')
    except:
        return HttpResponse('faculty Not Found')
def delete_faculty(request):
    try:
        faculty = Faculty.objects.get(id=request.GET['id'])
        faculty.delete()
        return HttpResponse('faculty Hase Been Deleted Succesfully!!')
    except:
        return HttpResponse('faculty Not Found')
def retrieve_faculty(request: HttpRequest):
    try:
        faculty = Faculty.objects.get(id=request.GET['id'])
        return HttpResponse(f"""
            <p>name: {faculty.name}</p>
            <p>address: {faculty.address}</p>
            
        """)
    except:
        return HttpResponseNotFound('faculty Not Found')
