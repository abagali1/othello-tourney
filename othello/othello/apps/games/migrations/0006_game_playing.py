# Generated by Django 3.0.5 on 2020-04-08 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20200406_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='playing',
            field=models.BooleanField(default=False),
        ),
    ]
