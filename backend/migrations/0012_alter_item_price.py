# Generated by Django 5.0.6 on 2024-09-08 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_remove_item_image_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True, verbose_name='Цена товара'),
        ),
    ]