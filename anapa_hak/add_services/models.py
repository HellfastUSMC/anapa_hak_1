from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import (MaxValueValidator, MinValueValidator)

from users.models import Supervisor, Shift, Team

MENU_TYPES = ['Breakfast', 'Dinner', 'Supper']

FOODS = ['Food1', 'Food2', 'Food3']

user = get_user_model()

class Poll(models.Model):
    header = models.CharField('Заголовок', max_length=255)
    date = models.DateField('Дата')
    text = models.TextField('Текст')
    rating = models.FloatField()


class News(models.Model):
    header = models.CharField('Заголовок', max_length=255)
    date = models.DateField('Дата')
    text = models.TextField('Текст')
    author = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, related_name='news')


class Menu(models.Model):
    date = models.DateTimeField('Время и дата')
    menu_type = models.CharField(choices=MENU_TYPES, max_length=255)
    dishes = models.CharField(choices=FOODS, max_length=255)
    # dishes = models.ManyToManyField(Food, related_name='Menus')


class Activity(models.Model):
    name = models.CharField('Название', max_length=255)
    responsible = models.ForeignKey(Supervisor, on_delete=models.CASCADE, related_name='activities')
    date_start = models.DateTimeField('Начало')
    date_end = models.DateTimeField('Начало')
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='activities')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='activities')
    rating = models.FloatField('Рейтинг', validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    comment = models.TextField('Комментарий')