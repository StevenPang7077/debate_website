# Generated by Django 3.0.4 on 2020-11-25 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0018_auto_20201124_0508'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='performance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Performance'),
        ),
    ]
