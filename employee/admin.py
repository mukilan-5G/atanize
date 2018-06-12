# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import TypeOfWork, Employee

# Register your models here.
admin.site.register(TypeOfWork)
admin.site.register(Employee)
