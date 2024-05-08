from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True, default='', verbose_name='nickname')

    lottery_type = models.CharField(max_length=30, blank=True, default='super lotto', verbose_name='lottery_type')

    telephone = models.CharField(max_length=20, blank=True, default='00000000000', verbose_name='telephone')

    first_name = models.CharField(max_length=30, blank=True, default='', verbose_name='first_name')
    last_name = models.CharField(max_length=30, blank=True, default='', verbose_name='last_name')

    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'user_info'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.username
