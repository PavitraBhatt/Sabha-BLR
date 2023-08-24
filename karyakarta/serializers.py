# from rest_framework import serializers

# class LoginSerializer(serializers.Serializer):
    # username = serializers.CharField()
    # password = serializers.CharField()
    # FirstName = serializers.CharField(max_length=100)
    # LastName = serializers.CharField(max_length=100)
    # DOB = serializers.DateField()
    # Area = serializers.CharField(max_length=100)
    # serializers.py

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
