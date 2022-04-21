
from rest_framework import serializers
from .models import User

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
        