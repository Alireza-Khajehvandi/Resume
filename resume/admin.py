from django.contrib import admin
from resume.models import Projects, Contact


class ProjectsAdmin(admin.ModelAdmin):
    date_hierarchy = "published_date"
    empty_value_display = "-empty-"
    # fields = ["title"]
    # exclude = ["title"] # ignore this field
    list_display = ["title", "counted_views", "status", "published_date", "created_date"]
    list_filter = ["status"]
    # ordering = ["created_date"]
    serch_fields = ["title", "content"]

admin.site.register(Projects, ProjectsAdmin)

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ["name", "email", "created_date"]
    list_filter = ["email"]
    serch_fields = ["name", "message"]
    
# Register your models here.
admin.site.register(Contact, ContactAdmin)
