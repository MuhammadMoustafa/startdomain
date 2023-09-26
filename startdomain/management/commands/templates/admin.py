from django.contrib import admin
from .models import Template

class TemplateAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Template._meta.get_fields()]

admin.site.register(Template, TemplateAdmin)
