from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner', 'owners_phonenumber']
    readonly_fields = ['created_at']
    list_display = ['address', 'owners_phonenumber', 'owner_pure_phone']
    # list_editable = ['new_building']
    # list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['likes']


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']
    pass


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['estates']
# admin.site.register(Flat, FlatAdmin)
