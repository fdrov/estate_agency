# Generated by Django 2.2.20 on 2021-04-25 16:38

from django.db import migrations
import phonenumbers


def pure_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        pure_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if not phonenumbers.is_valid_number(pure_number):
            continue
        flat.owner_pure_phone = phonenumbers.format_number(
            pure_number,
            phonenumbers.PhoneNumberFormat.E164
        )
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(pure_phone_numbers)
    ]
