# Generated by Django 5.0 on 2024-01-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to='avatars'),
        ),
    ]
