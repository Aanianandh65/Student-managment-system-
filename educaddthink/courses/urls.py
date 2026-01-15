from django.urls import path
from . import views

urlpatterns = [
    path('it/students/', views.it_students, name='it_students'),
    path('cadd/students/', views.cadd_students, name='cadd_students'),
    path('cadd/upcoming/', views.cadd_upcoming, name='cadd_upcoming'),

]
