from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import send_verification_code
from django.contrib.auth import get_user_model

User = get_user_model()


from .serializers import UserCreateSerializer, UpdateUserPersonalInfoSerializer
from .models import User
from .utils import generate_verification_code


class UserCreateAPIView(APIView):

    @swagger_auto_schema(
        request_body=UserCreateSerializer,
        operation_description="This endpoint create user.",
        responses={201: 'User create successfully', 400: 'Bad Request'}
    )
    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data
        User.objects.create_user(user_data["username"], user_data["email"], user_data["password"])
        return Response(
            {'message': 'User create successfully'}, status=status.HTTP_201_CREATED
        )


class PhoneNumberVerificationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        verification_code = generate_verification_code()  # Функция для генерации кода подтверждения
        user.verification_code = verification_code  # Установка кода подтверждения для текущего пользователя
        user.save()

        phone_number = user.phone_number
        send_verification_code(phone_number, verification_code)  # Отправка SMS с кодом подтверждения

        # Здесь вы также можете сохранить код подтверждения в базе данных для дальнейшей проверки

        return Response({'message': 'A verification code has been sent to your phone number.'}, status=200)


class UpdateUserPersonalInfoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = UpdateUserPersonalInfoSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Personal info added successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhoneNumberVerifyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        verification_code = request.data.get('verification_code')

        if verification_code == user.verification_code:
            user.is_verified = True
            user.save()
            return Response({'message': 'Phone number verified successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Please enter the correct verification code.'}, status=status.HTTP_400_BAD_REQUEST)


