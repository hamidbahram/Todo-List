from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Category)
class AdminCategory(admin.ModelAdmin):
    pass

@admin.register(models.Task)
class AdminCategory(admin.ModelAdmin):
    pass

@admin.register(models.File)
class AdminCategory(admin.ModelAdmin):
    pass