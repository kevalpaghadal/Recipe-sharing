# Generated by Django 5.0.2 on 2024-03-22 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_alter_review_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='addrecipe',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='users/recipe_video/'),
        ),
    ]