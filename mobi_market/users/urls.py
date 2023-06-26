from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .endpoints import (
    UserCreateAPIView,
    UpdateUserPersonalInfoAPIView,
    UpdatePhoneNumberAPIView,
    PhoneNumberVerifyAPIView,
)

urlpatterns = [
    path("user/register/", UserCreateAPIView.as_view(), name="register"),
    path("user/profile/", UpdateUserPersonalInfoAPIView.as_view(), name="add_personal_info"),
    path("user/phonenumber/", UpdatePhoneNumberAPIView.as_view(), name="add_personal_info"),
    path('user/token/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/phone/verify/',PhoneNumberVerifyAPIView.as_view(), name='phone_verification'),
]