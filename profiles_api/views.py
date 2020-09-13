from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIview features"""
        an_apiview = [
            'use HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional django view',
            'gives you the most control over your application logic',
            'IS mapped manually to URLs',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
