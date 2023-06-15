# from phonenumber_field.formfields import PhoneNumberField
from rest_framework.serializers import ModelSerializer, Serializer

from .models import User


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email", "password"]


class UpdateUserPersonalInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "avatar", "birth_date", "phone_number"]