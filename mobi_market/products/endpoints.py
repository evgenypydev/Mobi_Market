from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import CardProduct
from .serializers import CardCreateUpdateViewProductSerializer, CardShortViewSerializer


class CardProductByUserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CardShortViewSerializer


    @swagger_auto_schema(
        operation_description="This endpoint return all user products.",
        responses={
            200: CardShortViewSerializer(many=True),
            400: 'Bad Request'
        }
    )
    def get_queryset(self):
        user = self.request.user
        queryset = CardProduct.objects.filter(user_id=user.id)
        return queryset

    @swagger_auto_schema(
        request_body=CardCreateUpdateViewProductSerializer,
        operation_description="This endpoint create user product.",
        responses={
            201: CardCreateUpdateViewProductSerializer,
            400: 'Bad Request'
        }
    )
    def create(self, request, *args, **kwargs):
        user = self.request.user
        request.data["user_id"] = user.id
        serializer = CardCreateUpdateViewProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        request_body=CardCreateUpdateViewProductSerializer,
        operation_description="This endpoint update user product.",
        responses={
            201: CardCreateUpdateViewProductSerializer,
            400: 'Bad Request'
        }
    )
    def partial_update(self, request, *args, **kwargs):
        serializer = CardCreateUpdateViewProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="This endpoint retrieve user product.",
        responses={
            201: CardCreateUpdateViewProductSerializer,
            400: 'Bad Request'
        }
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CardCreateUpdateViewProductSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CardProductListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CardProduct.objects.all()
    serializer_class = CardShortViewSerializer


class CardProductRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CardProduct.objects.all()
    serializer_class = CardCreateUpdateViewProductSerializer
    lookup_field = "id"
