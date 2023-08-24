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
    

@csrf_exempt       
def kk_get(request): 
    
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        # pythondata = JSONParser().parse(stream)
        decoded_data = stream.getvalue().decode('utf-8')
        pythondata = json.dumps(decoded_data)
        # id = pythondata.get('id',None)
        id = pythondata.get('id', None) if isinstance(pythondata, dict) else None

        if id is not None:
            kk = Karyakarta.objects.get(id=id)
            serializer = KaryakartaSerializer(kk)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type ='application/json')
        kk = Karyakarta.objects.all()
        serializer = KaryakartaSerializer(kk,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type ='application/json')