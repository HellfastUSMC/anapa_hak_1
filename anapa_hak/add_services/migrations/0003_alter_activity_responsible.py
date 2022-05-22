# Generated by Django 3.2.13 on 2022-05-22 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220522_0457'),
        ('add_services', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='responsible',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='users.supervisor'),
        ),
    ]