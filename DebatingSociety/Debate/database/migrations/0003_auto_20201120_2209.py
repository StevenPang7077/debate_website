# Generated by Django 2.2.15 on 2020-11-20 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20201107_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='win',
            field=models.IntegerField(default=-1, help_text='0 for loss, 1 for win, -1 for N.A'),
        ),
        migrations.AlterField(
            model_name='performance',
            name='rank_in_room',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='performance',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
