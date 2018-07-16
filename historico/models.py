from django.db import models


# Create your models here.
class Historico(models.Model):
    time = models.DateTimeField('Data', auto_now_add=True)
    temp = models.CharField('Temperatura', max_length=30)
    feels = models.CharField('Sensação', max_length=30)
    dew = models.CharField('Sereno', max_length=30)
    humidity = models.IntegerField('Umidade')
