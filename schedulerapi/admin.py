from django.contrib import admin
from .models import Item, Pick

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ('severity', 'title', 'description', 'timeScheduled', 'weekly', 'yearly', 'monthly', 'daily')
    list_display = ['severity', 'title', 'description', 'timeNow', 'timeScheduled', 'weekly', 'yearly', 'monthly', 'daily']
    readonly_fields = ('timeNow',)
    search_fields = ('title', 'description')


@admin.register(Pick)
class PickAdmin(admin.ModelAdmin):
    fields = ('itemA', 'isDoneA', 'itemB', 'isDoneB', 'itemC', 'isDoneC')
    list_display = ['dayDate', 'itemA', 'isDoneA', 'itemB', 'isDoneB', 'itemC', 'isDoneC']
    readonly_fields = ('dayDate',)
    search_fields = ('dayDate',)