from django.contrib import admin

from jobs.models import Job, City, Category


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'city', 'budget', 'status', 'created_at']
    list_filter = ['status', 'category', 'city']
    search_fields = ['title', 'description']

admin.site.register(City)
admin.site.register(Category)