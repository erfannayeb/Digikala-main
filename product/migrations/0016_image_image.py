# Generated by Django 3.2.7 on 2021-09-28 15:28

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to=product.models.product_image_path),
        ),
    ]
