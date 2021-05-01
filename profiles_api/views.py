from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializer


class HelloAPIView(APIView):
    """ API View prueba """

    serializer_class = serializer.HelloSerializer

    def get(self, request, formart=None):
        """ Retornar lista de caracteristica del APIView """
        an_apiview = [
            'usamos metodos HTTP como funciones (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de django',
            'nos da el mayor control sobre la logica de nuestra aplicacion',
            'Esta mapeado manualmente a los URLS',
        ]

        return Response(
            {
                'message': 'Hello',
                'an_apiview': an_apiview
            }
        )

    def post(self, request):
        """ Crea un mensaje con nuestro nombre """
        # serializer_class es una clase que configura nuestra clase para la PIVIEW, es una manera estandar
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response(
                {
                    'message': message
                }
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        def put(self, request, pk=None):
            """ Maneja actualizar un objeto """
            return Response({'method': 'PUT'})

        def patch(self, request, pk=None):
            """ Maneja actualizar parcial de un objeto """
            return Response({'method': 'PATCH'})

        def delete(self, request, pk=None):
            """ Delete un objeto """
            return Response({'method': 'DELETE'})
