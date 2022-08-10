from django.http import HttpResponse, HttpRequest, HttpResponseNotFound

from subject.models import Subject
from .models import Professor
# Create your views here.
def create_professor(request):

    sub=Subject.objects.get(pk=1)

    new_professor = Professor(
        name='bedo',
        address='oooo',
        age=70,
    )
    new_professor.save()
    return HttpResponse("""<p>Created</p>""")
def list_professor(request):
    
    professors = []
    for professor in Professor.objects.all():
        professors.append({
            'name': professor.name,
            'address': professor.address,
            'age': professor.age,
            'sub' :professor.sub,







        })
    return HttpResponse(professors)
def update_professor(request):
    try:
        professor = Professor.objects.get(id=request.GET['id'])
        if 'name' in request.GET:
            professor.name = request.GET['name']
        if 'address' in request.GET:
            professor.address = request.GET['address']
        if 'age' in request.GET:
            professor.age = request.GET['age']
        
        professor.save()
        return HttpResponse('professor Hase Been Update Succesfully!!')
    except:
        return HttpResponse('professor Not Found')
def delete_professor(request):
    try:
        professor = Professor.objects.get(id=request.GET['id'])
        professor.delete()
        return HttpResponse('professor Hase Been Deleted Succesfully!!')
    except:
        return HttpResponse('pofessor Not Found')
def retrieve_professor(request: HttpRequest):
    try:
        professor = Professor.objects.get(id=request.GET['id'])
        return HttpResponse(f"""
            <p>name: {professor.name}</p>
            <p>address: {professor.address}</p>
            <p>age: {professor.age}</p>
           
        """)
    except:
        return HttpResponseNotFound('Student Not Found')