from rest_framework import serializers
from . import models
from users import models as user_models


class _UserTrainerSerializer(serializers.ModelSerializer):
    """
    Чтобы можно было посмотреть данные о тренере
    """
    class Meta:
        model = user_models.CustomUser
        fields = '__all__'


class FitnessTrainerSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Фитнес-тренер.
    """
    trainer = _UserTrainerSerializer(many=False, read_only=True)

    class Meta:
        model = models.FitnessTrainer
        fields = '__all__'


class HallSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Зал.
    """
    class Meta:
        model = models.Hall
        fields = '__all__'
