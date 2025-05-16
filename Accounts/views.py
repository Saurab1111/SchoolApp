from django.shortcuts import render
from rest_framework.decorators import api_view
from Accounts.serializers import SingUpSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
import jwt
from datetime import datetime, timedelta
from rest_framework.status import HTTP_200_OK
from django.contrib.auth.models import User,AnonymousUser
import os


@api_view(['POST'])
def signUp(request):
    if request.method=='POST':
        serializer= SingUpSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'response':"Singed Successfully!!"})

@api_view(['POST'])
def login(request):
    if request.method=='POST':
        user = authenticate(request=request,username=request.data['username'],password=request.data['password'])
        print(user)
        if not isinstance(user,AnonymousUser):
            payload={
                'user_id':user.id,
                'exp': datetime.now() + timedelta(hours=1)
            }
             
            key= os.getenv('SECRET_KEY')

            
            token = jwt.encode(payload, key, algorithm="HS256")
            print(token)
            
            response1=Response(f"Successfully logged in!, jwt token-{token}",status=HTTP_200_OK)
            response1.set_cookie(key=token,httponly=True,secure=True)
            return response1
        else:
            return Response({'error':'No Such User'},status=HTTP_200_OK)    

# Create your views here.
