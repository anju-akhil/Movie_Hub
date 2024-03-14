# Generated by Django 5.0.1 on 2024-02-01 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_alter_movies_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='review_movie', to='film.movies'),
        ),
    ]
