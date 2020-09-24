from django.urls import path
from . import  views

app_name = 'ruth'
urlpatterns = [
    path('', views.index, name = 'home' ),
    path('index/', views.index, name='index'),
    path('details/<int:person_id>/', views.details, name = 'details'),
    path('failed/', views.failed, name = 'failed'),
    path('home/', views.home, name = 'home'),
    path('file/', views.get_form, name = 'file'),
    path('calendar/', views.calendar, name = 'calendar'),
]