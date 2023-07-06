from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, CharField

from .models import User


class UserCreateSerializer(ModelSerializer):
    password = CharField(required=True, max_length=128, min_length=6, write_only=True)
    password_repeat = CharField(max_length=128, min_length=6, required=True, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password_repeat"]

    def validate(self, attrs):
        password = attrs.get('password')
        password_repeat = attrs.pop('password_repeat')
        if password != password_repeat:
            raise serializers.ValidationError({"error": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UpdateUserPersonalInfoSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name","birth_date", "avatar", "phone_number"]


class UpdatePhoneNumberSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["phone_number"]
