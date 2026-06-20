from django.contrib import admin
from .models import Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'company', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('name', 'email', 'company')

admin.site.register(Lead, LeadAdmin)
