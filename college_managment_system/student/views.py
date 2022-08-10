# from student.models import Student
# # Create your views here.

# def create_student (request ) :

#     return HttpResponse ("HIIIIIIIIII")
# def list_student (request ) :
#     pass
# def update_student (request ) :
#     pass
# def delete_student (request ) :
#     pass
# def retrieve_student (request ) :
#     pass


from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from .models import Student
# Create your views here.
def create_student(request):
    new_student = Student(
        name='dsfsdf',
        address='sfsdfdsf',
        age=60,
        ssn='1234546'
    )
    new_student.save()
    return HttpResponse("""<p>Created</p>""")
def list_student(request):
    students = []
    for student in Student.objects.all():
        students.append({
            'name': student.name,
            'address': student.address,
            'age': student.age,
            'ssn': student.ssn
        })
    return HttpResponse(students)
def update_student(request):
    try:
        student = Student.objects.get(id=request.GET['id'])
        if 'name' in request.GET:
            student.name = request.GET['name']
        if 'address' in request.GET:
            student.address = request.GET['address']
        if 'age' in request.GET:
            student.age = request.GET['age']
        if 'ssn' in request.GET:
            student.ssn = request.GET['ssn']
        student.save()
        return HttpResponse('Student Hase Been Update Succesfully!!')
    except:
        return HttpResponse('Student Not Found')
def delete_student(request):
    try:
        student = Student.objects.get(id=request.GET['id'])
        student.delete()
        return HttpResponse('Student Hase Been Deleted Succesfully!!')
    except:
        return HttpResponse('Student Not Found')
def retrieve_student(request: HttpRequest):
    try:
        student = Student.objects.get(id=request.GET['id'])
        return HttpResponse(f"""
            <p>name: {student.name}</p>
            <p>address: {student.address}</p>
            <p>age: {student.age}</p>
            <p>ssn: {student.ssn}</p>
        """)
    except:
        return HttpResponseNotFound('Student Not Found')