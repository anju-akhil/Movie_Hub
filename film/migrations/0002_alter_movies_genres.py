# Generated by Django 5.0.1 on 2024-01-27 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='genres',
            field=models.ManyToManyField(to='film.genre'),
        ),
    ]
