# Generated by Django 3.0.5 on 2020-04-10 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_auto_20200408_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='usable',
            field=models.BooleanField(default=True),
        ),
    ]