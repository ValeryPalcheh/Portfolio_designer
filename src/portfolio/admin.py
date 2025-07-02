from django.contrib import admin
from .models import Category, Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
    inlines = [ProjectImageInline]

admin.site.register(Category)
admin.site.register(Project, ProjectAdmin)

