from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    "test api view"

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
