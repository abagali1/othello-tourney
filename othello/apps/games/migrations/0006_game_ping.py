# Generated by Django 3.0.6 on 2020-05-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_game_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='ping',
            field=models.BooleanField(default=True),
        ),
    ]
