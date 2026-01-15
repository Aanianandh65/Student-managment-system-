from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name   # ✅ THIS FIXES DROPDOWN


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name   # ✅ THIS FIXES DROPDOWN


class Student(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    batch = models.CharField(max_length=50)
    batch_start = models.DateField()
    batch_end = models.DateField()

    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.name
