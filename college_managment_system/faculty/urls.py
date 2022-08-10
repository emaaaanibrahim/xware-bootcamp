from django.urls import path
from . import views

urlpatterns = [

    path('create/',views.create_faculty),
    path('list/',views.list_faculty),
    path('update/',views.update_faculty),
    path('delete/',views.delete_faculty),
    path('retrieve/',views.retrieve_faculty),






]