# Generated by Django 4.1.5 on 2023-01-28 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('01', 'Aguascalientes'), ('02', 'Baja California'), ('03', 'Baja California Sur'), ('04', 'Campeche'), ('05', 'Chiapas'), ('06', 'Chihuahua'), ('07', 'Coahuila'), ('08', 'Colima'), ('09', 'CDMX'), ('10', 'Durango'), ('11', 'Guanajuato'), ('12', 'Guerrero'), ('13', 'Hidalgo'), ('14', 'Jalisco'), ('15', 'México'), ('16', 'Michoacán'), ('17', 'Morelos'), ('18', 'Nayarit'), ('19', 'Nuevo León'), ('20', 'Oaxaca'), ('21', 'Puebla'), ('22', 'Querétaro'), ('23', 'Quintana Roo'), ('24', 'San Luis Potosí'), ('25', 'Sinaloa'), ('26', 'Sonora'), ('27', 'Tabasco'), ('28', 'Tamaulipas'), ('29', 'Tlaxcala'), ('30', 'Veracruz'), ('31', 'Yucatán'), ('32', 'Zacatecas')], max_length=255, verbose_name='nombre del estado')),
                ('status_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'estados',
            },
        ),
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.CharField(max_length=255, verbose_name='nombre del municipio')),
                ('status_delete', models.BooleanField(default=False)),
                ('estado', models.ManyToManyField(to='codigos.estados')),
            ],
            options={
                'db_table': 'municipios',
            },
        ),
        migrations.CreateModel(
            name='Codigos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('colonia', models.CharField(max_length=255, verbose_name='colonia')),
                ('status_delete', models.BooleanField(default=False)),
                ('estado', models.ManyToManyField(to='codigos.estados')),
                ('municipio', models.ManyToManyField(to='codigos.municipios')),
            ],
            options={
                'db_table': 'codigos',
            },
        ),
    ]
