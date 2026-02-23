from django.contrib import admin

from applications.models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['job','contractor','status','price_quote','created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['job__title', 'contractor__name']
