import jwt
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_100_CONTINUE
import dotenv
from pathlib import Path
import os
from django.contrib.auth.models import AnonymousUser
env_path=Path('F:\Workspace\Backend\School\School\School\.env')

  #Loading environment data

class CustomAuthMiddleware(APIView):
    def __init__(self,get_response):
        self.get_response=get_response
        dotenv.load_dotenv(env_path)
    
    def __call__(self,request):
        if request.path.startswith('/admin'):
            return self.get_response(request)
        
        
        def get_token_from_header(request):
            token= request.headers.get("Authorization")
            if token and token.startswith("Bearer"):
                return token.split(' ')[1]
            else:
                return None
           
        
        def get_user_from_token(request):
            try:
                token= get_token_from_header(request)
                
                if token:
                    key=os.getenv('SECRET_KEY')
                   
                    payload= jwt.decode(token,key,algorithms=['HS256'])

                    if payload:
                        
                        user_id= payload.get('user_id')
                        
                        user= User.objects.get(id=user_id)
                        
                        return user
                    
                    else:
                        return AnonymousUser()
                else:
                    return AnonymousUser()
        
            except (jwt.ExpiredSignatureError,jwt.InvalidTokenError) as e:
                return AnonymousUser()
        user=get_user_from_token(request)
        request.user= user
        return self.get_response(request)
        
        
    
