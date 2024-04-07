from typing import Protocol, OrderedDict
from . import models


class ScheduleReposInterface(Protocol):
    """
    Это слой репозиторий для того чтобы общаться с базой данных.
    Эта нужна чтобы была Чистая Архитектура (Clean Architecture)
    Здесь реализован интерфейс с помощью класса Protocol
    """
    @staticmethod
    def create_schedule(data: OrderedDict) -> models.Schedule: ...


class ScheduleReposV1:
    """
    Pеализация интерфейса
    """
    @staticmethod
    def create_schedule(data: OrderedDict) -> models.Schedule:

        return models.Schedule.objects.create(**data)
