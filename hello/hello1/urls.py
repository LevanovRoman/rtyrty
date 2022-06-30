from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('news/', news, name='news'),
    path('managment/', managment, name='managment'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('branches/', branches, name='all_branches'),
    path('branches/<str:country_name>', branches, name='branches')

]

