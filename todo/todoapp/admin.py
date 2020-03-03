from django.contrib import admin
from .models import Task, Category, File


class CategoryTabolarInline(admin.TabularInline):
    pass


def change_to_todo(modeladmin, request, queryset):
    queryset.update(status_type=Task.TODO)
change_to_todo.short_description = "selected task as change to todo"


def change_to_doing(modeladmin, request, queryset):
    queryset.update(status_type=Task.DOING)
change_to_doing.short_description = "selected task as change to doing"


def change_to_done(modeladmin, request, queryset):
    queryset.update(status_type=Task.DONE)
change_to_done.short_description = "selected task as change to done"


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass


@admin.register(File)
class AdminFile(admin.ModelAdmin):
    pass


@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display        = ('title', 'create', 'user', 'status_type',)
    list_editable       = ('title',)
    list_display_links  = ('create',)
    list_filter         = ('create', 'status_type',)
    search_fields       = ('title', 'content',)
    date_hierarchy      = ('create')
    actions             = [change_to_todo, change_to_done, change_to_doing]
    # exclude           = ('user',)
    # inlines           = [CategoryTabolarInline]
    fieldsets           = (
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