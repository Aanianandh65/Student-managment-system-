from django.shortcuts import render
from .models import ITStudentProgress, CADDStudentSoftware

def it_students(request):

    name = request.GET.get('name')
    course = request.GET.get('course')
    branch = request.GET.get('branch')
    min_progress = request.GET.get('min_progress')
    max_progress = request.GET.get('max_progress')

    students = ITStudentProgress.objects.select_related(
        'student__branch',
        'student__department',
        'course'
    )

    if name:
        students = students.filter(student__name__icontains=name)

    if course:
        students = students.filter(course__name__icontains=course)

    if branch:
        students = students.filter(student__branch__name__iexact=branch)

    if min_progress:
        students = students.filter(completion_percentage__gte=min_progress)

    if max_progress:
        students = students.filter(completion_percentage__lte=max_progress)

    return render(request, 'it_students.html', {
        'students': students
    })

def cadd_students(request):

    name = request.GET.get('name')
    software = request.GET.get('software')
    status = request.GET.get('status')
    branch = request.GET.get('branch')

    students = CADDStudentSoftware.objects.select_related(
        'student__branch',
        'student__department',
        'software'
    )

    if name:
        students = students.filter(student__name__icontains=name)

    if software:
        students = students.filter(software__name__icontains=software)

    if status:
        students = students.filter(status=status)

    if branch:
        students = students.filter(student__branch__name__iexact=branch)

    return render(request, 'cadd_students.html', {
        'students': students
    })
def cadd_upcoming(request):

    name = request.GET.get('name')
    software = request.GET.get('software')
    branch = request.GET.get('branch')
    batch = request.GET.get('batch')

    students = CADDStudentSoftware.objects.select_related(
        'student__branch',
        'software'
    ).filter(status='upcoming')

    if name:
        students = students.filter(student__name__icontains=name)

    if software:
        students = students.filter(software__name__icontains=software)

    if branch:
        students = students.filter(student__branch__name__iexact=branch)

    if batch:
        students = students.filter(student__batch__icontains=batch)

    return render(request, 'cadd_upcoming.html', {
        'students': students
    })

