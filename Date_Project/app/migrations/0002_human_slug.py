# Generated by Django 4.2.7 on 2023-11-18 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]