from django.contrib import admin
from . import models

class CategoryTabolarInline(admin.TabularInline):
   pass


@admin.register(models.Status)
class AdminStatus(admin.ModelAdmin):
    list_display = ('status_type',)
    actions = ['make_status']

    def make_status(modeladmin, request, queryset):
        queryset.update(status_type=1)
    make_status.short_description = "Mark selected status"


@admin.register(models.Category)
class AdminCategory(admin.ModelAdmin):
    pass


@admin.register(models.File)
class AdminFile(admin.ModelAdmin):
    pass


@admin.register(models.Task)
class AdminTask(admin.ModelAdmin):
    list_display        = ('title', 'create', 'user', 'status',)
    list_editable       = ('title',)
    list_display_links  = ('create',)
    list_filter         = ('create', 'status')
    search_fields       = ('title', 'content',)
    date_hierarchy      = ('create')
    # exclude             = ('user',)
    # inlines = [CategoryTabolarInline]
    fieldsets = (
        ('information', {
            "fields": ('title', 'content', 'name_file')
        }),
        ('time', {
            "fields": ('due_date',)
        }),
        ('detail information', {
            "fields": ('category', 'user', 'status')
        }),
    )