# Generated by Django 3.1.7 on 2021-04-23 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0028_auto_20210423_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='black',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='black', to='games.submission'),
        ),
        migrations.AlterField(
            model_name='game',
            name='white',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='white', to='games.submission'),
        ),
    ]