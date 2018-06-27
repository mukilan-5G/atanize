# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TypeOfWork(models.Model):
    type = models.CharField(max_length=60)
    base_salary = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User)

    class Meta:
        db_table = "TypeOfWork"


class Employee(models.Model):
    name = models.CharField(max_length=60)
    phone_no = models.CharField(max_length=60, unique=True)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User)
    type_of_work = models.ForeignKey(TypeOfWork)

    class Meta:
        db_table = "Employee"
