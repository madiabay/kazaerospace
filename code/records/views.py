from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import models, serializers


class RecordViewSet(ModelViewSet):
    """
    API эндпоинты для CRUD Record.
    """
    queryset = models.Record.objects.all()
    serializer_class = serializers.RecordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        models.Record.objects.create(
            identification_number=models.Record.generate_identification_number(),
            **serializer.validated_data
        )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
