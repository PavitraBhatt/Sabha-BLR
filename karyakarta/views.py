from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import bcrypt
from .models import Karyakarta
from django.views.decorators.csrf import csrf_exempt
import io
import json
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse   
from .serializers import KaryakartaSerializer

class KaryakartaCreateView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        if Karyakarta.objects.filter(username=username).exists():
            return Response({'message': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        new_karyakarta = Karyakarta(username=username, hashed_password=hashed_password)
        new_karyakarta.save()

        return Response({'message': 'Karyakarta created successfully'}, status=status.HTTP_201_CREATED)



class LoginView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            karyakarta = Karyakarta.objects.get(username=username)
        except Karyakarta.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if bcrypt.checkpw(password.encode('utf-8'), karyakarta.hashed_password):
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
