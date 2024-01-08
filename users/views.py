from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import UserRegistrationForm
from .models import User
from django.urls import reverse_lazy

class UserCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    model = User
    success_url = reverse_lazy('user-list')
    success_message = "O usuário foi criado com sucesso."

class UserListView(LoginRequiredMixin, ListView):
    model = User
    context_object_name = 'users'
    paginate_by = 10

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User

class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = UserRegistrationForm
    model = User
    success_url = reverse_lazy('user-list')
    success_message = "O usuário foi atualizado com sucesso."

class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy('user-list')
    success_message = "O usuário foi excluído com sucesso."
