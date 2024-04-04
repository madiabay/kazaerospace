from django.db import models


class UserRole(models.TextChoices):
    Client = 'Client'
    Trainer = 'Trainer'
    Admin = 'Admin'


class SexType(models.TextChoices):
    Male = 'Male'
    Female = 'Female'
