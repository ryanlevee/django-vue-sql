# Generated by Django 4.0.5 on 2022-10-18 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0019_remove_gamescore_title_gamescore_game_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamescore',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
