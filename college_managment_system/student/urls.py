from django.urls import path
from . import views

urlpatterns = [

    path('create/',views.create_student),
    path('list/',views.list_student),
    path('update/',views.update_student),
    path('delete/',views.delete_student),
    path('retrieve/',views.retrieve_student),






]