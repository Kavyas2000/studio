# Generated by Django 5.0.1 on 2024-04-22 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_app', '0032_alter_event_booking_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_booking',
            name='date',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='event_booking',
            name='time',
            field=models.CharField(max_length=30, null=True),
        ),
    ]