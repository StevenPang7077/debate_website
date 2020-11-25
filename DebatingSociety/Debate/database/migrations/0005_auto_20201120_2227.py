# Generated by Django 2.2.15 on 2020-11-20 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_performance_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='performance',
            old_name='rank_in_room',
            new_name='rank_in_room_total',
        ),
        migrations.RemoveField(
            model_name='performance',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='performance',
            name='debate_round',
        ),
        migrations.RemoveField(
            model_name='performance',
            name='form',
        ),
        migrations.RemoveField(
            model_name='performance',
            name='win',
        ),
        migrations.AddField(
            model_name='performance',
            name='wins',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='round',
            name='comment',
            field=models.TextField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='round',
            name='form',
            field=models.ForeignKey(help_text='Type of competition', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.Type'),
        ),
        migrations.AddField(
            model_name='round',
            name='performances',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Performance'),
        ),
        migrations.AddField(
            model_name='round',
            name='rank_in_room',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='round',
            name='win',
            field=models.IntegerField(default=-1, help_text='0 for loss, 1 for win, -1 for N.A'),
        ),
    ]