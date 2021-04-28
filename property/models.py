from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)
    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')
    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)
    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        db_index=True)
    new_building = models.BooleanField(null=True)
    likes = models.ManyToManyField(User, verbose_name='Кто лайкнул',
                                   blank=True)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Кто жаловался')
    flat = models.ForeignKey(Flat,
                             on_delete=models.CASCADE,
                             verbose_name='Квартира, на которую жаловались')
    complaint_text = models.TextField('Текст жалобы')


class Owner(models.Model):
    full_name = models.CharField(max_length=300, verbose_name='ФИО владельца',
                                 db_index=True)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20)
    owner_pure_phone = PhoneNumberField(blank=True,
                                        verbose_name='Нормализованный номер владельца')
    estates = models.ManyToManyField(Flat,
                                     verbose_name='Квартиры в собственности',
                                     related_name='estate_owners')

    def display_estates(self):
        return ', '.join([estate.address for estate in self.estates.all()[:3]])
    display_estates.short_description = 'Квартиры'


    def __str__(self):
        return self.full_name
