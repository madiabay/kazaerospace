import random
import uuid

from django.db import models
from django.contrib.auth import get_user_model

from users import choices as user_choices


class Record(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    identification_number = models.CharField(max_length=10, unique=True, db_index=True)
    client = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT,
        related_name='records',
        limit_choices_to={'user_role': user_choices.UserRole.Client}
    )
    schedule = models.ForeignKey(
        to='schedules.Schedule',
        on_delete=models.PROTECT,
        related_name='records',
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def generate_identification_number(cls):
        identification_number = ''.join(random.choices('0123456789', k=10))

        if cls.objects.filter(identification_number=identification_number).exists():
            return cls.generate_identification_number()
        return identification_number
