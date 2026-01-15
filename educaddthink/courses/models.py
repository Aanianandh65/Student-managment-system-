from django.db import models
from students.models import Student 

# IT models

class ITCourse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class ITStudentProgress(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(ITCourse, on_delete=models.PROTECT)
    completion_percentage = models.IntegerField()
    
    def __str__(self):
        return f"{self.student.name}"

# Cadd models

class Software(models.Model):
     name = models.CharField(max_length=100, unique=True)

class CADDStudentSoftware(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    software = models.ForeignKey(Software, on_delete=models.PROTECT)
    status = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name