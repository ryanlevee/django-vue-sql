# Generated by Django 4.0.5 on 2022-10-18 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0020_alter_gamescore_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamescore',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
