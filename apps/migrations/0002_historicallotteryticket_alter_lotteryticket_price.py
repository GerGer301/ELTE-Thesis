# Generated by Django 5.0.4 on 2024-05-06 00:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalLotteryTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw_id', models.IntegerField(unique=True, verbose_name='Draw ID')),
                ('draw_date', models.DateTimeField(unique=True, verbose_name='Draw Date')),
                ('red_1', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(33)], verbose_name='Red Ball 1')),
                ('red_2', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(33)], verbose_name='Red Ball 2')),
                ('red_3', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(33)], verbose_name='Red Ball 3')),
                ('red_4', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(33)], verbose_name='Red Ball 4')),
                ('red_5', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(33)], verbose_name='Red Ball 5')),
                ('red_6', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(33)], verbose_name='Red Ball 6')),
                ('blue_1', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(16)], verbose_name='Blue Ball 1')),
            ],
        ),
        migrations.AlterField(
            model_name='lotteryticket',
            name='price',
            field=models.IntegerField(default=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
