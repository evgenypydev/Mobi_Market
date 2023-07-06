# Generated by Django 4.2.2 on 2023-07-06 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CardProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='mobi_market/card_products/')),
                ('short_desc', models.CharField(blank=True, max_length=100, null=True)),
                ('detailed_desc', models.TextField(blank=True, max_length=500, null=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_card_products', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
