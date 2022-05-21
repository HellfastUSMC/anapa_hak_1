# from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import (MaxValueValidator, MinValueValidator)
user = get_user_model()

# class UserRole:
#     """Кастомные пользовательские роли."""

#     ADMIN = 'admin'
#     SUPERVISOR = 'supervisor'
#     PARENT = 'parent'
#     KID = 'kid'


# class CustomUserManager(UserManager):
#     """Кастомный менеджер пользователей."""

#     def create_superuser(
#         self,
#         username,
#         email=None,
#         password=None,
#         role=UserRole.ADMIN,
#         **kwargs,
#     ):
#         """Создание суперпользователя."""
#         return super().create_superuser(
#             username=username,
#             email=email,
#             password=password,
#             role=role,
#             **kwargs,
#         )


# class User(AbstractUser):
#     """Кастомная модель пользователя."""

#     ROLES = [
#         (UserRole.SUPERVISOR, 'Вожатый'),
#         (UserRole.PARENT, 'Родитель'),
#         (UserRole.ADMIN, 'Администратор'),
#         (UserRole.KID, 'Ребенок'),
#     ]

#     @property
#     def is_admin(self):
#         return self.role == UserRole.ADMIN

#     @property
#     def is_supervisor(self):
#         return self.role == UserRole.SUPERVISOR

#     @property
#     def is_parent(self):
#         return self.role == UserRole.PARENT

#     objects = CustomUserManager()
#     first_name = models.CharField(max_length=150, null=True, blank=True)
#     last_name = models.CharField(max_length=150, null=True, blank=True)
#     email = models.EmailField(
#         unique=True,
#         null=False,
#         blank=False,
#         max_length=254
#     )
#     bio = models.TextField('Общая информация', null=True, blank=True)
#     med_info = models.TextField('Медицинская информация')
#     food_info = models.TextField('Информация о питании')
#     birth_date = models.DateField('Дата рождения')
#     parent = models.ForeignKey(User)
#     role = models.CharField(
#         max_length=10,
#         choices=ROLES,
#         default=UserRole.KID
#     )

#     balance = models.FloatField('Баланс', validators=[MinValueValidator(0)])

#     class Meta:
#         ordering = ['-id']

class Shift(models.Model):
    SEASONS = [
        ('Л','Лето'),
        ('О','Осень'),
        ('З', 'Зима'),
        ('В','Весна')
    ]
    number = models.IntegerField(
        'Номер смены',
        validators=[MinValueValidator(0), MaxValueValidator(999)]
    )
    year = models.IntegerField(
        'Год смены',
        validators=[MinValueValidator(2022), MaxValueValidator(2100)]
    )
    season = models.CharField('Сезон', choices=SEASONS, max_length=1)
    date_start = models.DateField('Дата начала смены')
    date_end = models.DateField('Дата конца смены')


class Team(models.Model):
    number = models.IntegerField('Отряд', validators=[MinValueValidator(0)], unique=True)
    name = models.CharField('Название отряда', max_length=128)
    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True, related_name='teams')


class Placement(models.Model):
    number = models.IntegerField('Номер корпуса')
    room = models.IntegerField('Номер комнаты')


class Administrator(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='admins')


class Supervisor(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='supervisors')
    bio = models.TextField('Общая информация', null=True, blank=True)
    birth_date = models.DateField('Дата рождения')
    shift = models.ManyToManyField(Shift, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)


class Parent(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='parents')
    balance = models.FloatField('Баланс', validators=[MinValueValidator(0.0)], default=0.0)

class Kid(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='kids')
    shift = models.ManyToManyField(Shift, related_name='kids', name='Смена')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='kids', name='Отряд')
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, related_name='kids', name='Родитель')
    birth_date = models.DateField('Дата рождения')
    bio = models.TextField('Общая информация')
    med_info = models.TextField('Медицинская информация')
    food_info = models.TextField('Информация о питании')
    #balance = models.FloatField('Баланс', validators=[MinValueValidator(0.0)], default=0.0)
    qr_code = models.ImageField('QR код')
    building_number = models.IntegerField('Номер корпуса')
    room = models.IntegerField('Номер комнаты')
    activities = models.ManyToManyField('services.Activity', related_name='kids')
    menus = models.ManyToManyField('services.Menu', related_name='kids')