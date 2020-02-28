from django.contrib import admin
from . import models


class CategoryTabolarInline(admin.TabularInline):
    model = models.Status


@admin.register(models.Status)
class AdminStatus(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class AdminCategory(admin.ModelAdmin):
    pass


@admin.register(models.File)
class AdminFile(admin.ModelAdmin):
    pass


@admin.register(models.Task)
class AdminTask(admin.ModelAdmin):
    list_display = ('title', 'create', 'user')
    list_editable = ('title',)
    list_display_links = ('create',)
    list_filter = ('create', 'status')
    search_fields = ('title', 'content',)
    # exclude            = ('user',)
    date_hierarchy = ('create')
    # actions          = [Status]
    inlines = [CategoryTabolarInline]
    fieldsets = (
        ('information', {
            "fields": ('title', 'content', 'name_file')
        }),
        ('time', {
            "fields": ('due_date',)
        }),
        ('detail information', {
            "fields": ('category', 'user',)
        }),
    )
