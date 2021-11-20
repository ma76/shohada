from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .shahid_serializer import *
#Define Api-View
class ShahidView(APIView):
    def get(self,request):
        query = ShahidModel.objects.all()
        serialized = ShahidSerializer(query,many=True)
        return Response(serialized.data,status = status.HTTP_200_OK)
