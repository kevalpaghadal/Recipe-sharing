# Generated by Django 5.0.2 on 2024-03-15 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_addrecipe_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='addrecipe',
            name='Servings',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
