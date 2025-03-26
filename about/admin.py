from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    list_display = ('title', 'content', 'updated_on')
    # search_fields = ['title', 'content']
    # list_filter = ('status', 'created_on')
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
