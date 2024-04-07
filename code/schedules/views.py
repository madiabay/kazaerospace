from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from . import permissions, serializers, services


class ScheduleViewSet(ViewSet):
    """
    Реализован handler.
    Реализован метод create_schedule чтобы создать модель 'Pасписание' и чтобы только 'Admin' мог создать.
    """
    schedule_services: services.ScheduleServicesInterface = services.ScheduleServicesV1()
    permission_classes = permissions.IsAdminOrReadOnly,

    @swagger_auto_schema(request_body=serializers.ScheduleSerializer)
    def create_schedule(self, request, *args, **kwargs):
        serializer = serializers.ScheduleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = self.schedule_services.create_schedule(data=serializer.validated_data)

        return Response(
            {'data': f'Schedule with id={data.id} is successfully created'},
            status=status.HTTP_201_CREATED
        )
