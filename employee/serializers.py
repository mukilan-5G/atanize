from rest_framework import serializers

from .models import TypeOfWork, Employee


class TypeOfWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfWork
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"