# Generated by Django 5.0.1 on 2024-05-01 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio_app', '0040_des_delete_design'),
    ]

    operations = [
        migrations.RenameField(
            model_name='des',
            old_name='user_name',
            new_name='user',
        ),
    ]