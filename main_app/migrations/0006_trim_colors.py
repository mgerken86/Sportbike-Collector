# Generated by Django 4.0.6 on 2022-07-22 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_colors'),
    ]

    operations = [
        migrations.AddField(
            model_name='trim',
            name='colors',
            field=models.ManyToManyField(to='main_app.colors'),
        ),
    ]