# Generated by Django 4.2.19 on 2025-03-18 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_phone',
            field=models.CharField(max_length=20),
        ),
    ]
