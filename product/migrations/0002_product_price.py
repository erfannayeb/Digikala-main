# Generated by Django 3.2.7 on 2021-09-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
