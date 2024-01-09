# Generated by Django 5.0.1 on 2024-01-09 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ottapp', '0007_kids_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adult_WatchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ottapp.adult_movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ottapp.userprofile')),
            ],
        ),
    ]
