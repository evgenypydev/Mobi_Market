from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import CardProduct
from .serializers import CardCreateUpdateViewProductSerializer, CardShortViewSerializer


# class CardProductViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = CardProductSerializer
#
#     def get_queryset(self, request):
#         user = request.user
#         queryset = CardProduct.objects.filter(id__in=user.id)
#         return queryset
#
#     def create(self, request, *args, **kwargs):
#         user = request.user
#         if user.id == request.data["user"]:
#             serializer = CardProductSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'message': 'You cannot add a product for another user'}, status=status.HTTP_403_FORBIDDEN)
#
#     def partial_update(self, request, *args, **kwargs):
#         user = request.user
#         if user.id == request.data["user"]:
#             instance = self.get_object()
#             serializer = CardProductSerializer(instance, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': 'You cannot update a product for another user'}, status=status.HTTP_403_FORBIDDEN)
#
#     def destroy(self, request, *args, **kwargs):
#         user = request.user
#         instance = self.get_object()
#         if user.id == instance.user.id:
#             instance.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response({'message': 'You cannot delete a product for another user'}, status=status.HTTP_403_FORBIDDEN)


class CardProductByUserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CardShortViewSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = CardProduct.objects.filter(user_id=user.id)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = CardCreateUpdateViewProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, *args, **kwargs):
        serializer = CardCreateUpdateViewProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

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
