# Generated by Django 5.0.2 on 2024-02-24 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_address_user_city_user_country_user_pin_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='addrecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users/addrecipe_photo')),
                ('ingrediants', models.CharField(max_length=100)),
                ('step', models.CharField(max_length=250)),
            ],
        ),
    ]
