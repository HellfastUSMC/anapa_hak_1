from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()


class Good(models.Model):
    name = models.CharField('Наименование')
    price = models.FloatField('Цена')


class Transaction(models.Model):
    number = models.IntegerField('Номер транзакции')
    goods = models.ManyToManyField(Good, related_name='transactions')
    total = models.IntegerField('Итог')


class Wallet(models.model):
    owner = models.OneToOneField(user, on_delete=models.CASCADE, related_name='wallet', name='Владелец')
    balance = models.IntegerField('Баланс')
