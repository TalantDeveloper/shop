# Generated by Django 5.0.4 on 2024-05-10 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_item_image_delete_itemimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='countblogabout',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
