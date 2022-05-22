# from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import (MaxValueValidator, MinValueValidator)

from add_services.models import Menu, Activity

user = get_user_model()


class Shift(models.Model):
    SEASONS = [
        ('SUMMER', 'Лето'),
        ('AUTUMN', 'Осень'),
        ('WINTER', 'Зима'),
        ('SPRING', 'Весна'),
    ]
    number = models.IntegerField(
        'Номер смены',
        validators=[MinValueValidator(0), MaxValueValidator(999)]
    )
    year = models.IntegerField(
        'Год смены',
        validators=[MinValueValidator(2022), MaxValueValidator(2100)]
    )
    season = models.CharField('Сезон', choices=SEASONS, max_length=255)
    date_start = models.DateField('Дата начала смены')
    date_end = models.DateField('Дата конца смены')


class Team(models.Model):
    number = models.IntegerField('Отряд', validators=[MinValueValidator(0)], unique=True)
    name = models.CharField('Название отряда', max_length=255)
    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True, related_name='teams')


class Placement(models.Model):
    number = models.IntegerField('Номер корпуса')
    room = models.IntegerField('Номер комнаты')

class Achivements(models.Model):
    ACHIVE_CATS = [
        ('sport', 'Спорт'),
        ('sci', 'Наука'),
        ('lit', 'Литература'),
        ('it', 'ИТ'),
    ]
    name = models.CharField('Название', max_length=128)
    category = models.CharField('Категория', max_length=128, choices=ACHIVE_CATS)

class Administrator(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='admins')


class Supervisor(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='supervisors')
    bio = models.TextField('Общая информация', null=True, blank=True)
    birth_date = models.DateField('Дата рождения')
    shift = models.ManyToManyField(Shift, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)


class Parent(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='parents')
    balance = models.FloatField('Баланс', validators=[MinValueValidator(0.0)], default=0.0)

class Kid(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='kids')
    shift = models.ManyToManyField(Shift, related_name='kids', name='shift', blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='kids', name='team', blank=True)
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, related_name='kids', name='parent', blank=True)
    birth_date = models.DateField('Дата рождения')
    bio = models.TextField('Общая информация')
    med_info = models.TextField('Медицинская информация')
    food_info = models.TextField('Информация о питании')
    balance = models.FloatField('Баланс', validators=[MinValueValidator(0.0)], default=0.0)
    qr_code = models.ImageField('QR код')
    building_number = models.IntegerField('Номер корпуса')
    room = models.IntegerField('Номер комнаты')
    achivements = models.ManyToManyField(Achivements,)
    activities = models.ManyToManyField(Activity, related_name='kids', blank=True, null=True)
    menus = models.ManyToManyField(Menu, related_name='kids', blank=True, null=True)
