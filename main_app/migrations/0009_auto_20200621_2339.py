# Generated by Django 3.0.5 on 2020-06-21 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_player_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='country',
            field=models.TextField(max_length=550),
        ),
    ]
