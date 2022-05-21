from django.db import models
from django.core.validators import (MaxValueValidator, MinValueValidator)

MENU_TYPES = [('Bre', 'Завтрак'), ('Din', 'Обед'), ('Sup', 'Ужин')]

FOODS = [('Food1', 'Супчик'), ('Food2', 'Булка'), ('Food3', 'Фрукты')]
from users.models import Supervisor, Shift, Team


class Menu(models.Model):
    date = models.DateTimeField('Время и дата')
    menu_type = models.CharField('Вид меню', choices=MENU_TYPES, max_length=3)
    dishes = models.CharField('Блюда',choices=FOODS, max_length=32)
    # dishes = models.ManyToManyField(Food, related_name='Menus')

class Activity(models.Model):
    name = models.CharField('Название', max_length=128)
    responsible = models.ForeignKey(Supervisor, on_delete=models.CASCADE, related_name='activities')
    date_start = models.DateTimeField('Начало')
    date_end = models.DateTimeField('Начало')
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='activities')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='activities')
    rating = models.FloatField('Рейтинг', validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    comment = models.TextField('Комментарий')