from django.db import models


# Create your models here.
class Historico(models.Model):
    time = models.DateTimeField('Data', auto_now_add=True)
    temp = models.FloatField('Temperatura')
    feels = models.FloatField('Sensação')
    dew = models.FloatField('Sereno')
    humidity = models.IntegerField('Umidade')
