# Generated by Django 3.2.13 on 2022-05-21 23:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('date_start', models.DateTimeField(verbose_name='Начало')),
                ('date_end', models.DateTimeField(verbose_name='Начало')),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='Рейтинг')),
                ('comment', models.TextField(verbose_name='Комментарий')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Время и дата')),
                ('menu_type', models.CharField(choices=[('Breakfast', 'Завтрак'), ('Dinner', 'Обед'), ('Supper', 'Ужин')], max_length=255)),
                ('dishes', models.CharField(choices=[('Food1', 'Еда1'), ('Food2', 'Еда2'), ('Food3', 'Еда3')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('date', models.DateField(verbose_name='Дата')),
                ('text', models.TextField(verbose_name='Текст')),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('date', models.DateField(verbose_name='Дата')),
                ('text', models.TextField(verbose_name='Текст')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
