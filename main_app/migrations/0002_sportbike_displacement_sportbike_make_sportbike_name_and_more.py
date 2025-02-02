# Generated by Django 4.0.6 on 2022-07-21 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportbike',
            name='displacement',
            field=models.CharField(default='600cc', max_length=30),
        ),
        migrations.AddField(
            model_name='sportbike',
            name='make',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sportbike',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sportbike',
            name='skill_lvl',
            field=models.CharField(default='advanced', max_length=50),
        ),
    ]
