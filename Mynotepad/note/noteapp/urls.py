"""
URL configuration for note project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path 
from noteapp import views
from noteapp.views import add_note , delete_note

urlpatterns = [
    path('',views.index,name="index"),
    path('note',views.note,name="note"),
    path('contact',views.contact,name="contact"),
    path('home',views.home,name="home"),
    path('add-note/' , add_note ), 
    path('delete-note/<int:id>' , delete_note ), 
]
