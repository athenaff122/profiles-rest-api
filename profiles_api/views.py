from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloAPIView(APIView):
    "test api view"
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        "return a list of apiview feature"
        an_apiview=[
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'is similar to a traditional django view',
            'gives you the most control over your application logic',
            'is mapped manually to urls',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})
# Create your views here.

    def post(self,request):
        "create a hello message with our name"
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
              status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        "handle updating an object"
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        "handle a partial update of an object"
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        "delete an object"
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    "Test API Viewset"
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        a_viewset=[
        'Uses actions (list, create, retrieve, update, partial_update)',
        'Automactically maps to URLs using Routers',
        'Provides more functionality with less code',
        ]
        "return a hello message"
        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        "create a new hello message"
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        "handle getting an object by its ID"
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        "handle a partial update of an object"
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        "delete an object"
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        "handle removing object"
        return Response({'http_method': 'DELETE'})
