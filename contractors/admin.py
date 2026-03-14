from django.contrib import admin

from contractors.models import Contractor, Skill


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'contractor_skills', 'city', 'created_at']
    list_filter = ['name', 'skills__name','city']
    search_fields = ['name', 'city__name', 'skills__name']

    @staticmethod
    def contractor_skills(obj):
        return ', '.join(skill.name for skill in obj.skills.all())

admin.site.register(Skill)