from django.db import models
from users.models import User

class CardProduct(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, editable=True)
    title = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    photo = models.ImageField(upload_to="mobi_market/card_products/", blank=True, null=True)
    short_desc = models.CharField(max_length=100, blank=True, null=True)
    detailed_desc = models.TextField(max_length=500, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:
            existing_value = CardProduct.objects.get(pk=self.pk).user_id
            if existing_value != self.user_id:
                raise ValueError('Cannot change the value of the field after object creation.')
        super().save(*args, **kwargs)