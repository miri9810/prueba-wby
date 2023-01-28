from rest_framework import serializers
from .models import Codigos, Municipios, Estados


class CodigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estados
        exclude = ('status_delete', )


class MoveImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ('id', 'name', 'description', 'amount', 'move_picture', 'day', 'account', 'concept')
        #exclude = ('status_delete',)

    def create(self, validated_data):
        moves = Move.objects.create(
            name = validated_data.get('name'),
            description = validated_data.get('description'),
            amount = validated_data.get('amount'),
            move_picture = validated_data.get('move_picture'),
            day = validated_data.get('day'),
            #user_id = validated_data.get('user_id')            
        )
        moves.account.set(validated_data.get('account'))
        moves.concept.set(validated_data.get('concept'))
        moves.save()
        return moves

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['concept'] = ConceptSerializer(instance.concept.all(), many=True).data
        response['account'] = AccountBalanceSerializer(instance.account.all(), many=True).data
        #response['user'] = {'id':User.id}
        return response
