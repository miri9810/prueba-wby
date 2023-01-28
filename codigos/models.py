from django.db import models

# Create your models here.

class Estados(models.Model):
    opciones = [
            ('01','Aguascalientes'),
            ('02','Baja California'),
            ('03', 'Baja California Sur'),
            ('04', 'Campeche'),
            ('05', 'Chiapas'),
            ('06', 'Chihuahua'),
            ('07', 'Coahuila'),
            ('08', 'Colima'),
            ('09', 'CDMX'),
            ('10', 'Durango'),
            ('11', 'Guanajuato'),
            ('12', 'Guerrero'),
            ('13', 'Hidalgo'),
            ('14', 'Jalisco'),
            ('15', 'México'),
            ('16', 'Michoacán'),
            ('17', 'Morelos'),
            ('18', 'Nayarit'),
            ('19', 'Nuevo León'),
            ('20', 'Oaxaca'),
            ('21', 'Puebla'),
            ('22', 'Querétaro'),
            ('23', 'Quintana Roo'),
            ('24', 'San Luis Potosí'),
            ('25', 'Sinaloa'),
            ('26', 'Sonora'),
            ('27', 'Tabasco'),
            ('28', 'Tamaulipas'),
            ('29', 'Tlaxcala'),
            ('30', 'Veracruz'),
            ('31', 'Yucatán'),
            ('32', 'Zacatecas')
        ]
    estado = models.CharField(choices=opciones, max_length=255, verbose_name='nombre del estado')
    status_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'estados'


class Municipios(models.Model):
    municipio = models.CharField(max_length=255, verbose_name='nombre del municipio')
    estado = models.ManyToManyField(Estados)
    status_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'municipios'


class Codigos(models.Model):
    codigo = models.IntegerField()
    colonia = models.CharField(max_length=255, verbose_name='colonia')
    municipio = models.ManyToManyField(Municipios)
    estado = models.ManyToManyField(Estados)
    status_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'codigos'


