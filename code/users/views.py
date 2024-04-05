from rest_framework.viewsets import ModelViewSet
from . import models, serializers


class UserViewSet(ModelViewSet):
    """
    API эндпоинты для CRUD CustomUser.
    """
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
