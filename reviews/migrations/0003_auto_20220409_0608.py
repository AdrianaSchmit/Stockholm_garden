# Generated by Django 3.2 on 2022-04-09 06:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220306_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='user_name',
        ),
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.DecimalField(decimal_places=0, max_digits=1, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]