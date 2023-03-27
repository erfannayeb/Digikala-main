# Generated by Django 3.2.7 on 2021-09-15 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=500)),
                ('code', models.CharField(max_length=50)),
                ('expire', models.DateField()),
                ('percent', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
