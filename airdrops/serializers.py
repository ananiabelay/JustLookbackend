# serializers.py
from rest_framework import serializers
from .models import Airdrop

class AirdropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airdrop
        fields = '__all__'  
