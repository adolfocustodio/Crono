from django.urls import path
from .views import CategoryCreateView, CategoryListView, CategoryUpdateView, CategoryDeleteView

app_name = 'categories'

urlpatterns = [
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete')
]
