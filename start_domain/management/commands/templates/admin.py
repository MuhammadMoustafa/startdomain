from django.contrib import admin
from .models import Template

class TemplateAdmin(admin.ModelAdmin):
    # Define a function to get all fields of the model dynamically
    def get_fields(self, request, obj=None):
        return [field.name for field in obj._meta.fields]

    # Set list_display to include all fields
    list_display = get_fields(None, Template)

# Register your model with the custom admin class
admin.site.register(Template, TemplateAdmin)
