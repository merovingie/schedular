from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'timeScheduled', 'weekly', 'yearly', 'monthly', 'daily')
    list_display = ['title', 'description', 'timeNow', 'timeScheduled', 'weekly', 'yearly', 'monthly', 'daily']
    readonly_fields = ('timeNow',)
    search_fields = ('title', 'description')


