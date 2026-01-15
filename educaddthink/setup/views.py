from django.shortcuts import render
from .forms import BranchForm, DepartmentForm, ITCourseForm, SoftwareForm

def setup_master(request):

    branch_form = BranchForm(prefix='branch')
    dept_form = DepartmentForm(prefix='dept')
    course_form = ITCourseForm(prefix='course')
    software_form = SoftwareForm(prefix='software')

    if request.method == 'POST':

        if 'branch-name' in request.POST:
            branch_form = BranchForm(request.POST, prefix='branch')
            if branch_form.is_valid():
                branch_form.save()

        elif 'dept-name' in request.POST:
            dept_form = DepartmentForm(request.POST, prefix='dept')
            if dept_form.is_valid():
                dept_form.save()

        elif 'course-name' in request.POST:
            course_form = ITCourseForm(request.POST, prefix='course')
            if course_form.is_valid():
                course_form.save()

        elif 'software-name' in request.POST:
            software_form = SoftwareForm(request.POST, prefix='software')
            if software_form.is_valid():
                software_form.save()

    return render(request, 'setup_master.html', {
        'branch_form': branch_form,
        'dept_form': dept_form,
        'course_form': course_form,
        'software_form': software_form
    })
