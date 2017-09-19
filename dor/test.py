from __future__ import unicode_literals
import os,django
# -*- coding: utf-8 -*-
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dor_system.settings")
django.setup()
from dor.models import  DorChange,Student
from dor.DTO.StuDorLog import StuDorLogModel

change_log_data = DorChange.objects.filter(sno=201401003)
stu_data = Student.objects.filter(sno=2014101003)
dor_change_list = [[]]
for i in range(0, len(change_log_data)):
    test = StuDorLogModel()
    test.sno = change_log_data[i].sno
    test.sname = change_log_data[i].sname
    test.old_room_no = change_log_data[i].old_room_no
    test.new_room_no = change_log_data[i].new_room_no
    test.apply_time = change_log_data[i].apply_time
    test.reason = change_log_data[i].reason
    test.apply_status = change_log_data[i].app_status
    test.email = stu_data.email
    test.stu_phone = stu_data.phone
    test.college = stu_data.college
    test.major = stu_data.major
    dor_change_list.append(test)

print(len(change_log_data))