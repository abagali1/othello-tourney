# Generated by Django 3.0.6 on 2020-05-28 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0014_auto_20200527_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
