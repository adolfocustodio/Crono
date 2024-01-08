from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import CategoryForm
from .models import Category
from django.urls import reverse_lazy

class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CategoryForm
    model = Category
    success_url = reverse_lazy('categories:category-list')
    success_message = "A categoria foi criada com sucesso."

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'categories'
    paginate_by = 10

class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CategoryForm
    model = Category
    success_url = reverse_lazy('categories:category-list')
    success_message = "A categoria foi atualizada com sucesso."

class CategoryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('categories:category-list')
    success_message = "A categoria foi excluída com sucesso."
