# Generated by Django 3.1.3 on 2020-12-30 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0018_auto_20201228_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patientmodel',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
