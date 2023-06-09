# Generated by Django 3.2.7 on 2021-09-15 16:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.EmailField(max_length=50, unique=True)),
                ('last_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(8)])),
                ('phoneNumber', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='ایمیل')),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('companyName', models.CharField(max_length=200)),
                ('companyType', models.CharField(choices=[('pu', 'public'), ('pr', 'private'), ('l', 'limited'), ('c', 'coop')], max_length=2)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('province', models.CharField(max_length=200)),
                ('postalCode', models.CharField(max_length=200)),
            ],
        ),
    ]
