from django.db import models
from . import choices


class Schedule(models.Model):
    trainer = models.ForeignKey(
        to='fitness_trainers.FitnessTrainer',
        on_delete=models.PROTECT,
        related_name='schedules',
    )
    hall = models.ForeignKey(
        to='fitness_trainers.Hall',
        on_delete=models.CASCADE,
        related_name='schedules',
        limit_choices_to={'is_active': True},
    )
    start_time = models.TimeField(verbose_name='Время начала')
    end_time = models.TimeField(verbose_name='Время окончания')
    day_of_week = models.CharField(
        choices=choices.DayOfWeek.choices,
        max_length=9,
    )
