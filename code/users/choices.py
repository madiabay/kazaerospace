from django.db import models


class UserRole(models.TextChoices):
    Client = 'Client'
    Coach = 'Coach'
    Admin = 'Admin'


class SexType(models.TextChoices):
    Male = 'Male'
    Female = 'Female'
