# Generated by Django 5.0.1 on 2024-04-22 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_app', '0031_rename_user_frame_design_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_booking',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
