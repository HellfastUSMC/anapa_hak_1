from django.db import models
from django.core.validators import (MaxValueValidator, MinValueValidator)

MENU_TYPES = ['Breakfast', 'Dinner', 'Supper']

FOODS = ['Food1', 'Food2', 'Food3']

class Poll(models.Model):
    header = models.CharField('Заголовок')
    date = models.DateField('Дата')
    text = models.TextField('Текст')
    rating = models.FloatField()


class News(models.Model):
    header = models.CharField('Заголовок')
    date = models.DateField('Дата')
    text = models.TextField('Текст')
    author = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, related_name='news')


class Menu(models.Model):
    date = models.DateTimeField('Время и дата')
    menu_type = models.CharField(MENU_TYPES)
    dishes = models.CharField(FOODS)
    # dishes = models.ManyToManyField(Food, related_name='Menus')


class Activity(models.Model):
    name = models.CharField('Название')
    responsible = models.ForeignKey('Supervisor', on_delete=models.CASCADE, related_name='activities')
    date_start = models.DateTimeField('Начало')
    date_end = models.DateTimeField('Начало')
    shift = models.ForeignKey('Shift', on_delete=models.CASCADE, related_name='activities')
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='activities')
    rating = models.FloatField('Рейтинг', validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    comment = models.TextField('Комментарий')