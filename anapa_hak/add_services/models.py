from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import (MaxValueValidator, MinValueValidator)

#from users.models import Supervisor, Shift, Team

#from users import models as usrs

MENU_TYPES = [('Breakfast', 'Завтрак'), ('Dinner', 'Обед'), ('Supper', 'Ужин')]

FOODS = [('Food1', 'Еда1'), ('Food2', 'Еда2'), ('Food3', 'Еда3')]

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
    responsible = models.ForeignKey('users.Supervisor', on_delete=models.CASCADE, related_name='activities', blank=True, null=True)
    date_start = models.DateTimeField('Начало')
    date_end = models.DateTimeField('Начало')
    shift = models.ForeignKey('users.Shift', on_delete=models.CASCADE, related_name='activities')
    team = models.ForeignKey('users.Team', on_delete=models.CASCADE, related_name='activities')
    rating = models.FloatField('Рейтинг', validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    comment = models.TextField('Комментарий')