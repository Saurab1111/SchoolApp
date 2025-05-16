from django.urls import path
from Accounts.views import signUp,login
from Accounts.customauthmiddleware import CustomAuthMiddleware

urlpatterns = [
    path('signup/',signUp),
    path('login/',login),
    path('get_user/',CustomAuthMiddleware.as_view())
]
