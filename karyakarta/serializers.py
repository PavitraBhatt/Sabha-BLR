from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

from rest_framework import serializers
from .models import Karyakarta

class KaryakartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karyakarta
        fields = ['id', 'username', 'hashed_password']
