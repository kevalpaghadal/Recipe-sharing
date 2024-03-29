# Generated by Django 5.0.2 on 2024-03-23 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_addrecipe_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addrecipe',
            name='photo',
            field=models.ImageField(max_length=250, null=True, upload_to='users/recipe_photos/'),
        ),
        migrations.AlterField(
            model_name='addrecipe',
            name='video',
            field=models.FileField(blank=True, max_length=250, null=True, upload_to='users/recipe_video/'),
        ),
    ]