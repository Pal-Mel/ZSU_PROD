from rest_framework.views import APIView
from rest_framework.response import Response

class TestApiView(APIView):
    def get(self, request, *args, **kwargs):
        data = [{'id':1, 'name':'djon'},{'id':2, 'name':'fill'} ]
        return Response(data)