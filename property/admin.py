from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'new_building']
    fieldsets = (
        (None, {
            'fields': ('address', 'description', 'price', 'town', 'town_district')
        }),
        ('Про здание', {
            'fields': ('floor', 'rooms_number', 'living_area', 'has_balcony')
        }),
        ('Мета-инфа', {
            'fields': ('construction_year', 'new_building','active', 'likes', 'created_at')
        }),
    )
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['likes']

@ admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']
    pass


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['estates']
    list_display = ['full_name', 'display_estates']
    search_fields = ['full_name']
