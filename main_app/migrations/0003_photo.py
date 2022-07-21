# Generated by Django 4.0.6 on 2022-07-21 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_sportbike_displacement_sportbike_make_sportbike_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('sportbike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.sportbike')),
            ],
        ),
    ]
