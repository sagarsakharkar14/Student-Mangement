from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('add-std/', views.std_add),
    path('delete-std/<int:roll>', views.delete_std),
    path('update-std/<int:roll>', views.update_std),
    path('do-update-std/<int:roll>', views.do_update_std),
]
