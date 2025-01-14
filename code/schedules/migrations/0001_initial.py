# Generated by Django 5.0.3 on 2024-04-05 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fitness_trainers', '0003_hall_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='Время начала')),
                ('end_time', models.TimeField(verbose_name='Время окончания')),
                ('day_of_week', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9)),
                ('hall', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='fitness_trainers.hall')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schedules', to='fitness_trainers.fitnesstrainer')),
            ],
        ),
    ]
