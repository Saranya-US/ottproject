# Generated by Django 5.0.1 on 2024-01-09 23:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ottapp', '0009_adult_watchlater'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adult_Suggestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggested_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ottapp.adult_movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ottapp.userprofile')),
            ],
        ),
    ]