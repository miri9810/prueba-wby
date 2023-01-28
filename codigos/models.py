from django.db import models

# Create your models here.

class Codigo(models.Model):
    codigo = models.IntegerField()
    colonia = models.CharField(max_length=255, verbose_name='colonia')

    class Meta:
        db_table = 'codigos'
