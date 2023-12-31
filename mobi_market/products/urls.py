from django.urls import include, path, re_path
from rest_framework import routers

from .endpoints import (
    CardProductByUserViewSet,
    CardProductListAPIView,
    CardProductRetrieveAPIView,
    AddUserToProductView,
    DeleteUserFromProductView,
    FavouriteCardItemRetrieveApiView,
    FavouriteCardItemListApiView,
)

router = routers.DefaultRouter()
router.register(r'', CardProductByUserViewSet, basename='my_products')

urlpatterns = [
    path('my_products/', include(router.urls)),
    path('main_page/', CardProductListAPIView.as_view()),
    path('favourite_products/', FavouriteCardItemListApiView.as_view()),
    re_path('favourite_products/(?P<pk>.+)/', FavouriteCardItemRetrieveApiView.as_view()),
    re_path('main_page/(?P<id>.+)/', CardProductRetrieveAPIView.as_view()),
    re_path('product/(?P<id>.+)/like/', AddUserToProductView.as_view()),
    re_path('product/(?P<id>.+)/unlike/', DeleteUserFromProductView.as_view()),

]
