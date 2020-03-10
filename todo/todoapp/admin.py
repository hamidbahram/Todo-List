from django.contrib import admin
from .models import Task, Category, File, User


class TaskTabolarInline(admin.TabularInline):
    # model = Task
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
    # inlines = [TaskTabolarInline]
    pass


@admin.register(File)
class AdminFile(admin.ModelAdmin):
    pass


@admin.register(Task)
class AdminTask(admin.ModelAdmin):

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(AdminTask, self).get_form(request, obj, **kwargs)
    #     form.base_fields['user'].initial = request.user
    #     return form

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            kwargs['queryset'] = User.objects.filter(username=request.user.username)
        return super(AdminTask, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.readonly_fields + ('user',)
        return self.readonly_fields

    list_display        = ('title', 'create', 'user', 'status_type',)
    list_editable       = ('title',)
    list_display_links  = ('create',)
    list_filter         = ('create', 'status_type',)
    search_fields       = ('title', 'content',)
    date_hierarchy      = ('create')
    actions             = [change_to_todo, change_to_doing,change_to_done ]
    # readonly_fields     = ['user',]
    # exclude           = ('user',)
    fieldsets           = (
                    ('information', {
                        "fields": ('title', 'content', 'name_file')
                    }),
                    ('time', {
                        "fields": ('due_date',)
                    }),
                    ('detail information', {
                        "fields": ('category', 'user', 'status_type')
                    }),
                )              