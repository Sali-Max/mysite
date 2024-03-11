from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class postsAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('name', 'status')
    list_filter = ('status',)
    search_fields = ('name','text')
    date_hierarchy = 'create_date'
    ordering = ('-create_date',)   
    list_editable = ('status',) 