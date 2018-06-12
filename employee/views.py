# -*- coding: utf-8 -*-
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token
from rest_framework import generics

from .models import TypeOfWork, Employee
from .serializers import TypeOfWorkSerializer, EmployeeSerializer


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class TypeOfWorkList(generics.ListCreateAPIView):
    queryset = TypeOfWork.objects.all()
    serializer_class = TypeOfWorkSerializer


class TypeOfWorkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeOfWork.objects.all()
    serializer_class = TypeOfWorkSerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        """Returns Polls that were created today"""
        employees = Employee.objects.all()
        params = self.request.query_params
        if 'type_of_work' in params:
            employees = employees.filter(type_of_work=params.get('type_of_work'))
        return employees


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer