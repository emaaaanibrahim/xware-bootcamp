from django.urls import path
from . import views

urlpatterns = [

    path('create/',views.create_department),
    path('list/',views.list_department),
    path('update/',views.update_department),
    path('delete/',views.delete_department),
    path('retrieve/',views.retrieve_department),






]