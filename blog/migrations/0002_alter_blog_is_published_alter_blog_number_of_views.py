# Generated by Django 5.2.3 on 2025-07-01 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Опубликовано"),
        ),
        migrations.AlterField(
            model_name="blog",
            name="number_of_views",
            field=models.PositiveIntegerField(default=0, verbose_name="Просмотры"),
        ),
    ]
