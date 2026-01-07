from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from rest_framework.decorators import api_view
# Create your views here.
import requests


class UserSignupAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            serializer = UsersOtherInformationSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                refresh_token = RefreshToken.for_user(user)
                access_token = refresh_token.access_token
                return Response({"refresh":str(refresh_token), "access":str(access_token), "data":serializer.data}, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        

class UserLoginAPI(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    

@api_view(["GET"])
def external_api_data(request):
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    result = response.json()
    print("Inside view...")
    return Response(result)