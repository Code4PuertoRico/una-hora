import uuid

import pytz
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

TIMEZONE_CHOICES = [(tz, tz.split("/")[-1]) for tz in pytz.common_timezones_set]


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(verbose_name=_("email address"), unique=True)
    is_staff = models.BooleanField(
        verbose_name=_("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(
        verbose_name=_("date joined"), default=timezone.now
    )

    # profile fields
    full_name = models.CharField(
        blank=True, max_length=255, verbose_name=_("user's full name")
    )
    bio = models.TextField(blank=True, verbose_name=_("user's bio"))
    meeting_day = models.PositiveSmallIntegerField(
        null=True, verbose_name=_("day of week available for meetings")
    )
    meeting_time = models.TimeField(
        null=True, blank=True, verbose_name=_("time available for meetings")
    )
    meeting_method = models.TextField(
        blank=True, verbose_name=_("user's preferred meeting method with instructions")
    )
    timezone = models.CharField(
        max_length=255,
        verbose_name=_("user's timezone"),
        default="America/Puerto_Rico",
        choices=TIMEZONE_CHOICES,
    )
    tags = TaggableManager(
        blank=True,
    )

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def serialize(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "bio": self.bio,
        }

    def __str__(self):
        return self.email

    class Meta:
        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["-date_joined"]),
        ]
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
