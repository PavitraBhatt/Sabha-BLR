from django.shortcuts import render
from .models import Yuvako
from .serializers import YuvakoSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse   
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import status

# Create your views here.
@csrf_exempt       
def yuvako_get(request): 
    
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        # pythondata = JSONParser().parse(stream)
        decoded_data = stream.getvalue().decode('utf-8')
        pythondata = json.dumps(decoded_data)
        # id = pythondata.get('id',None)
        id = pythondata.get('id', None) if isinstance(pythondata, dict) else None

        if id is not None:
            yuvak = Yuvako.objects.get(id=id)
            serializer = YuvakoSerializer(yuvak)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type ='application/json')
        yuvak = Yuvako.objects.all()
        serializer = YuvakoSerializer(yuvak,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type ='application/json')
    
# @csrf_exempt
# def yuvak_get_id(request,id):  # Accept the 'SiteID' parameter
    
#     if request.method == 'GET':
#         if SiteID is not None:
#             try:
#                 site_obj = Site.objects.get(SiteID=SiteID)  # Assuming 'SiteID' is the field name
#                 serializer = SiteSerializer(site_obj)
#                 json_data = JSONRenderer().render(serializer.data)
#                 return HttpResponse(json_data, content_type='application/json')
#             except Site.DoesNotExist:
#                 return HttpResponse(status=404)
        
#         site = Site.objects.all()
#         serializer = SiteSerializer(site, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')

from django.db import IntegrityError

@csrf_exempt
def yuvak_post(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = YuvakoSerializer(data=pythondata)
        
        try:
            if serializer.is_valid():
                serializer.save()
                yuvako_data = [
                    serializer.validated_data["FirstName"],
                    serializer.validated_data["LastName"],
                    serializer.validated_data["MobileNumber"],
                    serializer.validated_data["DOB"].strftime("%Y-%m-%d"),  # Convert date to string
                    serializer.validated_data["Area"],
                    serializer.validated_data["ReferenceName"],
                    serializer.validated_data["ReferenceName"]
                ]
                
                add_yuvako_to_sheet(yuvako_data)
                res = {'msg': 'Data Created Successfully!'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json', status=status.HTTP_201_CREATED)
                
            else:
                json_data = JSONRenderer().render(serializer.errors)
                json_str = json_data.decode('utf-8')
                error_dict = json.loads(json_str)
                return JsonResponse(error_dict, status=status.HTTP_400_BAD_REQUEST, safe=False)
        
        except IntegrityError as e:
            # Handle duplicate MobileNumber error
            error_msg = "Duplicate MobileNumber. This number already exists."
            return JsonResponse({"error": error_msg}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            # Handle other exceptions
            error_msg = "An error occurred while processing your request."
            return JsonResponse({"error": error_msg}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
      
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializers import YuvakoSerializer
from .google_sheets import add_yuvako_to_sheet
# class AddYuvakAPIView(APIView):
#     def post(self, request):
#         serializer = YuvakoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = [serializer.validated_data["FirstName"], serializer.validated_data["LastName"],serializer.validated_data["DOB"],serializer.validated_data["Area"],serializer.validated_data["ReferenceName"],serializer.validated_data["ReferenceName"]]
#             add_yuvako_to_sheet(data)
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
    

import io
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .serializers import YuvakoSerializer
from .google_sheets import update_yuvako_in_sheet

@api_view(['POST'])
def update_yuvako(request, MobileNumber):
    try:
        yuvako = Yuvako.objects.get(MobileNumber=MobileNumber)
    except Yuvako.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = YuvakoSerializer(yuvako, data=pythondata, partial=True)
        
        if serializer.is_valid():
            serializer.save()

           
            updated_data = {
                "FirstName": serializer.validated_data["FirstName"],
                "LastName": serializer.validated_data["LastName"],
                "MobileNumber": serializer.validated_data["MobileNumber"],
                "DOB": serializer.validated_data["DOB"].strftime("%Y-%m-%d"),  # Convert date to string
                "Area": serializer.validated_data["Area"],
                "ReferenceName": serializer.validated_data["ReferenceName"],
            }

            update_yuvako_in_sheet(MobileNumber, updated_data)

            return Response({'msg': 'Data Updated Successfully!'}, status=status.HTTP_200_OK)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
