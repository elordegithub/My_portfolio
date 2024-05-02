from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]