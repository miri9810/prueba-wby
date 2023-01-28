from rest_framework import serializers
from .models import Codigos, Estados, Municipios


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estados
        fields = ('estado', 'user')


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Municipios
        fields = ('municipio', 'estado', 'user')

        def to_representation(self, instance):
            response = super().to_representation(instance)
            response['estado'] = EstadoSerializer(instance.estado.all(), many=True).data
            return response


class CodigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codigos
        fields = ('codigo', 'colonia', 'municipio', 'estado', 'user')

    def create(self, validated_data):
        codigo = Codigos.objects.create(
            codigo = validated_data.get('codigo'),
            colonia = validated_data.get('colonia')         
        )
        codigo.municipio.set(validated_data.get('municipio'))
        codigo.estado.set(validated_data.get('estado'))
        codigo.save()
        return codigo

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['municipio'] = MunicipioSerializer(instance.municipio.all(), many=True).data
        response['estado'] = EstadoSerializer(instance.estado.all(), many=True).data
        return response
