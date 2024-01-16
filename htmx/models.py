from django.db import models

# Create your models here.
class Login(models.Model):
     username = models.CharField(max_length=50, verbose_name='')
     salary = models.CharField(max_length=50, verbose_name='', default='')
     number = models.CharField(max_length=50, verbose_name='', default='')