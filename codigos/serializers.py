from rest_framework import serializers
from .models import Codigos, Municipios, Estados


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estados
        exclude = ('status_delete', )


class MunicipioSerialier(serializers.ModelSerializer):
    class Meta: 
        model = Municipios
        fields = ('municipios', 'estados')

        def to_representation(self, instance):
            response = super().to_representation(instance)
            response['estado'] = EstadoSerializer(instance.estado.all(), many=True).data
            return response


class MoveImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ('codigo', 'colonia', 'municipio', 'estado')

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
