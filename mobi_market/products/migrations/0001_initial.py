# Generated by Django 4.2.2 on 2023-06-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
        ),
    ]
