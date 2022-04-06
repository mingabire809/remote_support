from django.contrib import admin
from .models import Help


# Register your models here.

class HelpAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'subject', 'description', 'address')
    search_fields = ('full_name', 'email', 'phone', 'subject', 'address')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Help, HelpAdmin)
