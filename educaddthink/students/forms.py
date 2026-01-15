
from courses.models import ITStudentProgress, CADDStudentSoftware, ITCourse, Software
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    batch_start = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    batch_end = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Student
        fields = [
            'name',
            'phone',
            'branch',
            'department',
            'batch',
            'batch_start',
            'batch_end',
            'remarks'
        ]


class ITStudentForm(forms.ModelForm):
    class Meta:
        model = ITStudentProgress
        fields = ['course', 'completion_percentage']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].required = False
        self.fields['completion_percentage'].required = False


class CADDStudentSoftwareForm(forms.ModelForm):
    class Meta:
        model = CADDStudentSoftware
        fields = ['software', 'status']
