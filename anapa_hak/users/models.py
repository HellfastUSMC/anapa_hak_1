from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)

class UserRole:
    """Кастомные пользовательские роли."""

    ADMIN = 'admin'
    SUPERVISOR = 'supervisor'
    PARENT = 'parent'
    KID = 'kid'


class CustomUserManager(UserManager):
    """Кастомный менеджер пользователей."""

    def create_superuser(
        self,
        username,
        email=None,
        password=None,
        role=UserRole.ADMIN,
        **kwargs,
    ):
        """Создание суперпользователя."""
        return super().create_superuser(
            username=username,
            email=email,
            password=password,
            role=role,
            **kwargs,
        )


class User(AbstractUser):
    """Кастомная модель пользователя."""

    ROLES = [
        (UserRole.SUPERVISOR, 'Вожатый'),
        (UserRole.PARENT, 'Родитель'),
        (UserRole.ADMIN, 'Администратор'),
        (UserRole.KID, 'Ребенок'),
    ]

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN

    @property
    def is_supervisor(self):
        return self.role == UserRole.SUPERVISOR

    @property
    def is_parent(self):
        return self.role == UserRole.PARENT

    objects = CustomUserManager()
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        max_length=254
    )
    bio = models.TextField(null=True, blank=True)
    role = models.CharField(
        max_length=10,
        choices=ROLES,
        default=UserRole.KID
    )

    class Meta:
        ordering = ['-id']


class Shift(models.Model):

    SEASONS = [
        'Лето',
        'Осень',
        'Зима',
        'Весна'
    ]

    number = models.IntegerField(
        'Номер смены',
        validators=[MinValueValidator(0), MaxValueValidator(999)]
    )
    year = models.IntegerField(
        'Год смены',
        validators=[MinValueValidator(2022), MaxValueValidator(2100)]
    )
    season = models.TextChoices('Сезон', choices=SEASONS)
    