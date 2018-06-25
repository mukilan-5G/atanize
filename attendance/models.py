# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from employee.models import Employee

# Create your models here.
class Attendance(models.Model):
    date = models.DateField(auto_now=False)
    employee = models.ForeignKey(Employee)
    is_present = models.BooleanField(default=False)
    advance = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        db_table = "Attendance"
        unique_together = ('date', 'employee', )