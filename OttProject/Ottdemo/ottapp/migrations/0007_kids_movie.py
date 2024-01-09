# Generated by Django 5.0.1 on 2024-01-09 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ottapp', '0006_adult_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kids_Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('language', models.CharField(max_length=100)),
                ('actor', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('ratings', models.FloatField(default=0.0)),
                ('image', models.ImageField(upload_to='movie_image/')),
                ('video', models.FileField(upload_to='movie_videos/')),
            ],
        ),
    ]
