from django.urls import path

from . import views

app_name = 'appweb'

urlpatterns = [
    path('', views.index, name='index'),
    
]