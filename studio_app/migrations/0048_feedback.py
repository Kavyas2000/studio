# Generated by Django 4.2.7 on 2024-05-11 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_app', '0047_design_delete_des'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=20)),
            ],
        ),
    ]
