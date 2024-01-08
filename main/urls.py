from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('', include('users.urls', namespace='users')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('categories.urls', namespace='categories')),
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
