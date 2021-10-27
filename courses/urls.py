from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_course', views.add_course, name='add_course'),
    path('get_course_data/', views.get_course_data, name='get_course_data'),
]