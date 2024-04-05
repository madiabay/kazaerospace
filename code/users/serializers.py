from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели CustomUser.
    """
    class Meta:
        model = models.CustomUser
        fields = '__all__'
