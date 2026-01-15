from django.urls import path
from . import views

urlpatterns = [
    path('branch/<str:branch_name>/', views.branch_students, name='branch_students'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/all/', views.all_students, name='all_students'),
]

