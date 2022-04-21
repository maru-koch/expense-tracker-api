
from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email')
        username = attrs.get('username')
        if not username.isalnum():
            raise serializers.ValidationError('user name should only contain aplha-numerical characters ')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user