# Generated by Django 5.1.3 on 2024-12-07 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_authur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='authur',
        ),
    ]
