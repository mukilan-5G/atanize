# -*- coding: utf-8 -*-
from rest_framework import generics, status
from rest_framework.response import Response

from employee.models import Employee
from .models import Attendance
from .serializers import AttendanceSerializer


class AttendanceList(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def get(self, request, date, type_of_work, format=None):
        attendance_list = []
        employees = Employee.objects.filter(is_active=True)
        if type_of_work != '0':
            employees = employees.filter(type_of_work=type_of_work)
        for employee in employees:
            attendance, created = Attendance.objects.get_or_create(date=date, employee=employee)
            attendance_list.append(attendance)
        serializer = self.serializer_class(attendance_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, date, type_of_work, **kwargs):
        for data in request.data:
            employee = data.get('employee')
            attendance = Attendance.objects.get(date=data.get('date'), employee__id=employee.get("id"))
            attendance.is_present = data.get('is_present')
            attendance.advance = data.get('advance')
            attendance.save()
        return Response(request.data, status=status.HTTP_200_OK)



class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer