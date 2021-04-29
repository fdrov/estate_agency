# Generated by Django 2.2.20 on 2021-04-29 12:37

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20210429_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='floor',
            field=models.CharField(db_index=True, help_text='Первый этаж, последний этаж, пятый этаж', max_length=3, verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owners_phonenumber',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца'),
        ),
    ]