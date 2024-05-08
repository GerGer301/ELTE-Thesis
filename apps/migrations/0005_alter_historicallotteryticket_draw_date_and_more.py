# Generated by Django 5.0.4 on 2024-05-06 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_alter_historicallotteryticket_draw_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallotteryticket',
            name='draw_date',
            field=models.DateField(db_index=True, unique=True, verbose_name='Draw Date'),
        ),
        migrations.AlterField(
            model_name='historicallotteryticket',
            name='draw_id',
            field=models.BigIntegerField(db_index=True, unique=True, verbose_name='Draw ID'),
        ),
    ]
