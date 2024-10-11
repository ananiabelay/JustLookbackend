# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Airdrop
from .serializers import AirdropSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Airdrop
from .serializers import AirdropSerializer
class ItemList(APIView):
    def get(self, request):
        airdrops = Airdrop.objects.all()
        serializer = AirdropSerializer(airdrops, many=True)
        return Response(serializer.data)
class AirdropDetailView(APIView):
    def get(self, request, id):
        try:
            airdrop = Airdrop.objects.get(id=id)
            serializer = AirdropSerializer(airdrop)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Airdrop.DoesNotExist:
            return Response({"error": "Airdrop not found."}, status=status.HTTP_404_NOT_FOUND)
