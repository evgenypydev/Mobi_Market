from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer

from .models import CardProduct


class CardCreateUpdateViewProductSerializer(ModelSerializer):
    id = ReadOnlyField()

    class Meta:
        model = CardProduct
        fields = ["id", "user_id", "title", "price", "photo", "short_desc", "detailed_desc"]
        read_only_fields = ["id"]


class CardShortViewSerializer(ModelSerializer):
    class Meta:
        model = CardProduct
        fields = ["id", "photo", "title", "price", "photo", "short_desc"]



