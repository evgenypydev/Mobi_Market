from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import send_verification_code
from django.contrib.auth import get_user_model

User = get_user_model()


from .models import User
from .utils import generate_verification_code
from .serializers import (
    UserCreateSerializer,
    UpdateUserPersonalInfoSerializer,
    UpdatePhoneNumberSerializer,
)


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    @swagger_auto_schema(
        request_body=UserCreateSerializer,
        operation_description="This endpoint create user.",
        responses={201: 'User create successfully', 400: 'Bad Request'}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UpdateUserPersonalInfoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="This endpoint return user",
        responses={
            200: UpdateUserPersonalInfoSerializer,
            400: 'Bad Request',
        }
    )
    def get(self, request):
        user = request.user
        serializer = UpdateUserPersonalInfoSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=UpdateUserPersonalInfoSerializer,
        operation_description="This endpoint update user profile.",
        responses={
            200: 'User profile update successfully',
            400: 'Bad Request'
        }
    )
    def put(self, request):
        user = request.user
        serializer = UpdateUserPersonalInfoSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Personal info added successfully.'}, status=status.HTTP_200_OK)


class UpdatePhoneNumberAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=UpdatePhoneNumberSerializer,
        operation_description="This endpoint add phone number for user.",
        responses={200: 'Phone number added successfully and verification code has been sent to your phone number.', 400: 'Bad Request'}
    )
    def put(self, request):
        user = request.user
        serializer = UpdatePhoneNumberSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            verification_code = generate_verification_code()
            user.verification_code = verification_code
            user.save()
            phone_number = user.phone_number
            send_verification_code(phone_number, verification_code)
            return Response({'message': 'Phone number added successfully and verification code has been sent to your phone number.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhoneNumberVerifyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="This endpoint verify code from user phone number.",
        responses={200: 'Phone number verified successfully.',400: 'Please enter the correct verification code.'}
    )
    def put(self, request):
        user = request.user
        verification_code = request.data.get('verification_code')
        if verification_code == user.verification_code:
            user.is_verified = True
            user.save()
            return Response({'message': 'Phone number verified successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Please enter the correct verification code.'}, status=status.HTTP_400_BAD_REQUEST)
