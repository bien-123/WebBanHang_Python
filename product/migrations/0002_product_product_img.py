# Generated by Django 3.2.15 on 2023-08-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.CharField(default='', max_length=255),
        ),
    ]
