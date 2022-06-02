from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Cards)
class CardsAdmin(admin.ModelAdmin):
    list_display = ('seria', 'number', 'creation_date', 'finish_date', 'status')
    list_display_links = ('seria', 'number')
    search_fields = ('seria', 'number', 'status')
    list_filter = ('status',)

admin.site.register(Status)
admin.site.register(History)