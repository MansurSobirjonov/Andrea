from django.contrib import admin
from .models import Post, Comment, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    filter_horizontal = ('tags', )
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
