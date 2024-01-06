from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc_preview', 'category')

    def desc_preview(self, obj):
        return obj.desc[:100] + '...'
