# Generated by Django 2.2.20 on 2021-04-25 16:31

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20210425_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
