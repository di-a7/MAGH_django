from django.contrib import admin
from .models import Todolist
# Register your models here.

# @admin.register(Todolist)
class TodolistAdmin(admin.ModelAdmin):
   list_display = ("title","description","status")
   list_filter = ("status","title")           # Todolist.objects.filter("title" = "...", "status" = "...")
   list_per_page = 5
   list_editable = ('status',)

admin.site.register(Todolist, TodolistAdmin)