from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializer


class HelloAPIView(APIView):
    """ API View prueba """

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
