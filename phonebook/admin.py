from django.contrib import admin
from . import models


class EntryAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'id']
    search_fields = ['name', 'phone']
    # list_filter = ['name', 'phone']


admin.site.register(models.Entry, EntryAdmin)
