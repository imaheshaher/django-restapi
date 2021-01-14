from rest_framework import serializers
from .models import CustomUser,Blog
from rest_framework_jwt.settings import api_settings

from rest_framework_jwt.settings import api_settings
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields = "__all__"
    # def get_token(self, obj):
    #     jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    #     jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    #     payload = jwt_payload_handler(obj)
    #     token = jwt_encode_handler(payload)
    #     return token
    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password',instance.email)
        instance.set_password(instance.password)
        instance.save()
        return instance

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        excludes = ['user']
        fields = ('title','description')