from django.urls import include, path, re_path
from rest_framework import routers

from .endpoints import CardProductByUserViewSet, CardProductListAPIView, CardProductRetrieveAPIView

router = routers.DefaultRouter()
router.register(r'', CardProductByUserViewSet, basename='my_products')

urlpatterns = [
    path('my_products/', include(router.urls)),
    path('main_page/', CardProductListAPIView.as_view()),
    re_path('main_page/(?P<id>.+)/', CardProductRetrieveAPIView.as_view()),
]
