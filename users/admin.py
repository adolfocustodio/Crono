from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'bio_preview')

    def bio_preview(self, obj):
        return obj.bio[:100] + '...'
