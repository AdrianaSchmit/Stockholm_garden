# Generated by Django 3.2 on 2022-04-10 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_reviews_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.DecimalField(choices=[(1, ' ⭐ '), (2, ' ⭐  ⭐ '), (3, ' ⭐  ⭐  ⭐ '), (4, ' ⭐  ⭐  ⭐  ⭐ '), (5, ' ⭐  ⭐  ⭐  ⭐  ⭐ ')], decimal_places=0, max_digits=2, null=True),
        ),
    ]
