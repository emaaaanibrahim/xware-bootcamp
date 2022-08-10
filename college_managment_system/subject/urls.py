from django.urls import path
from . import views

urlpatterns = [

    path('create/',views.create_subject),
    path('list/',views.list_subject),
    path('update/',views.update_subject),
    path('delete/',views.delete_subject),
    path('retrieve/',views.retrieve_subject),






]