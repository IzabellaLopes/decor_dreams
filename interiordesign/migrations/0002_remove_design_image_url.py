# Generated by Django 3.2.23 on 2024-03-26 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interiordesign', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='design',
            name='image_url',
        ),
    ]
