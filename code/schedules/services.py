from typing import Protocol, OrderedDict
from . import repositories, models


class ScheduleServicesInterface(Protocol):
    """
    Это слой предназначен чтобы могли здесь писать бизнес логики.
    Эта нужна чтобы была Чистая Архитектура (Clean Architecture)
    Здесь реализован интерфейс с помощью класса Protocol
    """

    def create_schedule(self, data: OrderedDict) -> models.Schedule: ...


class ScheduleServicesV1:
    """
    Pеализация интерфейса
    """
    schedule_repository: repositories.ScheduleReposInterface = repositories.ScheduleReposV1()

    def create_schedule(self, data: OrderedDict) -> models.Schedule:
        return self.schedule_repository.create_schedule(data=data)
