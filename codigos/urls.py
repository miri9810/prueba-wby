from django.urls import path
from .views import EstadoView, MunicipioView, MunicipioIDView, CodigoView, CodigoIDView

urlpatterns = [
    path('estado/', EstadoView.as_view(), name='Registro de Estados'),
    path('municipio/', MunicipioView.as_view(), name='Registro de Municipios'),
    path('municipio/<int:pk>/', MunicipioIDView.as_view(), name='CRUD de Municipios'),
    path('codigo/', CodigoView.as_view(), name='Registro de Codigos'),
    path('codigo/<int:pk>/', CodigoIDView.as_view(), name='CRUD de Codigos'),

]