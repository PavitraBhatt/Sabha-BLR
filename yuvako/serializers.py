from rest_framework import serializers
from .models import Yuvako

class YuvakoSerializer(serializers.Serializer):
    FirstName = serializers.CharField(max_length=100)
    LastName = serializers.CharField(max_length=100)
    DOB = serializers.DateField()
    Area = serializers.CharField(max_length=100)
    ReferenceName = serializers.CharField(max_length=100)
    Coming = serializers.BooleanField(default=True)

    def create(self,validate_data):
        return Yuvako.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.FirstName = validated_data.get('FirstName',instance.FirstName)
        instance.LastName = validated_data.get('LastName',instance.LastName)
        instance.DOB = validated_data.get('DOB',instance.DOB)
        instance.Area = validated_data.get('Area',instance.Area)
        instance.ReferenceName = validated_data.get('ReferenceName',instance.ReferenceName)
        instance.Coming = validated_data.get('Coming',instance.Coming)
        instance.save()
        return instance
    