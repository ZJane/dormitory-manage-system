from django.shortcuts import render
from dor.models import Student,DormitorySchedule,Dormitory
from django.db.models import Q

def search_stu(request):

    dorm_floor_number = request.POST.get('dorm_floor_number','')
    if(dorm_floor_number == '至诚'):
        dorm_floor_number = 'J'
    elif(dorm_floor_number == '弘毅'):
        dorm_floor_number = 'K'
    elif(dorm_floor_number == '思源'):
        dorm_floor_number = 'L'
    elif(dorm_floor_number == '知行'):
        dorm_floor_number = 'M'
    dorm_number = request.POST.get('dorm_number', '')
    student_name = request.POST.get('student_name', '')
    students = Student.objects.filter(Q(sname=student_name)|Q(dor_no=dorm_floor_number)|Q(room_no=dorm_number))
    for student in students:
        dorm_floor = Dormitory.objects.get(dor_no = student.dor_no)
        student.dor_no = dorm_floor.dor_name
    return render(request, 'admin/searchInfo.html',{"students":students,"i":1})

def sort_stu_info(request):
    students = Student.objects.filter(gender='男')
    students.order_by('sname')

def show_room_info(request):
    pass

