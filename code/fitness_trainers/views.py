from rest_framework.viewsets import ModelViewSet
from . import models, serializers


class FitnessTrainerViewSet(ModelViewSet):
    """
    API эндпоинты для CRUD FitnessTrainer.
    """
    queryset = models.FitnessTrainer.objects.all()
    serializer_class = serializers.FitnessTrainerSerializer


class HallViewSet(ModelViewSet):
    """
    API эндпоинты для CRUD Hall.
    """
    queryset = models.Hall.objects.all()
    serializer_class = serializers.HallSerializer
