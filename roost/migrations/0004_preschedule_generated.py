# Generated by Django 3.1 on 2020-08-25 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roost', '0003_preschedule_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='preschedule',
            name='generated',
            field=models.BooleanField(default=False),
        ),
    ]
