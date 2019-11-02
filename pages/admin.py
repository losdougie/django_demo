from django.contrib import admin

# Register your models here.
from .models import ToDo, ToDoType

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'priority', 'status', 'title','working')
    list_display_links = ('id', 'title')
    list_filter = ('status',)
    list_editable = ('working',)
    search_fields = ('title', 'desc')
    list_per_page = 20

admin.site.register(ToDo, ToDoAdmin)
admin.site.register(ToDoType)