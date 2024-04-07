from rest_framework import serializers
from . import models


class ScheduleSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Schedule.
    """

    class Meta:
        model = models.Schedule
        fields = '__all__'
