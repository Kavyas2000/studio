# Generated by Django 5.0.1 on 2024-03-12 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_app', '0006_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('purpose', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=10)),
            ],
        ),
    ]
