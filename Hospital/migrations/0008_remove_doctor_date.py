# Generated by Django 3.1.3 on 2020-12-25 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0007_auto_20201225_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='date',
        ),
    ]