# Django Imports
from django import urls
from django.urls import path, include

# Standard Package Imports

# Project Imports
from . import views


# Third Party Imports


app_name = 'main_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('members/<name>', views.members, name='members'),
    path('viewMembers', views.viewMembers, name='viewMembers'),
    #path('get_quote/', views.get_quote, name='get_quote'),
    # path('<int:year>/', views.diary),
    # path('<int:year>/<str:name>/', views.diary),
]