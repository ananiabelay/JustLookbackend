from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Airdrop,TelegramUser
from .serializers import AirdropSerializer
from .serializers import UserConfig
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt

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
class AirdropCreateOrUpdate(APIView):
    def post(self, request):
        telegram_id = request.data.get('telegram_id')
        
        if not telegram_id:
            return Response({"error": "Telegram ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            airdrop = TelegramUser.objects.get(telegram_id=telegram_id)
            airdrop.login_count += 1
            airdrop.last_login = now()
            airdrop.save()
            serializer = UserConfig(airdrop)
            return Response({"message": "User updated.", "data": serializer.data}, status=status.HTTP_200_OK)
        
        except TelegramUser.DoesNotExist:
            # If user does not exist, create a new one
            serializer = UserConfig(data=request.data)
            if serializer.is_valid():
                serializer.save(date_joined=now(), login_count=1, last_login=now())
                return Response({"message": "New user added.", "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
