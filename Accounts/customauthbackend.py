from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User,AnonymousUser
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        try:
            user= User.objects.get(username=username)
            if user:
            
                if check_password(password,user.password):
                    return user
                else:
                    return AnonymousUser()
        
            else:
                return AnonymousUser()
        except BaseException as e:
            return AnonymousUser()
        
        





# class AdminBackend(BaseBackend):

#     def authenticate(self, request, username = None, password = None, **kwargs):

#         adminuser= User.objects.get(username=username)
#         if adminuser:
#             if check_password(password,adminuser.password):
#                 return adminuser
#             else:
#                 return None
#         else:
#             return None
#         return super().authenticate(request, username, password, **kwargs)