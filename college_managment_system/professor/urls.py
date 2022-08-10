from django.urls import path
from . import views

urlpatterns = [

    path('create/',views.create_professor),
    path('list/',views.list_professor),
    path('update/',views.update_professor),
    path('delete/',views.delete_professor),
    path('retrieve/',views.retrieve_professor),






]