# Generated by Django 3.1.3 on 2020-12-24 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0004_auto_20201224_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctormodel',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
    ]
