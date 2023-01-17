from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager, AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(UserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not extra_fields.get("phone_number"):
            raise ValueError(_("Please enter a phone number"))
        return super().create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        if not extra_fields.get("phone_number"):
            raise ValueError(_("Please enter a phone number"))
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(_("Username"), max_length=40, unique=True)
    email = models.EmailField(_("Email"), max_length=80, unique=True)
    phone_number = PhoneNumberField(
        _("Phone Number"), unique=True, null=False, blank=False
    )

    REQUIRED_FIELDS = ["username", "phone_number"]
    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = "用戶"
        verbose_name = "用戶"

    def __str__(self):
        return self.username
