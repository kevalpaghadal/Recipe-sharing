# Generated by Django 5.0.2 on 2024-03-22 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_alter_addrecipe_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.addrecipe'),
        ),
    ]
