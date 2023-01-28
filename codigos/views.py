from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Estados, Municipios, Codigos
from .serializers import EstadoSerializer, MunicipioSerializer, CodigoSerializer

# Create your views here.


class EstadoView(APIView):
    permission_classes=(IsAuthenticated,)

    def post(self, request):
        data = request.data
        data['user_id']=request.user.id
        serializer = EstadoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MunicipioView(APIView):
    permission_classes=(IsAuthenticated,)

    def post(self, request):
        data = request.data
        #data['user_id']=request.user.id
        serializer = MunicipioSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MunicipioIDView(APIView):
    permission_classes=(IsAuthenticated,)

    def get(self, request, pk):
        mun_list = Municipios.objects.filter(pk=pk, user=request.user, status_delete=False)
        serializer = MunicipioSerializer(mun_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        mun_obj = get_object_or_404(Municipios, pk=pk, user=request.user)
        serializer = MunicipiosSerializer(instance=mun_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CodigoView(APIView):
    permission_classes=(IsAuthenticated,)

    def post(self, request):
        data = request.data
        #data['user_id']=request.user.id
        serializer = CodigoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CodigoIDView(APIView):
    permission_classes=(IsAuthenticated,)

    def get(self, request, pk):
        cod_list = Codigos.objects.filter(pk=pk, user=request.user, status_delete=False)
        serializer = CodigoSerializer(cod_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        cod_obj = get_object_or_404(Codigos, pk=pk, user=request.user)
        serializer = CodigoSerializer(instance=cod_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        cod_obj = get_object_or_404(Account, pk=pk, status_delete=False)
        cod_obj.status_delete = True
        cod_obj.save()
        return Response({'message':'Eliminado'}, status=status.HTTP_204_NO_CONTENT)