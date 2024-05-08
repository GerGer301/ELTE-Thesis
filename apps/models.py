from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from myaccount.models import User

class LotteryTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    red_1 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(33)])
    red_2 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(33)])
    red_3 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(33)])
    red_4 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(33)])
    red_5 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(33)])
    red_6 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(33)])
    blue_1 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(16)])
    purchase_date = models.DateField(auto_now_add=False)
    price = models.IntegerField(validators=[MinValueValidator(0)], default=2)
    won_amount = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return f'{self.user.username}\'s ticket on {self.purchase_date}'

class HistoricalLotteryTicket(models.Model):
    draw_id = models.BigIntegerField(unique=True, verbose_name='Draw ID', db_index=True)
    draw_date = models.DateField(auto_now_add=False, unique=True, verbose_name='Draw Date', db_index=True)
    red_1 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(33)], verbose_name='Red Ball 1')
    red_2 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(33)], verbose_name='Red Ball 2')
    red_3 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(33)], verbose_name='Red Ball 3')
    red_4 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(33)], verbose_name='Red Ball 4')
    red_5 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(33)], verbose_name='Red Ball 5')
    red_6 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(33)], verbose_name='Red Ball 6')
    blue_1 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(16)], verbose_name='Blue Ball 1')

    def __str__(self):
        return f'Draw ID: {self.draw_id} on {self.draw_date}'
    
