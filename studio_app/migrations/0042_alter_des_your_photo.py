# Generated by Django 5.0.1 on 2024-05-01 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_app', '0041_rename_user_name_des_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='des',
            name='your_photo',
            field=models.FileField(upload_to='media'),
        ),
    ]