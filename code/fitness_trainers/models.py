import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from users import choices as user_choices


class FitnessTrainer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    trainer = models.OneToOneField(
        to=get_user_model(),
        on_delete=models.PROTECT,
        related_name='fitness_trainer',
        limit_choices_to={'user_role': user_choices.UserRole.Trainer}  # to make sure the Trainer
    )


class Hall(models.Model):  # Зал
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    max_capacity_people = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(1), MaxValueValidator(32767)),
    )  # Maximum capacity of people
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='hall_photos/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
