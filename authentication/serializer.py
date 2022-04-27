
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        print('Reached here')
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError('user name should only contain aplha-numerical characters ')
        return attrs

    def create(self, validated_data):
        return User.objects.create(**validated_data)

class EmailverificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=200)
    class meta:
        model = User
        fields = ['token']

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)
    password = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length= 255, read_only = True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'token']

    def validate(self, attr):
        email = attr.get('email', '')
        password = attr.get('password', '')
        user = authenticate(email = email, password = password)

        if user is None:
            raise AuthenticationFailed("Invalid account credentials")
        
        if not user.is_active:
            raise AuthenticationFailed("Your account is not active")
        
        if not user.is_verified:
            raise AuthenticationFailed("Your account is not Verified")
        
        
        
        

        return {
            'email':user.email,
            'password':user.password,
            'token':user.token()
            
        }



        