from django.urls import path
from .views import UserCreateView, UserListView, UserDetailView, UserUpdateView, UserDeleteView

app_name = 'users'

urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete')
]
