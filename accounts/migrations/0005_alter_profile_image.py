# Generated by Django 3.2.7 on 2021-09-26 16:48

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210915_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.user_profile_image_path),
        ),
    ]
