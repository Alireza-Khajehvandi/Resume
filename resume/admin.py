from django.contrib import admin
from resume.models import Project, Category


class ProjectsAdmin(admin.ModelAdmin):
    date_hierarchy = "published_date"
    empty_value_display = "-empty-"
    # fields = ["title"]
    # exclude = ["title"] # ignore this field
    list_display = ["title", "author", "counted_views",
                    "status", "published_date", "created_date"]
    list_filter = ["status", 'author']
    # ordering = ["created_date"]
    serch_fields = ["title", "content"]


admin.site.register(Project, ProjectsAdmin)

admin.site.register(Category)
