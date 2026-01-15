from django.shortcuts import render
from .models import Student
from django.contrib import messages
from courses.models import ITStudentProgress, CADDStudentSoftware
from django.shortcuts import render, redirect
from .forms import StudentForm, ITStudentForm, CADDStudentSoftwareForm
from courses.models import Software
from django.shortcuts import get_object_or_404
from courses.models import ITStudentProgress, CADDStudentSoftware
from .forms import StudentForm, ITStudentForm

def branch_students(request, branch_name):

    name = request.GET.get('name')
    batch = request.GET.get('batch')

    students = Student.objects.filter(
        branch__name__iexact=branch_name
    ).select_related('department', 'branch')

    if name:
        students = students.filter(name__icontains=name)

    if batch:
        students = students.filter(batch__icontains=batch)

    rows = []

    for student in students:

        course_or_software = "-"
        status = "-"

        # IT STUDENT LOGIC
        if student.department.name.upper() == "IT":
            it = ITStudentProgress.objects.filter(student=student).first()
            if it:
                course_or_software = it.course.name
                status = f"{it.completion_percentage}% Completed"

        # CADD STUDENT LOGIC
        elif student.department.name.upper() == "CADD":
            ongoing = CADDStudentSoftware.objects.filter(
                student=student,
                status='ongoing'
            ).first()

            if ongoing:
                course_or_software = ongoing.software.name
                status = "Ongoing"
            else:
                upcoming = CADDStudentSoftware.objects.filter(
                    student=student,
                    status='upcoming'
                ).first()
                if upcoming:
                    course_or_software = upcoming.software.name
                    status = "Upcoming"

        rows.append({
            'id': student.id,
            'name': student.name,
            'phone': student.phone,
            'department': student.department.name,
            'course_or_software': course_or_software,
            'status': status,
            'batch': student.batch,
        })

    return render(request, 'branch_students.html', {
        'branch': branch_name.upper(),
        'rows': rows
    })


def add_student(request):

    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        it_form = ITStudentForm(request.POST)
        software_ids = request.POST.getlist('software')
        statuses = request.POST.getlist('status')

        if student_form.is_valid():
            student = student_form.save()

            # IT STUDENT
            if student.department.name.lower() == 'it':
                if it_form.is_valid():
                    it = it_form.save(commit=False)
                    it.student = student
                    it.save()

            # CADD STUDENT
            if student.department.name.lower() == 'cadd':
                for software_id, status in zip(software_ids, statuses):
                    CADDStudentSoftware.objects.create(
                        student=student,
                        software_id=software_id,
                        status=status
                    )

            # ✅ SUCCESS MESSAGE
            messages.success(request, "Student saved successfully ✅")

            # 🔁 REDIRECT TO FRESH FORM
            return redirect('add_student')

    else:
        student_form = StudentForm()
        it_form = ITStudentForm()

    softwares = Software.objects.all()

    return render(request, 'add_student.html', {
        'student_form': student_form,
        'it_form': it_form,
        'softwares': softwares
    })



def edit_student(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    it_progress = None
    cadd_softwares = None

    if student.department.name.lower() == 'it':
        it_progress = ITStudentProgress.objects.filter(student=student).first()

    if student.department.name.lower() == 'cadd':
        cadd_softwares = CADDStudentSoftware.objects.filter(student=student)

    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=student)
        it_form = ITStudentForm(request.POST, instance=it_progress)

        if student_form.is_valid():
            student_form.save()

            if student.department.name.lower() == 'it' and it_form.is_valid():
                it = it_form.save(commit=False)
                it.student = student
                it.save()

            if student.department.name.lower() == 'cadd':
                for cs in cadd_softwares:
                    new_status = request.POST.get(f'status_{cs.id}')
                    cs.status = new_status
                    cs.save()

            return redirect('branch_students', branch_name=student.branch.name)

    else:
        student_form = StudentForm(instance=student)
        it_form = ITStudentForm(instance=it_progress)

    context = {
        'student': student,
        'student_form': student_form,
        'it_form': it_form,
        'cadd_softwares': cadd_softwares
    }

    return render(request, 'edit_student.html', context) 

def all_students(request):

    name = request.GET.get('name')
    batch = request.GET.get('batch')
    department = request.GET.get('department')

    students = Student.objects.select_related(
        'branch', 'department'
    )

    if name:
        students = students.filter(name__icontains=name)

    if batch:
        students = students.filter(batch__icontains=batch)

    if department:
        students = students.filter(department__name__iexact=department)

    return render(request, 'all_students.html', {
        'students': students
    })