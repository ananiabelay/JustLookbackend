# serializers.py
from rest_framework import serializers
from .models import Airdrop
from .models import TelegramUser

class AirdropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airdrop
        fields = '__all__'  
class UserConfig(serializers.ModelSerializer):
    last_login = serializers.DateField(source='date_time_field', read_only=True)
    date_joined = serializers.DateField(source='date_time_field', read_only=True)

    class Meta:
        model = TelegramUser
        fields = '__all__'