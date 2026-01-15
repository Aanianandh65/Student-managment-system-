from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
    path('', include('courses.urls')),
    path('', include('setup.urls')),
    path('', include('dashboard.urls')),  

]
