# Generated by Django 3.1 on 2020-08-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roost', '0002_auto_20200816_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='preschedule',
            name='name',
            field=models.CharField(default='No name yet', max_length=50),
        ),
    ]