from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'created_at', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building']
    pass

# admin.site.register(Flat, FlatAdmin)
