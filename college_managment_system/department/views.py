from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from .models import Department
# Create your views here.
def create_department(request):
    new_department = Department(
        name='dsfsdf',
        
    )
    new_department.save()
    return HttpResponse("""<p>Created</p>""")
def list_department(request):
    departments = []
    for department in Department.objects.all():
        departments.append({
            'name': department.name,
           
        })
    return HttpResponse(departments)
def update_department(request):
    try:
        department = Department.objects.get(id=request.GET['id'])
        if 'name' in request.GET:
            department.name = request.GET['name']
       
        department.save()
        return HttpResponse('department Hase Been Update Succesfully!!')
    except:
        return HttpResponse('department Not Found')
def delete_department(request):
    try:
        department = Department.objects.get(id=request.GET['id'])
        department.delete()
        return HttpResponse('department Hase Been Deleted Succesfully!!')
    except:
        return HttpResponse('departments Not Found')
def retrieve_department(request: HttpRequest):
    try:
        department = Department.objects.get(id=request.GET['id'])
        return HttpResponse(f"""
            <p>name: {department.name}</p>
            
     
        """)
    except:
        return HttpResponseNotFound('department Not Found')
