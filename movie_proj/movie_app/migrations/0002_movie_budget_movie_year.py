# Generated by Django 4.0.6 on 2022-08-12 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(default=1000000),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
