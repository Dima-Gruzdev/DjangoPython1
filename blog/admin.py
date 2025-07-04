from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'number_of_views', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('heading', 'content',)
