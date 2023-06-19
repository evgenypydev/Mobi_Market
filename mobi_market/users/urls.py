from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .endpoints import (
    UserCreateAPIView,
    UpdateUserPersonalInfoAPIView,
    UpdatePhoneNumberAPIView,
    PhoneNumberVerifyAPIView,
)

urlpatterns = [
    path("api/register/", UserCreateAPIView.as_view(), name="register"),
    path("api/user/profile/", UpdateUserPersonalInfoAPIView.as_view(), name="add_personal_info"),
    path("api/user/phonenumber/", UpdatePhoneNumberAPIView.as_view(), name="add_personal_info"),
    path('api/token/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/phone/verify/',PhoneNumberVerifyAPIView.as_view(), name='phone_verification'),
]