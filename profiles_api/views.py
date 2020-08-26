from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers
from profiles_api import models

class HelloApiView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similiar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message' : 'Hello!' , 'an_apiview' : an_apiview})

    def post(self, request):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                            )

    def put(self, request, pk=None):
        """ Handle updating an object """
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """ Handle partial update of an object """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test Api Viewset """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return a hello message """
        an_viewset = [
            'Uses HTTP methods as functions (list, create ,retrieve, update , partial_update)',
            'Auto maps to URLs using Routers',
            'More function with less code',
        ]
        return Response({'message': 'Hello!', 'Viewset': an_viewset})

    def create(self, request):
        """ Create a new hello message """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ Handle getting an object by its ID """
        return Response({'http_method':'GET'})

    def updata(self, request, pk=None):
        """ Handle object update """
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """ Handle updating object """
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """ Handle deleting an object """
        return Respnse({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    
