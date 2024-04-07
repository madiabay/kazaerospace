from rest_framework import serializers
from . import models


class RecordSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Запись.
    """

    class Meta:
        model = models.Record
        fields = (
            'client',
            'schedule',
        )
