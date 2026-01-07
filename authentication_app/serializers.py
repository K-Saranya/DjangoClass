from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# User = get_user_model

class UserLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class UsersOtherInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersOtherInformation
        fields = '__all__'
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        user =UsersOtherInformation.objects.create_user(password=password, **validated_data)
        user.save()
        return user
        