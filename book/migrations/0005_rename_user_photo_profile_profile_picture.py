# Generated by Django 5.1.5 on 2025-02-04 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_profile_user_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_photo',
            new_name='profile_picture',
        ),
    ]
