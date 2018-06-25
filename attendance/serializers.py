from rest_framework import serializers

from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        depth = 1
        model = Attendance
        fields = "__all__"