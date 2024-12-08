# Generated by Django 5.1.3 on 2024-12-06 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testemonail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.CharField(blank=True, max_length=255, null=True)),
                ('rating_count', models.IntegerField()),
                ('username', models.CharField(max_length=50, unique=True)),
                ('user_job_title', models.CharField(max_length=50)),
                ('review', models.TextField()),
            ],
        ),
    ]
