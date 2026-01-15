from django import forms
from students.models import Branch, Department
from courses.models import ITCourse, Software

# ---------- BRANCH ----------
class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if Branch.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("This branch already exists.")
        return name


# ---------- DEPARTMENT ----------
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if Department.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("This department already exists.")
        return name


# ---------- IT COURSE ----------
class ITCourseForm(forms.ModelForm):
    class Meta:
        model = ITCourse
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if ITCourse.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("This course already exists.")
        return name


# ---------- CADD SOFTWARE ----------
class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if Software.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("This software already exists.")
        return name
