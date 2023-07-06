from rest_framework.fields import ReadOnlyField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from .models import CardProduct


class CardProductCreateUpdateSerializer(ModelSerializer):
    id = ReadOnlyField()

    class Meta:
        model = CardProduct
        fields = ["id", "user_id", "title", "price", "photo", "short_desc", "detailed_desc",]
        read_only_fields = ["id"]




class CardProductViewDeleteSerializer(ModelSerializer):
    total_likes = SerializerMethodField()
    user_like = SerializerMethodField()

    def get_total_likes(self, obj):
        return obj.total_likes()

    def get_user_like(self, obj):
        return obj.user_like(self.context['request'].user)

    class Meta:
        model = CardProduct
        fields = ["id", "user_id", "title", "price", "photo", "short_desc", "detailed_desc", "total_likes", "user_like"]



class CardShortViewSerializer(ModelSerializer):
    total_likes = SerializerMethodField()
    user_like = SerializerMethodField()

    def get_total_likes(self, obj):
        return obj.total_likes()

    def get_user_like(self, obj):
        return obj.user_like(self.context['request'].user)

    class Meta:
        model = CardProduct
        fields = ["id", "photo", "title", "price", "photo", "short_desc", "total_likes", "user_like"]


