from django.db import models

# Create your models here.

class Codigo(models.Model):
    colonia = models.CharField(max_length=255, verbose_name='colonia')
    municipio = models.CharField(max_length=255, verbose_name='municipio')
    estado = models.CharField(max_length=255, verbose_name='estado')

    class Meta:
        db_table = 'codigos'
