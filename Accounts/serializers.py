from rest_framework import serializers
from django.contrib.auth.models import User

class SingUpSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
    
    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
    def validate_password(self,value):
        if len(value)<8:
            return "Password length is less than 8"
        else:
            return value