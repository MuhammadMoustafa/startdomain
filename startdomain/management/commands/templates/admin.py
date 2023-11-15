from django.contrib import admin
from .models import Template

class TemplateAdmin(admin.ModelAdmin):
    list_display = []
    for f in Template._meta.concrete_fields:
        if f.many_to_many:
            continue
        list_display.append(f.name)

admin.site.register(Template, TemplateAdmin)
