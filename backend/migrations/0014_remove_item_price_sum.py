# Generated by Django 5.0.6 on 2024-09-10 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_item_price_sum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='price_sum',
        ),
    ]
