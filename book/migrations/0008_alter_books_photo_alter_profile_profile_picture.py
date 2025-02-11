# Generated by Django 5.1.6 on 2025-02-08 20:21

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_books_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='photos/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='profile_picture/'),
        ),
    ]
