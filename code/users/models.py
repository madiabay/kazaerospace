import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from . import choices


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    first_name = None
    last_name = None
    familia = models.CharField(_("Familia"), max_length=150, blank=True)
    imya = models.CharField(_("Imya"), max_length=150, blank=True)
    otchestvo = models.CharField(_("Otchestvo"), max_length=150, blank=True)

    email = models.EmailField(unique=True, verbose_name=_("Email"), )
    phone_number = PhoneNumberField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(
        choices=choices.SexType.choices,
        max_length=6,
    )
    user_role = models.CharField(
        choices=choices.UserRole.choices,
        max_length=7,
    )

    REQUIRED_FIELDS = ['email', 'phone_number', 'sex', 'user_role']
