from django.contrib import admin
from .models import Estados, Municipios, Codigos

# Register your models here.

admin.site.register(Estados)
admin.site.register(Municipios)
admin.site.register(Codigos)